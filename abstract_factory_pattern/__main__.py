from factories.prod_factory import ProdFactory
from factories.dev_factory import DevFactory

for factory in ProdFactory, DevFactory:
    vm = factory.create_vm()
    vm.start()
    vm.shutdown()

    esx = factory.create_esx()
    esx.start()
    esx.shutdown()
