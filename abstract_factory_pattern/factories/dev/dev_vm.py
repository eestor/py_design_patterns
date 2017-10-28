
from ..abs_object import AbsObject

class DevVm(AbsObject):

    def start(self):
        print("Starting dev vm")


    def shutdown(self):
        print("Shutting down dev vm")