

from cinema import Cinema
from movie import Movie
from screening import Screening
from screeningManager import ScreeningManager
from seat import Seat


class MovieBookingSystem:
    
    def __init__(self, _movie: Movie, _cinema: Cinema, _screening_manager: ScreeningManager):
        self._movie = _movie
        self._cinema = _cinema
        self._screening_manager = _screening_manager
    
    def add_movie(self, movie: Movie) -> None:
        pass

    def add_cinema(self, cinema: Cinema) -> None:
        pass

    def add_screening(self, movie: Movie, screening: Screening) -> None:
        pass

    def book_tickets(self, screening: Screening, seats: Seat) -> None:
        pass
    
    def get_available_seats(self, screening: Screening) -> list[Seat]:
        pass

    def get_tickets_for_screening(self, screening: Screening) -> list:
        pass

    def get_tickets_count(self, screening: Screening) -> int:
        pass
