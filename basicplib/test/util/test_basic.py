from basicplib.util.basic import *
from multiprocessing import Process
from subprocess import Popen, PIPE

def test_singleton():
    @singleton
    class A:
        pass
    class B:
        pass
    a = A()
    b = A()
    assert id(a) == id(b)
    a = B()
    b = B()
    assert id(a) != id(b)

def test_save_execute():
    def _divide(a, b):
        return a / b
    def _func_with_dict_param(a, b=2):
        return a / b
    def _func_without_return(a, b=2):
        pass 
    v, r = save_execute(_divide, 1.0, 2.0)
    assert v == 0.5 and r == True
    v, r = save_execute(_divide, 1.0, 0.0)
    assert (v == None) and r == False 
    v, r = save_execute(_func_with_dict_param, 2.0, 4.0)
    assert v == 0.5 and r == True
    v, r = save_execute(_func_with_dict_param, b=2, a=4)
    assert v == 2 and r == True
    v, r = save_execute(_func_with_dict_param, 4, b=2)
    assert v == 2 and r == True
    v, r = save_execute(_func_without_return, 2.0, 4.0)
    assert (v == None) and (r == True)
    from basicplib.util.network import download
    v, r = save_execute(download, "wrongurl")
    assert (v == None) and (r == False)

def test_kill_processes():
    p = Popen('sleep 1234509887', stderr=PIPE, stdout=PIPE, shell=True)
    assert (True, 0) == kill_processes(['sleep', '1234509888'], True)
    assert (True, 1) == kill_processes(['sleep', '1234509887'], True)
    assert (True, 0) == kill_processes(['sleep', '1234509887'], True)
