#parent class
class Kendaraan:
    def __init__(self, nama, warna, harga):
        self.nama = nama
        self.warna = warna
        self.harga = harga

    def tampilkan(self):
        print("Rincian: ", self.nama, self.warna, self.harga)

    def kecepatanmaxpertama(self):
        print("kecepatan maximum kendaraan: ", self.nama, "adalah 150km/ jam")

    def gantigearpertama(self): 
        print("Gantigear maximum kendaraan adalah sampai 6")

#children class
class Mobil(Kendaraan):
    def kecepatanmaxkedua(self):
        print("Kecepatan maximum kendaraan: ", self.nama, "adalah 200km/ jam")

    def gantigearkedua(self):
        print("Gantigear maximum kendaraan adalah sampai 7")

#memanggil fungsi dari parent class kendaraan
Avanza = Mobil("Avanza", "Putih", 20000000)      
Avanza.tampilkan()
Avanza.kecepatanmaxpertama()
Avanza.gantigearpertama()

#memanggil fungsi dari parent class kendaraan dan children class mobil
Jeep = Mobil("Jeep", "Coklat", 30000000)
Jeep.tampilkan()
Jeep.kecepatanmaxkedua()
Jeep.gantigearkedua()