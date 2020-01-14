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
    def jeżeli(dane, warunek, zdanie):

        if dane == warunek:
            return zdanie

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

    def podlewanie_nawożenie(self, słowo, nw):

        print("Czy chcesz", słowo,"wszystkie rośliny?")
        print("[1] - Tak")
        print("[2] - Nie")
        wybor = self.wpisz_liczbe()
        if wybor == 1:
            pole = Pole(self.mapa, self.rozmiar)
            return pole.podlej_rosline(None, None, 1, nw, self.woda, self.nawoz)
        if wybor == 2:
            print("Podaj współrzędne:")
            wybor1 = self.wspolrzedne() - 1
            wybor2 = self.wspolrzedne() - 1
            pole = Pole(self.mapa, self.rozmiar)
            return pole.podlej_rosline(wybor1, wybor2, 2, nw, self.woda, self.nawoz)

    def wspolrzedne(self):

        x = self.wpisz_liczbe()
        while x > self.rozmiar or x < 1:
            print("Wpisz poprawną liczbę!")
            x = self.wpisz_liczbe()

        return x

    def start(self):

        pole = Pole(self.mapa, self.rozmiar)
        pole.rysuj()
        pole.pokaz()
        self.mapa = pole.pole
        print("")

    def dzialania(self, a):

        if a == 1:

            if self.nasiona <= 0:
                print("Nie masz nasion!")
            else:
                print("Co chcesz posadzić?")
                print("[1] - Ziemniak.")
                print("[2] - Sałata.")
                print("[3] - Pomidor.")
                print("[4] - Truskawka.")
                wybierz = self.wpisz_liczbe()
                print("Na jakich współrzędnych chcesz sadzić?")
                print("x =", end=' ')
                wybor1 = self.wspolrzedne() - 1
                print("y =", end=' ')
                wybor2 = self.wspolrzedne() - 1
                pole = Pole(self.mapa, self.rozmiar)
                pole.posadz_rosline(wybor1, wybor2, wybierz)
                self.nasiona -=1

        elif a == 2:

            print("Twoje rzeczy:")
            print("Monety: ", self.monety)
            print("Nawóz: ", self.nawoz)
            print("Woda: ", self.woda)
            print("Nasiona: ", self.nasiona)

        elif a == 3:

            print("Które pole chcesz sprawdzić?")
            print("x =", end=' ')
            wybor1 = self.wspolrzedne() - 1
            print("y =", end=' ')
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

            print("[1] - Podlewanie.")
            print("[2] - Nawożenie.")

            wybor_czynnosci = self.wpisz_liczbe()
            if wybor_czynnosci == 1:
                print("Podlewanie")
                self.woda -= self.podlewanie_nawożenie("podlać", 1)
            elif wybor_czynnosci == 2:
                print("Nawożenie")
                self.nawoz -= self.podlewanie_nawożenie("nawieźć", 2)
            else:
                "Wybrano niepoprawną opcję!"

        elif a == 5:

            print("Co chcesz kupić?")
            print("[1] - Nasiona. 10zł/szt.")
            print("[2] - Wodę 1zł/szt.")
            print("[3] - Nawóz. 5zł/szt.")
            wybor_kupna = self.wpisz_liczbe()
            if wybor_kupna == 1:
                self.nasiona += self.zakupy(10)
            if wybor_kupna == 2:
                self.woda += self.zakupy(1)
            if wybor_kupna == 3:
                self.nawoz += self.zakupy(5)

        elif a == 6:

            print("Podaj współrzędne rośliny do wykopania.")
            print("x =", end=' ')
            wybor1 = self.wspolrzedne() - 1
            print("y =", end=' ')
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

            with open("ekwipunek.txt", mode='w') as save_file2:
                zapisz_ilosc = csv.writer(save_file2, delimiter=' ')
                zapisz_ilosc.writerow([self.rozmiar])
                zapisz_ilosc.writerow([self.cykl])
                zapisz_ilosc.writerow([self.nasiona])
                zapisz_ilosc.writerow([self.woda])
                zapisz_ilosc.writerow([self.nawoz])
                zapisz_ilosc.writerow([self.monety])


            with open("ogrod_save.txt", mode='w') as save_file:
                zapisz_mape = csv.writer(save_file, delimiter=',', quotechar='"',quoting =  csv.QUOTE_MINIMAL)

                for x in range(self.rozmiar):
                    for y in range(self.rozmiar):
                        zapisz_mape.writerow([pole.pole[x, y]])

        else:

            print("Wpisz poprawny punkt!")











