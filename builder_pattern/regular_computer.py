from abs_builder import AbsBuilder

class RegularComputer(AbsBuilder):


    def build_mainboard(self):
        self._computer.type = "Regular"
        self._computer.memory = "16 GB"
        self._computer.cpu = "Intel Core i5"
