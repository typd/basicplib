from basicplib.util.basic import singleton, save_execute


def test_singleton():
    @singleton
    class Acls:
        pass
    class Bcls:
        pass
    acls = Acls()
    bcls = Acls()
    assert id(acls) == id(bcls)
    acls = Bcls()
    bcls = Bcls()
    assert id(acls) != id(bcls)

def test_save_execute():
    def _divide(avar, bvar):
        return avar / bvar
    def _func_with_dict_param(avar, bvar=2):
        return avar / bvar
    def _func_without_return(avar, bvar=2):
        pass 
    val, res = save_execute(_divide, 1.0, 2.0)
    assert val == 0.5 and res == True
    val, res = save_execute(_divide, 1.0, 0.0)
    assert (val == None) and res == False 
    val, res = save_execute(_func_with_dict_param, 2.0, 4.0)
    assert val == 0.5 and res == True
    val, res = save_execute(_func_with_dict_param, bvar=2, avar=4)
    assert val == 2 and res == True
    val, res = save_execute(_func_with_dict_param, 4, bvar=2)
    assert val == 2 and res == True
    val, res = save_execute(_func_without_return, 2.0, 4.0)
    assert (val == None) and (res == True)
