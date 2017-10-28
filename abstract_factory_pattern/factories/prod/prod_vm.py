
from ..abs_object import AbsObject

class ProdVm(AbsObject):

    def start(self):
        print("Starting prod vm")


    def shutdown(self):
        print("Shutting down prod vm")