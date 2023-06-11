
odp = input("Czy Ziemia jest płaska? Czy chcesz znać odpowiedź? (t/n)\n")

if odp.lower() == "t":
    required = True;
else:
    required = False;

def odpowiedz(self):
    return "Tak, Ziemia jest płaska."

def nowaOdpowiedz(self):
    return "Nie, Ziemia jest elipsoidą."

def brak(self):
    return "Brak odpowiedzi - lepiej nie mówić."

class SednoOdpowiedzi(type):
    def __init__(cls, clsname, bases, atrdict):
        #print(f'{atrdict}')
        if required:
            if atrdict.get('cn'):
                cls.odpowiedz = nowaOdpowiedz;
            else:
                cls.odpowiedz = odpowiedz;
        else:
            cls.odpowiedz = brak;

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    cn = True

fil1 = Arystoteles()
print(f"Filozof {fil1.__class__.__name__} mówi: {fil1.odpowiedz()}")

fil2 = Platon()
print(f"Filozof {fil2.__class__.__name__} mówi: {fil2.odpowiedz()}")

fil3 = SwTomasz()
print(f"Filozof {fil3.__class__.__name__} mówi: {fil3.odpowiedz()}")

fil4 = Kopernik()
print(f"Filozof {fil4.__class__.__name__} mówi: {fil4.odpowiedz()}")