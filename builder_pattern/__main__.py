from director import Director
from regular_computer import RegularComputer
from special_computer import SpecialComputer


computer_builder = Director(RegularComputer())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(SpecialComputer())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()
