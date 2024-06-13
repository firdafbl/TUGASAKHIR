#parent class
class Manusia:
    def __init__(self, nama, pekerjaan, usia):
        self.nama = nama
        self.pekerjaan = pekerjaan
        self.usia = usia

    def data(self):
        print("Nama saya adalah: ", self.nama, "saya berusia", self.usia,"th")

    def profesi(self): 
        print("Pekerjaan saya adalah:", self.pekerjaan)

class Tentara(Manusia):
    def tugastentara(self):
        print("Saya bertugas menjaga negara")

class Dokter(Manusia):
    def tugasdokter(self):
        print("Saya bertugas memeriksa orang yang sakit")

class Petani(Manusia):
    def tugaspetani(self):
        print("Saya bertugas menanam, merawat, dan memanen padi")

Ten = Tentara ("Reo","tentara", 55)      
Ten.data()
Ten.profesi()
Ten.tugastentara()

Dok = Dokter ("Ria", "Dokter", 45)      
Dok.data()
Dok.profesi()
Dok.tugasdokter()

Pet = Petani ("Baba", "petani" ,35)      
Pet.data()
Pet.profesi()
Pet.tugaspetani()