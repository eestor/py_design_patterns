
class Director(object):

    def __init__(self, builder):
        self._builder = builder


    def build_computer(self):
        self._builder.new_computer()
        self._builder.build_mainboard()


    def get_computer(self):
        return self._builder.get_computer()
