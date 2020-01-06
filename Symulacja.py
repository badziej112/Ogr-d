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

        if a == 2:

            print("Twoje rzeczy")
            print("Monety: ", self.monety)
            print("Nawóz: ", self.nawoz)
            print("Woda: ", self.woda)
            print("Nasiona: ", self.nasiona)

        if a == 3:

            print("Które pole chcesz sprawdzić?")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            jakosc, wartosc, nawodnienie = pole.sprawdz(wybor1, wybor2)
            print("Wartość rośliny:", wartosc)
            print("Jakość rośliny:", jakosc)
            if nawodnienie == True:
                print("Roślina jest podlana.")
            if nawodnienie == False:
                print("Roślina jest sucha.")

        if a == 4:

            print("Czy chcesz podlać wszystkie rośliny?")
            print("[1] - Tak")
            print("[2] - Nie")
            wybor = self.wpisz_liczbe()
            if wybor == 1:
                pole = Pole(self.mapa, self.rozmiar)
                self.woda -= pole.podlej_rosline(None, None, 1)
            if wybor == 2:
                print("Podaj współrzędne:")
                wybor1 = self.wspolrzedne() - 1
                wybor2 = self.wspolrzedne() - 1
                pole = Pole(self.mapa, self.rozmiar)
                self.woda -= pole.podlej_rosline(wybor1, wybor2, 2)

        if a == 5:

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

        if a == 0:

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











