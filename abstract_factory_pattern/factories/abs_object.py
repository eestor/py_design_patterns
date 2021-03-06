
import abc

class AbsObject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def shutdown(self):
        pass