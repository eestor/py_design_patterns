
from abc import abstractmethod, ABCMeta

class AbsStrategy(metaclass = ABCMeta ):

    @abstractmethod
    def calculate(self):
        pass