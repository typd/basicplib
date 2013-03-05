import time

#curr_time_int = lambda: int(time.time())
def curr_time_int():
    return int(time.time())

def format_duration(duration):
    if duration < 60:
        return '0:{0:02d}'.format(duration)
    elif duration < (60 * 60):
        minutes = duration // 60
        seconds = duration - (minutes * 60)
        return '{0:d}:{1:02d}'.format(minutes, seconds)
    else:
        hours = duration // (60 * 60)
        minutes = (duration - (hours * 60 * 60)) // 60
        seconds = (duration - (hours * 60 * 60) - (minutes * 60))
        return '{0:d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)
