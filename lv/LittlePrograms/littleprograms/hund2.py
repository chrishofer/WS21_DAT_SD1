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

if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14)
    rex2 = rex
    lassie = Hund("Lassie", 12)

    print(Hund.zaehler)
    rex.gib_laut("Extrawurstsemmel")
    # Hund.gib_laut(rex, "Extrawurstsemmel") # das macht python aus zeile davor

    print(lassie.__str__())
    print(lassie.__repr__())
    # was passiert?
    print(lassie) # print verwendet __str__ falls vorhanden, sonst __repr__

    for element in [rex, lassie]:
        print(element)

    print([rex, lassie])

    # wir koennen dezidiert elemente aus collections oder objekte selbst loeschen
    del rex

    print(Hund.zaehler)
    print(Hund.get_anzahl_hunde())
    print(lassie.get_anzahl_hunde())

    # Hund alter verändern geht
    lassie.age = 3
    print(lassie.age)
    lassie.__loves = "Caesar"
    print(lassie.__loves)
    lassie.gib_laut("hunger")
    print(dir(lassie))
    # technisch ist es möglich, aber gesellschaftlich geächtet! (bitte nicht machen)
    lassie._Hund__loves = "Sheba" # das ist fuer katzen achtung!
    lassie.gib_laut("noch mal hungrig")

    print(lassie.age)

    print(lassie.last_adventure)
    lassie.last_adventure = 12
    # Exkurs
    #print(susie.get_note())
    #susie.set_note(2)

    #print(susie.note)
    #susie.note = 2