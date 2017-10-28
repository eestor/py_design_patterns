
from esx import Esx
from abs_factory import AbsFactory

class EsxFactory(AbsFactory):

    def create_vc_object(self):
        self.esx = esx =  Esx()
        esx.name = 'Devvhs71'
        return esx