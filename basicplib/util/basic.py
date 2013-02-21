import os
from subprocess import Popen, PIPE

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

def kill_processes(keywords, hard_kill=False):
    if keywords == None or len(keywords) == 0:
        raise ValueError("need keywords to kill process")
    pscmd = 'ps auxwww | grep "' + '" | grep "'.join(keywords) + '"'
    p = Popen(pscmd, stderr=PIPE, stdout=PIPE, shell=True)
    out, err = p.communicate()
    exit_code = p.poll()
    if exit_code:
        return False, 0
    succ = True
    killed = 0
    for line in out.splitlines():
        if pscmd in line:
            continue
        parts = line.split()
        pid = parts[1]
        cmd = 'kill %s' % pid
        if hard_kill:
            cmd = 'kill -9 %s' % pid
        p = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
        out, err = p.communicate()
        exit_code = p.poll()
        if exit_code:
            print cmd
            print line + " " + str(exit_code)
            succ = False
        else:
            killed += 1
    return succ, killed 

"""
def get_pid():
    return os.getpid()
"""

"""
def current_dir():
    return os.path.dirname(os.path.abspath(__file__))
"""
