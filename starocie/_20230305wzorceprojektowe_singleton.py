class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Regular():
    pass

r1=Regular()
r2=Regular()
print(r1==r2)
print(r1)
print(r2)

class SngClass(metaclass=Singleton):
    pass

sc1 = SngClass()
sc2 = SngClass()

print(sc1==sc2)
print(sc1)
print(sc2)