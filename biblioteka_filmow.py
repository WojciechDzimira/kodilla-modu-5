import logging
from faker import Faker
fake = Faker('pl_PL')

class Film:
    """ klasa reprezentująca filmy """
    def __init__(self, title, production_year, genre, views_number, **kwargs):
        self.title = title
        self.year = production_year
        self.genre = genre
        self.views_number = views_number
        logging.debug(f"Do biblioteki dodano film {title} {production_year}")
    def play(self):
        """metoda wyświetla tytuł i rok wydania filmu"""
        print(f"{self.title} {self.year}.")
        self.views_number

  
    
class Serial(Film):
    def __init__(self, title, production_year, genre, views_number, episode_number, season_number, **kwargs):
        super().__init__(
            title = title, 
            production_year = production_year, 
            genre = genre, 
            views_number = views_number, 
            **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
        logging.debug(f"Rozszerzono bibliotekę o serial: {title}, sezon:{self.season_number:02}, odcinek: {self.episode_number:02}")
    def play(self):
        """metoda wyświetla tytuł numer sezonu i nr odcinka"""
        print(f"{self.title} S{self.season_number:02}E{self.episode_number:02}.")
  
  


if __name__ == "__main__":        
    logging.basicConfig(level=logging.DEBUG)
    
    
