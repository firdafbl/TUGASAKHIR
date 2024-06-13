from abc import ABC, abstractmethod #ABC=abstract base class

class Bentuk(ABC):
    @abstractmethod #fungsi class turunan 
    def luas (self): 
        pass

    def keliling(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi=sisi

    def luas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi
    
class Lingkaran(Bentuk):
    def __init__(self, jari):
        self.jari = jari

    def luas(self):
        return 3.14 * (self.jari ** 2)
    
    def keliling(self):
        return 2 * 3.14 * self.jari
    
persegi = Persegi(5)
lingkaran = Lingkaran(7)

print("Luas Persegi: ", persegi.luas())
print("Keliling Persegi: ", persegi.keliling())
print("Luas Lingkaran: ", lingkaran.luas())
print("Keliling Lingkaran: ", lingkaran.keliling())


