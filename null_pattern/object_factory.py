
from virtual_machine import Vm
from null_class import NullClass

class VcObjectFactory:

    @staticmethod
    def create_task_for_obj(obj_name):
        if obj_name == 'vm1':
            return Vm(obj_name)
        else:
            return NullClass(obj_name)
