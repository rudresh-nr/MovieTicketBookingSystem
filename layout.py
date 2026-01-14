
from seat import Seat
from typing import Optional


class Layout:

    def __init__(self, row: int, column: int, seat_by_number: dict[str, Seat], seat_by_position: dict[str, dict]):
        self.row = row
        self.column = column
        self.seat_by_number = seat_by_number  # dict with key as seat number and value as Seat object
        self.seat_by_position = seat_by_position  # dict with key as row and value as dict of column and Seat object

    def add_seat(self) -> None:
        pass

    def seat_by_number(self) -> Optional[Seat]:
        pass

    def seat_by_position(self) -> Optional[Seat]:
        pass

    def get_all_seats(self) -> list[Seat]:
        pass
        