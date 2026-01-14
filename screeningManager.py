
from movie import Movie
from screening import Screening
from seat import Seat
from ticket import Ticket
from typing import List

class ScreeningManager:

    def __init__(self, _screening_by_movie: dict[Movie, list[Screening]], 
                 _tickets_by_screening: dict[Screening, list[Ticket]]):
        
        self._screening_by_movie = _screening_by_movie  # dict with key as Movie object and value as list of Screening objects
        self._tickets_by_screening = _tickets_by_screening  # dict with key as Screening object and value as list of Ticket objects    

    def add_screening(self, movie:Movie, screening: Screening) -> None:
        if movie not in self._screening_by_movie:
            self._screening_by_movie[movie] = []
        else:
            self._screening_by_movie[movie].append(screening)

    def add_ticket(self, screening: Screening, ticket: Ticket) -> None:
        self._tickets_by_screening.setdefault(screening, []).append[ticket]

    def get_screening_for_movie(self, movie:Movie)-> list[Screening]:
        return list(self._screening_by_movie.get(movie, []))

    def get_ticekts_for_screening(self, screening: Screening) -> List[Ticket]:
        return list(self._tickets_by_screening.get(screening, []))

    def get_available_seats(self, screening: Screening) -> List[Seat]:
        