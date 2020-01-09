from Pole import Pole
import csv

class Symulacja:

    def __init__(self, rozmiar):

        self.rozmiar = rozmiar
        self.cykl = 0
        self.nasiona = 10
        self.woda = 100
        self.nawoz = 100
        self.monety = 20
        self.mapa = {}

    @staticmethod
    def wpisz_liczbe():

        a = False
        while a == False:
            x = input()
            try:
                b = int(x)
                a = True
            except ValueError:
                print("Podaj cyfrę!")

        return b

    def zakupy(self, koszt_sztuki):

        print("Podaj ile chcesz kupić: ")
        zakup = self.wpisz_liczbe()
        if self.monety >= koszt_sztuki*zakup:
            self.monety -= koszt_sztuki*zakup
            return zakup
        else:
            print("Nie masz tyle pieniędzy!")
            return 0

    def podlewanie_nawożenie(self, środek, słowo, nw):

        print("Czy chcesz", słowo,"wszystkie rośliny?")
        print("[1] - Tak")
        print("[2] - Nie")
        wybor = self.wpisz_liczbe()
        if wybor == 1:
            pole = Pole(self.mapa, self.rozmiar)
            środek -= pole.podlej_rosline(None, None, 1, nw)
        if wybor == 2:
            print("Podaj współrzędne:")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            środek -= pole.podlej_rosline(wybor1, wybor2, 2, nw)

    def wspolrzedne(self):

        x = self.wpisz_liczbe()
        while x > self.rozmiar or x < 1:
            print("Wpisz poprawną liczbę!")
            x = self.wpisz_liczbe()

        return x

    def start(self):

        try:
            with open("ogrod_save.txt", mode='r') as load_file:
                load_gra = csv.reader(load_file, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
                lista = []
                for x in load_gra:
                    lista.append(x)

        except FileNotFoundError:
            pass

        pole = Pole(self.mapa, self.rozmiar)
        pole.rysuj()
        pole.pokaz()
        self.mapa = pole.pole
        print("")

    def dzialania(self, a):

        if a == 1:

            print("Na jakich współrzędnych chcesz sadzić?")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            pole.posadz_rosline(wybor1, wybor2)
            self.nasiona -=1
            self.cykl += 1

        elif a == 2:

            print("Twoje rzeczy:")
            print("Monety: ", self.monety)
            print("Nawóz: ", self.nawoz)
            print("Woda: ", self.woda)
            print("Nasiona: ", self.nasiona)

        elif a == 3:

            print("Które pole chcesz sprawdzić?")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            jakosc, wartosc, nawodnienie, nawożenie = pole.sprawdz(wybor1, wybor2)
            print("Wartość rośliny:", wartosc)
            print("Jakość rośliny:", jakosc)
            if nawodnienie == True:
                print("Roślina jest podlana.")
            elif nawodnienie == False:
                print("Roślina jest sucha.")
            if nawożenie == True:
                print("Roślina była nawożona.")
            elif nawożenie == False:
                print("Roślina nie była nawożona.")

        elif a == 4:

            print("[1] - Nawożenie.")
            print("[2] - Podlewanie.")
            wybor = self.wpisz_liczbe()
            if wybor == 1:
                self.podlewanie_nawożenie(self.nawoz, "nawieźć", 2)
            elif wybor == 2:
                self.podlewanie_nawożenie(self.woda, "podlać", 1)
            else:
                "Wybrano niepoprawną opcję!"

        elif a == 5:

            print("Co chcesz kupić?")
            print("[1] - Nasiona.")
            print("[2] - Wodę.")
            print("[3] - Nawóz.")
            wybor = self.wpisz_liczbe()
            if wybor == 1:
                self.nasiona += self.zakupy(10)
            if wybor == 2:
                self.woda += self.zakupy(1)
            if wybor == 3:
                self.nawoz += self.zakupy(5)

        elif a == 6:

            print("Podaj współrzędne rośliny do wykopania.")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            self.monety += pole.wykop_rosline(wybor1, wybor2)
            pole.pokaz()

        elif a == 0:

            print("Koniec tury.")
            pole = Pole(self.mapa, self.rozmiar)
            pole.dojrzewanie()
            pole.pokaz()
            self.cykl += 1

            with open("ogrod_save.txt", mode='w') as save_file:
                save_gra = csv.writer(save_file, delimiter=',', quotechar='"',quoting =  csv.QUOTE_MINIMAL)

                save_gra.writerow([
                    self.rozmiar,
                    self.cykl,
                    self.nasiona, self.nawoz, self.woda, self.monety,
                    self.mapa
                ])

        else:

            print("Wpisz poprawny punkt!")











