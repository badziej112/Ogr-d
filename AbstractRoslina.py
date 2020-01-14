from _collections_abc import ABCMeta, abstractmethod

class AbstractRoslina(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, wartosc, symbol):

        self.jakosc = 10
        self.wartosc = wartosc
        self.wartosc_stala = wartosc
        self.symbol = symbol
        self.nawodnienie = False
        self.nawożone = False
