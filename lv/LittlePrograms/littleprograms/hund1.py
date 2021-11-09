class Hund: # Namen werden mit CamelCase großgeschrieben HundMitKatze
    species = "Canis lupus familiaris" # Klassenattribut (oder auch statische Attribut genannt)

    def __init__(self, name : str, age : int):
        self.name = name # Instanzattribut (jedes Objekt/Instanz hat eigene Version davon)
        self.age = age
        # hier koennte beliebig komplexer code stehen der auch andere Objekte erzeugt
        # oder methoden bzw. funktionen aufruft

    def gib_laut(self, text: str):
        print(f'{self.name} bellt ganz laut {text}')


if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14)
    lassie = Hund("Lassie", 12)

    rex.gib_laut("Extrawurstsemmel")

    # Zugriff auf das Klassenattribut
    print(Hund.species)
    print(Hund.__dict__)
    print(rex.age) # Zugriff auf das Instanzattribut age
    print(lassie.age)
    print(lassie.species) # auch auf Klassenattribute Zugriff moeglich ACHTUNG nur lesend
    print(lassie.__dict__) # python schaut im __dict__ der Instanz  nach ob es das kennt
    # sonst schaut es im __dict__ der Klasse weiter
    print(dir(lassie))



    # was passiert wenn wir das ACHTUNG nicht beachten
    # pfui nicht machen
    #lassie.species = "Kaetzchen" # fügt eine neues Instanzattribut hinzu und aendert nicht
    # das Klassenattribut
    #print(lassie.__dict__)
