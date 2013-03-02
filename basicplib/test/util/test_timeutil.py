import basicplib.util.timeutil as t

def test_curr_time_int():
    curr = t.curr_time_int()
    assert curr > 1361108082

def test_format_duration():
    assert "0:00" == t.format_duration(0)
    assert "0:32" == t.format_duration(32)
    assert "1:32" == t.format_duration(92)
    assert "1:01:32" == t.format_duration(3692)
