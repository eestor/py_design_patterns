


from abs_strategy import AbsStrategy

class UpsStrategy(AbsStrategy):
    SHIP_COST = 200.00  # Php per kg.
    SERVICE_FEE = 300.00

    def __init__(self, weight):
        self.weight = weight

    def calculate(self):
        return self.SERVICE_FEE + self.SHIP_COST * self.weight
