
from null_object import NullObject
from abs_factory import AbsFactory

class EsxFactory(AbsFactory):

    def create_vc_object(self):
        self.null_obj = null_obj =  NullObject()
        null_obj.name = 'Unknown Object'
        return null_obj