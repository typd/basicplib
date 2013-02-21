from basicplib.util.file import *
import tempfile

def test_purge_filename():
    assert purge_filename('aa/b') == 'aa b'
    assert purge_filename('aa/b/c') == 'aa b c'
    assert purge_filename('aa/b/c/') == 'aa b c '
    assert purge_filename('aa:b:c:') == 'aa b c '

def test_file_size():
    try:
        temp = tempfile.NamedTemporaryFile()
        temp.write(' ' * 100)
        temp.flush()
        assert 100 == get_size(temp.name)
        assert '100B' == get_size_str(temp.name)
        temp.seek(0)
        
        temp.write(' ' * 1011)
        temp.flush()
        assert 1011 == get_size(temp.name)
        assert '1.01K' == get_size_str(temp.name)
        temp.seek(0)

        temp.write(' ' * 8016)
        temp.flush()
        assert 8016 == get_size(temp.name)
        assert '8.02K' == get_size_str(temp.name)
        temp.seek(0)

        temp.write(' ' * 1085000)
        temp.flush()
        assert 1085000 == get_size(temp.name)
        assert '1.08M' == get_size_str(temp.name)
        temp.seek(0)
    finally:
        temp.close()
