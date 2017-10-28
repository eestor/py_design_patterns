
from abs_object import AbsObject

class NullObject(AbsObject):

    def __init__(self, obj_name):
        self.obj_name = obj_name


    def start(self):
        print("Unknown object: {}".format(self.obj_name))


    def shutdown(self):
        pass


