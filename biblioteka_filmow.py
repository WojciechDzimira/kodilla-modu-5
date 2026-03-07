import logging
from faker import Faker
fake = Faker('pl_PL')

class Film:
    """ klasa reprezentująca filmy """
    def __init__(self, film_title, film_year, film_genre, film_play_number, **kwargs):
        self.title = film_title
        self.year = film_year
        self.genre = film_genre
        self.play_number = film_play_number
        logging.debug(f"Do biblioteki dodano film {film_title} {film_year}")
    def play(self):
        """metoda wyświetla tytuł i rok wydania filmu"""
        print(f"{self.title} {self.year}.")
  
    
class Serial(Film):
    def __init__(self, film_title, film_year, film_genre, film_play_number, serial_episode_number, serial_season_number, **kwargs):
        super().__init__(
            film_title = film_title, 
            film_year = film_year, 
            film_genre = film_genre, 
            film_play_number = film_play_number, 
            **kwargs)
        self.episode_number = serial_episode_number
        self.season_number = serial_season_number
        logging.debug(f"Rozszerzono bibliotekę o serial: {film_title}, sezon:{self.season_number}, odcinek: {self.episode_number}")
    def play(self):
        """metoda wyświetla tytuł numer sezonu i nr odcinka"""
        print(f"{self.title} S{self.season_number:02}E{self.episode_number:02}.")
  
  


if __name__ == "__main__":        
    logging.basicConfig(level=logging.DEBUG)
    
    
