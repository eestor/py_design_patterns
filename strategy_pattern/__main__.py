
from strategy_factory import StrategyFactory
from ups_strategy import UpsStrategy
from fedex_strategy import FedexStrategy



calc_method = UpsStrategy(40)
strategy = StrategyFactory(calc_method)
result = strategy.compute()
print("UPS Total Cost : %0.2f " %result)

calc_method = FedexStrategy(40)
strategy = StrategyFactory(calc_method)
result = strategy.compute()
print("FEDEX Total Cost : %0.2f " % result)

