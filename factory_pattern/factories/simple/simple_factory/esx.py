
from .abs_vc_object import AbsVcObject

class Esx(AbsVcObject):

    def start(self):
        print("Starting esx machine")


    def shutdown(self):
        print("Shutting down esx machine")