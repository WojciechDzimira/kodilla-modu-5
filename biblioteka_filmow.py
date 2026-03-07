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
        self.views_number += 1

  
    
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
        self.views_number += 1
    

def get_movies():
    """funkcja filtruje listę i zwraca tylko filmy"""
    return
def get_series():
    """funkcja filtruje liste i zwraca tylko seriale"""
    return
def generate_views():
    """wynkcja wybiera element z biblioteki i dodaje mu losowe wyświetlenia w zakresie od 1 do 100"""
    return
def use_generate_views():
    """funkcja uruchamia funkcje generate_views() 10 razy"""
    return

def top_titles():
    """funkcja wyświetla wybraną ilość najpopularniejszych tytułów w bibliotece"""
    return
def add_serial_season():
    """funkcja dodaje do biblioteki cały sezon serialu po dostarczeniu do niej tytułu, rok wydania 
    gatunku, numer sezonu, liczba odcinków do dodania"""
    return
def episode_number():
    """funkcja wyświetla liczbę dostępnych odcinków serialu"""


if __name__ == "__main__":        
    logging.basicConfig(level=logging.DEBUG)
    
    
