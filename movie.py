class Movie:
    def __init__(self, title, genre, durationInMinutes):
        self.title = title
        self.genre = genre
        self.durationInMinutes = durationInMinutes
    
    def getTitle(self):
        return self.title
    
    def getGenre(self):
        return self.genre
    
    def getDurationInMinutes(self):
        return self.durationInMinutes
    
    def setTitle(self, title):
        self.title = title
    
    def setGenre(self, genre):
        self.genre = genre  
    
    def setDurationInMinutes(self, durationInMinutes):
        self.durationInMinutes = durationInMinutes
    
    def __repr__(self):
        return f"Movie(title={self.title}, genre={self.genre}, durationInMinutes={self.durationInMinutes})"
    
# Example usage:
if __name__ == "__main__":
    movie = Movie("Inception", "Sci-Fi", 148)
    print(movie)
    movie.setDurationInMinutes(150)
    print(f"Updated Duration: {movie.getDurationInMinutes()} minutes")