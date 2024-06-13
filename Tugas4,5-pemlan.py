from abc import ABC, abstractmethod

class Mobil(ABC):
    def fasilitas(self):
        pass
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass

class BMW(Mobil):
    def fasilitas(self):
        return "Mesin V8 Berperforma Tinggi"
    def kecepatan(self):
        return 305 
    def harga(self):
        return "900 jutaan"
    def kekuatan(self):
        return 255
    
class Avanza(Mobil):
    def fasilitas(self):
        return "Sistem Audio 6 Speaker"
    def kecepatan(self):
        return 180
    def harga(self):
        return "200 jutaan"
    def kekuatan(self):
        return 91 

class Ferrari(Mobil):
    def fasilitas(self):
        return "Cockpit yang Berfokus pada Pengemudi"
    def kecepatan(self):
        return 330 
    def harga(self):
        return "15 Milyar"
    def kekuatan(self):
        return 663    
 
def mobil_info(mobil: Mobil):
    print(f"Fasilitas Mobil: {mobil.fasilitas()}")
    print(f"Kecepatan Mobil: " + str(mobil.kecepatan()) + " km/jam")
    print(f"Harga Mobil: {mobil.harga()}")
    print(f"Kekuatan Mobil: " + str(mobil.kekuatan()) + " hp")
    

bmw = BMW();
avanza = Avanza();
ferrari = Ferrari();

mobil_info(bmw);
mobil_info(avanza);
mobil_info(ferrari);


    

