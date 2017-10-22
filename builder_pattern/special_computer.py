from abs_builder import AbsBuilder

class SpecialComputer(AbsBuilder):


    def build_mainboard(self):
        self._computer.type = "Special"
        self._computer.memory = "22 GB"
        self._computer.cpu = "Intel Core i7"
