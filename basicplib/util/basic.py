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

def get_pids(keywords):
    if not keywords:
        raise ValueError("need keywords")
    pscmd = 'ps auxwww | grep "' + '" | grep "'.join(keywords) + '"'
    try:
        print pscmd
        out = check_output(pscmd, shell=True)
    except CalledProcessError:
        return []
    result = [line.split()[1] for line in out.splitlines() if pscmd not in line]
    return result

def kill_processes(keywords, hard_kill=False):
    pids = get_pids(keywords)
    succ = True
    killed = 0
    for pid in pids:
        cmd = 'kill %s' % pid
        if hard_kill:
            cmd = 'kill -9 %s' % pid
        proc = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
        proc.communicate()
        exit_code = proc.poll()
        if exit_code:
            succ = False
        else:
            killed += 1
    return succ, killed 

#def get_pid():
#    return os.getpid()
#def current_dir():
#    return os.path.dirname(os.path.abspath(__file__))
