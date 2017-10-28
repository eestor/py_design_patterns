
from abs_class import AbsClass

class NullClass(AbsClass):

    def __init__(self, obj_name):
        self._obj_name = obj_name

    def get_data(self, task_name):
        print("Unable to  do task of:  {} for {}".format(task_name, self._obj_name))