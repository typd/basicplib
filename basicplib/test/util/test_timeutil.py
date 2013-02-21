import basicplib.util.timeutil as t

def test_curr_time_int():
    print t.curr_time_int()
    curr = t.curr_time_int()
    assert curr > 1361108082
