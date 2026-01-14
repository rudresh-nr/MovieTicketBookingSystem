from __future__ import annotations
from datetime import datetime, timedelta
from decimal import Decimal
from typing import List

from ticket import Ticket

class Order:
    """

    Represents a single transaction in the movie ticket booking system.
    Encapsulates a collection of Ticket objects together and records the date and time of the order.

    """
    def __init__(self, local_date_time: datetime) -> None:

        self._tickets: List[Ticket] = []
        self.local_date_time: datetime = local_date_time

    def add_ticket(self, ticket:Ticket) -> None:
        """Add a ticket to the order."""
        self._tickets.append(ticket)
    
    def calculate_total_price(self) -> Decimal:
        """Calculate the total price of all tickets in the order."""
        total = Decimal("0")

        for ticket in self._tickets:
            if hasattr(ticket, 'get_price()'):
                price = ticket.get_price()
            elif hasattr(ticket, 'price'):
                price = ticket.price
            else:
                raise AttributeError(
                    "Ticket must expose price via get_price() or price attribute"
                )
            total += price
        return total
    
    def get_all_tickets(self) -> List[Ticket]:
        """Return all tickets in the order."""
        return list(self._tickets)