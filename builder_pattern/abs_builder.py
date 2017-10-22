import abc
from computer import Computer


class AbsBuilder(metaclass=abc.ABCMeta):
    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def build_mainboard(self):
        pass
