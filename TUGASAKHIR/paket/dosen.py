class Dosen:
    def __init__(self, nama):
        self.nama = nama

    def mengajar(self):
        print("Mengajar")

class PemrogramanLanjut(Dosen):
    def mengajar(self):
        return("Mengajar Pemrograman Lanjut")

class PendidikanPancasila(Dosen):
    def mengajar(self):
        return("Mengajar Pendidikan Pancasila")

class SistemBasis(Dosen):
    def mengajar(self):
        return("Mengajar Sistem Basis Data")

dosen1 = PemrogramanLanjut("Pak Amak")
dosen2 = PendidikanPancasila("Pak Didik")
dosen3 = SistemBasis("Pak Heri")

for dosen in (dosen1, dosen2, dosen3):
    print(f'{dosen.nama} {dosen.mengajar()}')
