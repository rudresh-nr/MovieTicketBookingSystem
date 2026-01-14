from layout import Layout

class Room:
    def __init__(self, room_number: str, layout: Layout):
        self.room_number = room_number
        self.layout = layout

    def get_room_number(self) -> str:
        return self.room_number
    
    def get_layout(self) -> Layout:
        return self.layout