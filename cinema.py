from room import Room
from typing import List

class Cinema:

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.room: List[Room] = []

    def add_room(self, room: Room) -> None:
        self.room.append(room)