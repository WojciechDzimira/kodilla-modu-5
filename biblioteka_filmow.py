import logging
import random
from faker import Faker
fake = Faker('pl_PL')
from datetime import datetime
logging.basicConfig(level=logging.DEBUG)


class Title:
    """klasa reprezentująca rekord biblioteki"""
    def __init__(self, title, year, genre, views_number):
        self.title = title
        self.year = year
        self.genre = genre
        self.views_number = views_number
class Film(Title):
    """ klasa reprezentująca filmy, dziedzicząca po klasie Title """
    def __init__(self, title, year, genre, views_number):
        super().__init__(
            title = title, 
            year = year, 
            genre = genre,
            views_number = views_number)
        logging.debug(f"Do biblioteki dodano film {title} {year}")
    def play(self):
        """metoda wyświetla tytuł i rok wydania filmu oraz dodaje 1 do odtworzeń"""
        print(f"{self.title} {self.year}.")
        self.views_number += 1

class Serial(Title):
    """ klasa reprezentująca seriale, dziedzicząca po klasie Title """
    def __init__(self, title, year, genre, views_number, episode_number, season_number):
        super().__init__(
            title = title, 
            year = year, 
            genre = genre,
            views_number = views_number
        )
        self.episode_number = episode_number
        self.season_number = season_number
        logging.debug(f"Rozszerzono bibliotekę o serial: {title}, sezon:{self.season_number:02d}, odcinek: {self.episode_number:02d}")
    def play(self):
        """metoda wyświetla tytuł numer sezonu i nr odcinka oraz dodaje 1 do odtworzeń"""
        print(f"{self.title} S{self.season_number:02d} E{self.episode_number:02d}.")
        self.views_number += 1
    
def int_input(text):
    """Funkcja prosi uzytkownika o liczbę całkowitą i sprawdza czy 
    uzytkownik faktycznie wprowadził liczbę calkowita"""
    while True:
        try:
            number = int(input(f"{text}"))
            if number > -1:
                return number
            else:
                print("to nie jest dodatnia liczba całkowita, wprowadz jeszcze raz.")
                logging.warning("Użytkownik wprowadził liczbę ujemną")
        except ValueError:
            print("to nie jest liczba całkowita, wprowadz jeszcze raz.")
            logging.warning("Użytkownik wprowadził wartośc nie będącą liczbą")

def choose_content_type():
    """"Funkcja wyboru rodzaju wyświetlanych najpopularniejszych tytułów z biblioteki"""
    print("1: Najpopularniejsze Filmy \n2: Najpopularniejsze Seriale \n3: Najpopularniejsze Ogólnie")
    while True:
        choice = int_input("Wpisz 1, 2 lub 3: ")
        if choice  in {1, 2, 3}:
            return choice
        else:
            print("Błąd, wpisz jeszcze raz")  
            logging.warning("Użytkownik wprowadził niepoprawną wartość")  
    

def get_movies():
    """funkcja filtruje listę i zwraca tylko filmy"""
    film_list = []
    for record in library_list:
        if type(record) == Film:
            film_list.append(record)
    return sorted(film_list, key=lambda x: x.title)
    
def get_series():
    """funkcja filtruje liste i zwraca tylko seriale"""
    serial_list = []
    for record in library_list:
        if type(record) == Serial:
            serial_list.append(record)
    return sorted(serial_list, key=lambda x: x.title)
    
def generate_views():
    """funkcja wybiera element z biblioteki i dodaje mu losowe wyświetlenia w zakresie od 1 do 100"""
    record = random.randrange(len(library_list))
    library_list[record].views_number += random.randint(1, 100)

def use_generate_views():
    """funkcja uruchamia funkcje generate_views() 10 razy"""
    for _ in range(10):
        generate_views()

def top_titles(content_type):
    """funkcja wyświetla wybraną ilość najpopularniejszych tytułów w bibliotece"""
    top_views_list = []
    top_views_list = sorted(library_list, key=lambda x: x.views_number, reverse=True)
    top_views = int_input("Jaką liczbę najpopularniejszych tytułów wyświetlić? Podaj liczbę całkowotą większą od 0: ")

    if content_type == 1:  
        filtered = []
        for record in top_views_list:
            if type(record) == Film:
                filtered.append(record)
        return filtered[:top_views]
    
    
    elif content_type == 2:  
        filtered = []
        for record in top_views_list:
            if type(record) == Serial:
                filtered.append(record)
        return filtered[:top_views]
    
    elif content_type == 3:  
        return top_views_list[:top_views]
                   
def episode_number(serial_title):
    """funkcja wyświetla liczbę dostępnych odcinków serialu"""
    filtered = []
    for record in library_list:
        if record.title == serial_title:
            filtered.append(record)
    return len(filtered)

def add_serial_season(title, year, genre, views_number, season_number):
    """Funkcja dodaje cały sezon serialu"""
    
    for episode in range(1, 16):
        serial = Serial(
            title = title, 
            year = year,
            genre = genre,
            views_number = views_number,
            season_number = season_number,
            episode_number = episode
             )
        library_list.append(serial)
    

def populate_library():
    """funkcja wypełnia biblioteke losowymi danymi filmów i seriali używając faker"""

    genre_list = ["dramaty", "komedia", "tragedia", "fantasy", "horror", "przygodowy", "Sci-fi", "akcja"]
    print("UZUPEŁNIANIE BIBLIOTEKI LOSOWYMI FILMAMI/SERIALAMI")
    number_of_films = int_input("Podaj ile losowych filmów chcesz mieć w bibliotece? Wpisz liczbę całkowitą lub 0: ")
    number_of_serials = int_input("Podaj ile losowych seriali ma znaleźć się w bibliotece: kazdy bedzie miał 3 sezony po 15 odcinków. Wpisz liczbę całkowitą lub 0: ")

    if number_of_films > 0:
        for i in range(number_of_films):
            film = Film(
            title = fake.catch_phrase(),
            year = fake.year(),
            genre = fake.random_element(genre_list), 
            views_number = 0
            )
            library_list.append(film)
    
    if number_of_serials > 0:
        for i in range(number_of_serials):
            title = fake.catch_phrase()
            year = fake.year()
            genre = fake.random_element(genre_list) 
            views_number = 0
            for season in range(1, 4):
                add_serial_season(title, year, genre, views_number, season)


    return library_list

def search(text):
    """funkcja wyszukuje film lub serial po jego tytule"""
    text = text.lower()
    for record in library_list:
        if text == record.title.lower():
            return record
           
    print("Brak wyszukiwanego tytułu w bibliotece")
    logging.warning("Użytkownik próbował wyszukać tytuł którego nie ma w bibliotece")
    return None
    
        
        
            
if __name__ == "__main__":  
    today_datetime = datetime.now().strftime("%d.%m.%Y")
    library_list = []

    top = []     
    print("Biblioteka filmów")
    library_list = populate_library()
    use_generate_views()
    print(f"Najpopularniejsze filmy i seriale dnia {today_datetime}: ")
    top = top_titles(choose_content_type())
    for i, record in enumerate (top, start=1):
        if type(record) == Film:
            print(f"nr{i}: {record.title}, liczba wyświetleń {record.views_number}")
        else:
            print(f"nr{i}: {record.title}, S{record.season_number:02d}E{record.episode_number:02d} liczba wyświetleń {record.views_number}")
