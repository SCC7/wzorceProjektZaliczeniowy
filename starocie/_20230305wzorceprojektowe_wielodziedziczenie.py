class MultiBases(type):
    def __new__(cls, clsname, bases, atrs):
        if len(bases)>1:
            raise TypeError("Nie można wielodziedziczyć")
        return super().__new__(cls, clsname, bases, atrs)

class Reg():
    pass

class Base(metaclass=MultiBases):
    pass;

class Next(Reg, Base):
    pass