import locale
from subprocess import check_output, CalledProcessError, Popen, PIPE

#decrator
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


def save_execute(func, *args, **kargs):
    try:
        return func(*args, **kargs), True
    except:
        return None, False 
