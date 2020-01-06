from Obszar import Obszar
from Ziemniak import Ziemniak

class Pole:

    def __init__(self, pole, rozmiar):

        self.pole = pole
        self.rozmiar = rozmiar

    @staticmethod
    def wykryj_rosline(pole, Roslina, jakosc, woda):

        if isinstance(pole, Roslina) is True:

            if pole.nawodnienie == True:
                pole.jakosc -= jakosc

            if pole.nawodnienie == False:
                pole.jakosc += jakosc
                pole.nawodnienie = True

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


    def podlej_rosline(self, a, b, wybor):

        ubytek_wody = 0
        if wybor == 1:
            for x in range(self.rozmiar):
                for y in range(self.rozmiar):
                    if self.pole[x, y].symbol != "   ":
                        ubytek_wody += self.wykryj_rosline(self.pole[x, y], Ziemniak, 5, 5)

        if wybor == 2:
            if self.pole[a, b].symbol != "   ":
                ubytek_wody += self.wykryj_rosline(self.pole[a, b], Ziemniak, 5, 5)

        return ubytek_wody

    def dojrzewanie(self):

        for x in range(self.rozmiar):
            for y in range(self.rozmiar):
                if self.pole[x,y].symbol != "   ":
                    if self.pole[x, y].nawodnienie == False:
                        self.pole[x, y].jakosc -= 15
                    if self.pole[x, y].nawodnienie == True:
                        self.pole[x,y].jakosc += 10
                        self.pole[x, y].nawodnienie = False
                    if self.pole[x,y].jakosc >= 50:
                        self.pole[x,y].symbol = self.pole[x,y].symbol[0] + "+ "
                    if self.pole[x,y].jakosc >= 100:
                        self.pole[x,y].symbol = self.pole[x,y].symbol[0] + "++"
                    if self.pole[x,y].jakosc < 0:
                        self.pole[x,y] = Obszar()
                    if self.pole[x,y].jakosc > 125:
                        self.pole[x,y] = Obszar()



    def sprawdz(self, x, y):

        return self.pole[x, y].jakosc, self.pole[x, y].wartosc, self.pole[x, y].nawodnienie








