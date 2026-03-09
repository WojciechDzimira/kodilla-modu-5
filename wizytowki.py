import logging

from faker import Faker
fake = Faker('pl_PL')

class BaseContact:
    """ klasa reprezentująca prywatną wizytówkę """
    def __init__(self, owner_name, owner_surname, owner_e_mail, owner_private_number): #wykasowany **kwargs
        self.name = owner_name
        self.surname = owner_surname
        self.e_mail = owner_e_mail
        self.private_number = owner_private_number
        logging.debug(f"utowrzono wizytowke dla {owner_name} {owner_surname}")

    @property
    def label_length(self):
        """ metoda oblicza sumę znaków w imieniu i nazwisku wraz ze spacją"""
        length = len(self.name) + len(self.surname) + 1
        return length
    def contact(self):
        """metoda wyświetla numer prywatny, imie i nazwisko"""
        print(f"Wybieram numer : {self.private_number} i dzwonie do {self.name} {self.surname}.")
    
class BusinessContact(BaseContact):
    def __init__(self, owner_name, owner_surname, owner_e_mail, owner_private_number, 
                 owner_firm_name, owner_position, owner_business_number):   #wykasowany **kwargs
        super().__init__(
            owner_name=owner_name, 
            owner_surname=owner_surname, 
            owner_e_mail=owner_e_mail, 
            owner_private_number=owner_private_number 
            )
        self.position = owner_position
        self.firm_name = owner_firm_name
        self.business_number = owner_business_number
        logging.debug(f"Rozszerzono wizytówkę o dane firmowe: {self.firm_name}")
    def contact(self):
        """metoda wyświetla numer służbowy, imie i nazwisko"""
        print(f"Wybieram numer : {self.business_number} i dzwonie do {self.name} {self.surname}.")  

def int_input(text):
    """Funkcja prosi uzytkownika o liczbę całkowitą i sprawdza czy 
    uzytkownik faktycznie wprowadził liczbę calkowita"""
    while True:
        try:
            number = int(input(f"{text}"))
            if number > 0:
                return number
            else:
                print("to nie jest dodatnia liczba całkowita, wprowadz jeszcze raz.")
                logging.warning("Użytkownik wprowadził liczbę ujemną")
        except ValueError:
            print("to nie jest liczba całkowita, wprowadz jeszcze raz.")
            logging.warning("Użytkownik wprowadził wartośc nie będącą liczbą")

def card_choosing():
    """"Funkcja wyboru rodzaju wizytówek jakie mają byc wygenerowane"""
    while True:
        operation = int_input("Wpisz 1 lub 2: ")
        if operation  in {1, 2}:
            return operation
        else:
            print("Błąd, wpisz jeszcze raz")  
            logging.warning(f"Użytkownik wprowadził niepoprawną wartość")           

def create_contacts(choice_card, choice_card_number):
    """Funkcja pobiera od uzytkowniak jaki rodzaj wizytowek i jaka ich ilosc chce wygenerowac 
    po czym tworzy je i zapisuje na odpowieniej liście"""
    
    business_contact_list = []
    base_contact_list = []

    if choice_card == 1:
        for i in range(choice_card_number):
            card = BaseContact(
            owner_name = fake.first_name(),
            owner_surname = fake.last_name(),
            owner_e_mail = fake.email(),
            owner_private_number = fake.phone_number()
            )
            base_contact_list.append(card)
            logging.debug(f"Stworzono {i+1}/{choice_card_number} wizytówek prywatnych")
        return base_contact_list
    elif choice_card == 1:
        for i in range(choice_card_number):
            card = BusinessContact(
            owner_name = fake.first_name(),
            owner_surname = fake.last_name(),
            owner_e_mail = fake.email(),
            owner_private_number = fake.phone_number(),
            owner_position = fake.job(),
            owner_firm_name = fake.company(),
            owner_business_number = fake.phone_number()
            )
            business_contact_list.append(card)
            logging.debug(f"Stworzono {i+1}/{choice_card_number} wizytówek firmowych")
        return business_contact_list

if __name__ == "__main__":        
    logging.basicConfig(level=logging.DEBUG)
    

    print("1: stwórz prywatną wizytówkę")
    print("2: stwórz biznesową wizytówkę")
    choice_card = card_choosing()
    list = create_contacts(choice_card, int_input("Ile wizytówek stworzyć? "))
   