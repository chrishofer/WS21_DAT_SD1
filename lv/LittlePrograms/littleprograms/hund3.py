class Hund: # Namen werden mit CamelCase großgeschrieben HundMitKatze
    species = "Canis lupus familiaris" # Klassenattribut (oder auch statische Attribut genannt)
    zaehler = 0 # zählen mit wie viele Hundeobjekte es gibt

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    @property
    def last_adventure(self):
        return self.__last_gassi

    def __init__(self, name : str, age : int):
        self.name = name # Instanzattribut (jedes Objekt/Instanz hat eigene Version davon)
        self.age = age
        self.__last_gassi = 24
        self.__loves = "Pedigree" # private soll nur in Hund verwendet werden
        # hier koennte beliebig komplexer code stehen der auch andere Objekte erzeugt
        # oder methoden bzw. funktionen aufruft
        Hund.zaehler += 1

    def __del__(self):
        Hund.zaehler -= 1

    @classmethod
    def get_anzahl_hunde(cls):
        return cls.zaehler   # alternativ wäre auch Hund.zaehler moeglich (bzw. in statischer methode nur so möglich)

    def gib_laut(self, text: str):
        print(f'{self.name} bellt ganz laut {text} und freut sich auf sein/ihr {self.__loves}')

    def __str__(self):
        return f'{self.name} ist ein Hund ist {self.age} Jahre alt'

    def __repr__(self):
        return f'Hund(name={self.name}, age={self.age})'

class Corgi(Hund):
    # es wird standarmaessig nur ein init aufgerufen (spezialitaet von python)
    # wenn wir kein init haetten wuerde das init von den eltern aufgerufen werdne

    def __init__(self, name, age, iq):
        # wir müssen explizit init unserer eltern aufrufen
        super().__init__(name, age) # Hund.__init__(self, name, age) # das wäre die alternative
        self.iq = iq
        self.gib_laut("wuff wuff")
        super().gib_laut("wuff wuff") # um die implementation der basisklasse aufzurfen - dafuer kann ich super() verwenden

    def gib_laut(self, text: str):
        print(f'{self.name} ist sehr intelligent {self.iq} und bellt nicht so laut um uns nicht zu stoeren {text}')


if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14)
    rex2 = rex
    lassie = Hund("Lassie", 12)
    c = Corgi("Cheddar", 15, 120)

    c.gib_laut("wuff wuff")
    c.age = 14

