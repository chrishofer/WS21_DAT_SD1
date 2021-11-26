
class Motor:

    __zaehler = 1

    @property
    def umdrehungen_pro_minute(self):
        return self.__umdrehungen_pro_minute
    
    @property
    def geschwindigkeit(self):
        return self.__geschwindigkeit
    
    @geschwindigkeit.setter
    def geschwindigkeit(self, value):
        if value >= 200:
            self.__geschwindigkeit = 200
        else:
            self.__geschwindigkeit = value

    def __meine_hilfsmethode_fuer_internen_gebrauch(self):
        print("easter egg")

    def __init__(self):
        super().__init__()
        # jeder soll geschwindigkeit aendern koennen
        # deshalb mach ich das public (quasi muss nix tun)
        # jetzt möchte ich zugriff schreibend steuern
        # deshalb props get/set property
        # mir steht es frei ob ich mit oder ohne __ drauf zugreife
        # es unterscheidet sich dadurch, dass ohne __-Zugriff über
        # die setter Methode zugegriffen wird (und diese Logik ausgeführt wird)
        self.geschwindigkeit = 0

        #self.maNr = Motor.__zaehler

        # das war früher public aber es soll niemand mehr von außen verändern können
        # sondern nur lesen darauf zugreifne können -> private mit get property
        # immer wenn ich ein get property habe (nur lesen) - dann muss ich in der eigenen klasse
        # in allen methoden immer direkt aufs private attribut zugreifen (wenn ich zuweisen möchte)
        self.__umdrehungen_pro_minute = 0

        # einspritzmenge ist nur für internen gebrauch - private
        # kein anderer teil des autos muss das so genau wissen
        self.__einspritz_menge = 0

        # protected heißt es ist nur für die klasse selbst relevant und
        # für etwaige klassen die davon ableiten (zb elektromotor)
        self._motor_modus = "eco"



    def __repr__(self):
        return f'Motor bewegt Fahrzeug mit {self.geschwindigkeit} km/h und {self.umdrehungen_pro_minute} Umdrehungen'


class Motorhalle:
    def __init__(self, groesse_in_m2 : int):
        self.groesse = groesse_in_m2
        self.meine_motoren = []
        self.anzahl_motoren = 0

    def add_motor(self, m: Motor):
        self.meine_motoren.append(m)
        self.anzahl_motoren += 1


if __name__ == '__main__':
    m1 = Motor()
    m1.geschwindigkeit = 333
    #m1.umdrehungen_pro_minute = 200
    print(m1.umdrehungen_pro_minute)
    print(m1)

    halle = Motorhalle(100)
    halle.meine_motoren.append(m1)
    halle.add_motor(m1)
