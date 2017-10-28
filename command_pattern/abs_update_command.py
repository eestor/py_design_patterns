
import abc

class AbsUpdateCommand(metaclass=abc.ABCMeta):


    @abc.abstractproperty
    def name(self):
        pass


    @abc.abstractproperty
    def description(self):
        pass
