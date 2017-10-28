from .abs_factory import AbsFactory
from .dev.dev_esx import DevEsx
from .dev.dev_vm import DevVm


class DevFactory(AbsFactory):
    @staticmethod
    def create_vm():
        return DevVm()

    @staticmethod
    def create_esx():
        return DevEsx()
