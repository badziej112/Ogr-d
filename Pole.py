from Obszar import Obszar
from Ziemniak import Ziemniak
from Salata import Salata
from Pomidor import Pomidor
from Truskawka import Truskawka

class Pole:

    def __init__(self, pole, rozmiar):

        self.pole = pole
        self.rozmiar = rozmiar

    @staticmethod
    def wykryj_rosline(pole, Roslina, jakosc, zasob, nawoz_woda, a, ilosczasobu):

        if isinstance(pole, Roslina) is True and ilosczasobu >= zasob:

            if nawoz_woda == True:
                pole.jakosc -= jakosc

            if nawoz_woda == False:
                pole.jakosc += jakosc
                if a == 1:
                    pole.nawodnienie = True
                elif a == 2:
                    pole.nawożone = True
                else:
                    "Coś poszło nie tak!"

            return zasob

        elif isinstance(pole, Roslina) is True and ilosczasobu < zasob:
            print("Nie starczyło zasobów!")
            return 0
        else:
            return 0

    def etap_rozwoju(self, jakosc, symbol, x, y, wzrost):

        if self.pole[x, y].jakosc >= jakosc:
            self.pole[x, y].symbol = self.pole[x, y].symbol[0] + symbol
            self.pole[x, y].wartosc = self.pole[x, y].wartosc_stala * wzrost

    def rysuj(self):

        for x in range(self.rozmiar):
            for y in range(self.rozmiar):
                self.pole[x, y] = Obszar()

    def pokaz(self):

        print("   __1______2______3______4__")
        for x in range(self.rozmiar):
            obszar = []
            i = 0
            for y in range(self.rozmiar):
                obszar.append(self.pole[x, y].symbol)
                i += 1
                if i == self.rozmiar:
                    print(x+1, end=' ')
                    print(obszar)
        print("   ##########################")

    def posadz_rosline(self, x, y, roslina):

        if roslina == 1:
            self.pole[x, y]  =  Ziemniak()
        elif roslina == 2:
            self.pole[x, y] = Salata()
        elif roslina == 3:
            self.pole[x, y] = Pomidor()
        elif roslina == 4:
            self.pole[x, y] = Truskawka()
        else:
            print("Wpisano zły numer rośliny!")

        self.pokaz()

    def wykop_rosline(self, x, y):

        if isinstance(self.pole[x, y], Obszar) is False:
            zarobek = self.pole[x, y].wartosc
            self.pole[x, y] = Obszar()
            return  zarobek
        else:
            print("Na podanym polu nie ma rośliny!")
            return 0

    def ubytek_zasobu(self, pole, nawoz_woda, a, ilosczasobu):

        u = 0

        while u == 0:
            u += self.wykryj_rosline(pole, Ziemniak, a*10, 5, nawoz_woda, a, ilosczasobu)
            u += self.wykryj_rosline(pole, Salata, a*10, 15, nawoz_woda, a, ilosczasobu)
            u += self.wykryj_rosline(pole, Pomidor, a*5, 20, nawoz_woda, a, ilosczasobu)
            u += self.wykryj_rosline(pole, Truskawka, a*5, 30, nawoz_woda, a, ilosczasobu)
            break

        return u, -u

    def podlej_rosline(self, a, b, wybor, nw, ilosc1, ilosc2):

        ubytek = 0
        iloscwody, iloscnawozu = ilosc1, ilosc2
        if wybor == 1:
            for x in range(self.rozmiar):
                for y in range(self.rozmiar):
                    if self.pole[x, y].symbol != "   ":
                        if nw == 1:
                            u, i = self.ubytek_zasobu(self.pole[x, y], self.pole[x, y].nawodnienie, 1, iloscwody)
                            ubytek += u
                            iloscwody += i
                        elif nw == 2:
                            u, i = self.ubytek_zasobu(self.pole[x, y], self.pole[x, y].nawożone, 2, iloscnawozu)
                            ubytek += u
                            iloscnawozu += i

        if wybor == 2:
            if self.pole[a, b].symbol != "   ":
                if nw == 1:
                    u, i = self.ubytek_zasobu(self.pole[x, y], self.pole[x, y].nawodnienie, 1, iloscwody)
                    ubytek += u
                    iloscwody += i
                elif nw == 2:
                    u, i = self.ubytek_zasobu(self.pole[x, y], self.pole[x, y].nawożone, 2, iloscnawozu)
                    ubytek += u
                    iloscnawozu += i

        return ubytek

    def dojrzewanie(self):

        for x in range(self.rozmiar):
            for y in range(self.rozmiar):
                if self.pole[x,y].symbol != "   ":

                    if self.pole[x, y].nawodnienie == False:
                        self.pole[x, y].jakosc -= 15
                    elif self.pole[x, y].nawodnienie == True:
                        self.pole[x,y].jakosc += 10
                        self.pole[x, y].nawodnienie = False

                    if self.pole[x, y].nawożone == True:
                        self.pole[x,y].jakosc += 10
                        self.pole[x, y].nawożone = False

                    self.etap_rozwoju(0, "  ", x, y, 1)
                    self.etap_rozwoju(50, "+ ", x, y, 1.5)
                    self.etap_rozwoju(100, "++", x, y, 2)

                    if self.pole[x,y].jakosc <= 0:
                        self.pole[x,y] = Obszar()
                    if self.pole[x,y].jakosc > 125:
                        self.pole[x,y] = Obszar()

    def sprawdz(self, x, y):

        return self.pole[x, y].jakosc, self.pole[x, y].wartosc, self.pole[x, y].nawodnienie, self.pole[x, y].nawożone








