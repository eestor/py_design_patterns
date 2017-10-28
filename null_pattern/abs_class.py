
import abc

class AbsClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_data(selfself, obj_name):
        pass