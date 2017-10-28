
import abc

class AbsFactory(metaclass=abc.ABCMeta):

    @abc.abstractstaticmethod
    def create_vm():
        pass

    @abc.abstractstaticmethod
    def create_esx():
        pass