from basicplib.util.strutil import is_str

def test_is_str():
    assert is_str('')
    assert is_str(' ')
    assert not is_str(3)
    assert is_str(u'aa')
