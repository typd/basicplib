import tempfile
import shutil
import os

from basicplib.util.fileutil import purge_filename, ensure_path, get_size
from basicplib.util.fileutil import get_size_str, save, ensure_dir
from basicplib.util.fileutil import is_dir_path, convert_to_valid_path


def write_file(path, length):
    ensure_path(path)
    save(' ' * length, path)

def test_convert_to_valid_path():
    assert convert_to_valid_path('aB098') == 'aB098'
    assert convert_to_valid_path('aB098.dat') == 'aB098.dat'
    assert convert_to_valid_path('a/') == 'a/'
    assert convert_to_valid_path('a/8') == 'a/8'
    assert convert_to_valid_path('abc *()') == 'abc'
    assert convert_to_valid_path('abc *():', '-') == 'abc ----'
    assert convert_to_valid_path('abc\ndef\tg') == 'abcdefg'

def test_is_dir_path():
    assert is_dir_path('abc/')
    assert is_dir_path('abc/a') == False
    assert is_dir_path('') == False
    assert is_dir_path(None) == False

def test_save():
    directory = tempfile.mkdtemp()
    save(b' ' * 20, os.path.join(directory, 'temp.dat'))
    save(b' ' * 20, os.path.join(directory, 'dir/temp.dat'))
    shutil.rmtree(directory)

def test_purge_filename():
    assert purge_filename('aa/b') == 'aa b'
    assert purge_filename('aa/b/c') == 'aa b c'
    assert purge_filename('aa/b/c/') == 'aa b c '
    assert purge_filename('aa:b:c:') == 'aa b c '

def test_ensure_dir():
    def _assert(path):
        ensure_dir(path)
        dir_name = os.path.dirname(path)
        assert os.path.exists(dir_name)
        if not os.path.isdir(path):
            assert not os.path.exists(path)
    directory = tempfile.mkdtemp()
    _assert(os.path.join(directory, "abc/"))
    _assert(os.path.join(directory, "abc/file"))
    _assert(os.path.join(directory, "dir1/dir2/file"))
    shutil.rmtree(directory)

def test_ensure_path():
    def _assert(path, is_dir):
        ensure_path(path)
        assert os.path.exists(path)
        assert os.path.isdir(path) == is_dir
    directory = tempfile.mkdtemp()
    _assert(os.path.join(directory, "abc/"), True)
    _assert(os.path.join(directory, "abc/file"), False)
    _assert(os.path.join(directory, "dir1/dir2/file"), False)
    shutil.rmtree(directory)

def test_file_size_dir():
    _dir = tempfile.mkdtemp()
    path1 = os.path.join(_dir, "abc/file")
    write_file(path1, 1234)
    assert 1234 == get_size(_dir)
    assert 1234 == get_size(os.path.join(_dir, "abc"))
    path2 = os.path.join(_dir, "file2")
    write_file(path2, 300)
    assert 1534 == get_size(_dir)
    assert 1234 == get_size(os.path.join(_dir, "abc"))

def test_file_size_file():
    def _assert(length, size_str):
        temp = tempfile.NamedTemporaryFile()
        write_file(temp.name, length)
        assert length == get_size(temp.name)
        assert size_str == get_size_str(temp.name)
        temp.close()
    _assert(100, '100B')
    _assert(1011, '1.01K')
    _assert(8016, '8.02K')
    _assert(1085000, '1.08M')
