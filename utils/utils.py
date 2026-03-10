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
