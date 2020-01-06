from _collections_abc import ABCMeta, abstractmethod

class AbstractRoslina(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, jakosc, wartosc, symbol):

        self.jakosc = jakosc
        self.wartosc = wartosc
        self.symbol = symbol
        self.nawodnienie = False
