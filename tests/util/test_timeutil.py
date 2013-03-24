import datetime

import basicplib.util.timeutil as tutil


def test_curr_time_int():
    curr = tutil.curr_time_int()
    assert curr > 1361108082


def test_format_duration():
    assert "0:00" == tutil.format_duration(0)
    assert "0:32" == tutil.format_duration(32)
    assert "1:32" == tutil.format_duration(92)
    assert "1:01:32" == tutil.format_duration(3692)


def test_shift_datetime():
    now = datetime.datetime.now()
    shifted = tutil.shift_datetime(datetime.datetime.now(), days=-10)
    delta = now - shifted
    print delta
    print delta.total_seconds()
    assert abs(delta.total_seconds() - 10 * 24 * 3600) < 0.1 
