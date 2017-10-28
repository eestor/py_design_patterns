

from abs_command import AbsCommand

class NoCommand(AbsCommand):

    def __init__(self, args):
        self._command = args[0]
        pass


    def execute(self):
        print("No command named {}".format(self._command))

