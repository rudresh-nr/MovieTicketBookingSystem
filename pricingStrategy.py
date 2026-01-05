from abc import ABC, abstractmethod
from decimal import Decimal

class PricingStrategy(ABC):

    @abstractmethod
    def getPrice(self) -> Decimal:
        pass


class NormalPrice(PricingStrategy):
     def getPrice(self) -> Decimal:
         return Decimal(100.00)


class premiumPrice(PricingStrategy):
    def getPrice(self) -> Decimal:
        return Decimal(150.00)
    

class VIPPrice(PricingStrategy):
    def getPrice(self) -> Decimal:
        return Decimal(200.00)