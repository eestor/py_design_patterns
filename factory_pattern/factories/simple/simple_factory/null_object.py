
from .abs_vc_object import AbsVcObject

class NullObject(AbsVcObject):

    def __init__(self, obj_name):
        self.obj_name = obj_name


    def start(self):
        print("Unknown object: {}".format(self.obj_name))


    def shutdown(self):
        pass


