
from .abs_vc_object import AbsVcObject

class Vm(AbsVcObject):


    def start(self):
        print("Starting virtual machine")


    def shutdown(self):
        print("Shutting down virtual machine")