
from vm import Vm
from abs_factory import AbsFactory

class VmFactory(AbsFactory):

    def create_vc_object(self):
        self.vm = vm =  Vm()
        vm.name = 'devvma1'
        return vm
