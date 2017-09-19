

class StrategyFactory(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def compute(self):
        return self.strategy.calculate()