from Obszar import Obszar
from Ziemniak import Ziemniak

class Pole:

    def __init__(self, pole, rozmiar):

        self.pole = pole
        self.rozmiar = rozmiar

    @staticmethod
    def wykryj_rosline(pole, Roslina, jakosc, woda, nawoz_woda):

        if isinstance(pole, Roslina) is True:

            if nawoz_woda == True:
                pole.jakosc -= jakosc

            if nawoz_woda == False:
                pole.jakosc += jakosc
                if nawoz_woda == pole.nawożone:
                    pole.nawożone = True
                elif nawoz_woda == pole.nawodnienie:
                    pole.nawodnienie = True
                else:
                    "Coś poszło nie tak!"

            return woda

        else:

            return 0

    def rysuj(self):

        for x in range(self.rozmiar):
            for y in range(self.rozmiar):
                self.pole[x, y] = Obszar()

    def pokaz(self):

        for x in range(self.rozmiar):
            obszar = []
            i = 0
            for y in range(self.rozmiar):
                obszar.append(self.pole[x, y].symbol)
                i += 1
                if i == self.rozmiar:
                    print(obszar)

    def posadz_rosline(self, x, y):

        self.pole[x, y]  =  Ziemniak()
        self.pokaz()

    def wykop_rosline(self, x, y):

        if isinstance(self.pole[x, y], Obszar) is False:
            zarobek = self.pole[x, y].wartosc
            self.pole[x, y] = Obszar()
            return  zarobek
        else:
            print("Na podanym polu nie ma rośliny!")
            return 0

    def podlej_rosline(self, a, b, wybor, nw):

        ubytek = 0
        if wybor == 1:
            for x in range(self.rozmiar):
                for y in range(self.rozmiar):
                    if self.pole[x, y].symbol != "   ":
                        if nw == 1:
                            ubytek += self.wykryj_rosline(self.pole[x, y], Ziemniak, 5, 5, self.pole[x, y].nawodnienie)
                        elif nw == 2:
                            ubytek += self.wykryj_rosline(self.pole[x, y], Ziemniak, 10, 5, self.pole[x, y].nawożone)

        if wybor == 2:
            if self.pole[a, b].symbol != "   ":
                if nw == 1:
                    ubytek += self.wykryj_rosline(self.pole[x, y], Ziemniak, 5, 5, self.pole[x, y].nawodnienie)
                elif nw == 2:
                    ubytek += self.wykryj_rosline(self.pole[x, y], Ziemniak, 10, 5, self.pole[x, y].nawożone)

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

                    if self.pole[x, y].jakosc >= 100:
                        self.pole[x, y].symbol = self.pole[x, y].symbol[0] + "++"
                        self.pole[x, y].wartosc = self.pole[x, y].wartosc_stala * 2

                    elif self.pole[x,y].jakosc >= 50:
                        self.pole[x,y].symbol = self.pole[x,y].symbol[0] + "+ "
                        self.pole[x,y].wartosc = self.pole[x,y].wartosc_stala * 1.5

                    else:
                        self.pole[x,y].symbol = self.pole[x,y].symbol[0] + "  "
                        self.pole[x,y].wartosc = self.pole[x,y].wartosc_stala

                    if self.pole[x,y].jakosc < 0:
                        self.pole[x,y] = Obszar()
                    elif self.pole[x,y].jakosc > 125:
                        self.pole[x,y] = Obszar()

    def sprawdz(self, x, y):

        return self.pole[x, y].jakosc, self.pole[x, y].wartosc, self.pole[x, y].nawodnienie, self.pole[x, y].nawożone








