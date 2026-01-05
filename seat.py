from pricingStrategy import NormalPrice, PricingStrategy, premiumPrice, VIPPrice

class Seat:
    
    def __init__(self, seat_number: str, pricing_strategy: PricingStrategy):
        self.seat_number = seat_number
        self.pricing_strategy = pricing_strategy

    def get_price(self):
        return self.pricing_strategy.getPrice()
    


# Example usage:

seat_a1 = Seat("A1", NormalPrice())
seat_b2 = Seat("B2", premiumPrice())
seat_c3 = Seat("C3", VIPPrice())

print(f"Seat {seat_a1.seat_number} Price: ${seat_a1.get_price()}")
print(f"Seat {seat_b2.seat_number} Price: ${seat_b2.get_price()}")
print(f"Seat {seat_c3.seat_number} Price: ${seat_c3.get_price()}")