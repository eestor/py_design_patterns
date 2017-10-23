

import abc

class AbsFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_vc_object(self):
        pass

