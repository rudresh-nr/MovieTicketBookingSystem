from screening import Screening
from seat import Seat
from decimal import Decimal

class Ticket:

    def __init__(self, screening: Screening, seat:Seat, price: Decimal):
        self.screening = screening
        self.seat = seat
        self.price = price