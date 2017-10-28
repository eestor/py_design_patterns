
from abs_class import AbsClass

class Vm(AbsClass):

    def __init__(self, name):
        self._obj_name = name

    def get_data(self, task_name):
        print('Doing task of {} for {}'.format(task_name, self._obj_name))