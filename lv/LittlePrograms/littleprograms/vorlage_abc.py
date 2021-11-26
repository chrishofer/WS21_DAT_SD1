import abc

# es gibt auch abstractstaticmethod und abstractclassmethod
class Flaeche(abc.ABC):
    @abc.abstractmethod
    def flaeche(self) -> float:
        pass

    def winkewinke(self):
        print("winke winke")


class Rechteck(Flaeche):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def flaeche(self):
        return self.l * self.b

if __name__ == '__main__':
    #f = Flaeche() # geht nicht
    r = Rechteck(10, 2)

