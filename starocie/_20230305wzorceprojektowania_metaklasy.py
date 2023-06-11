
class MojaMeta(type):
    def __new__(cls, clsname, bases, attrs):
        print(f"Nazwa klasy: {clsname}")
        print(f"Klasy dziedziczone: {bases}")
        print(f"Słownik atrybutów: {attrs}")
        return type.__new__(cls, clsname, bases, attrs)

class Regular:
    pass

r=Regular()

class After(Regular, metaclass=MojaMeta):
    @property
    def info(self):
        return "informacja"

class Next(After):
    pass