from .abs_factory import AbsFactory
from .prod.prod_esx import ProdEsx
from .prod.prod_vm import ProdVm

class ProdFactory(AbsFactory):


    @staticmethod
    def create_vm():
        return ProdVm()

    @staticmethod
    def create_esx():
        return ProdEsx()
