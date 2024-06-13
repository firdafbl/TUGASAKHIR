from abc import ABC, abstractmethod

class Universitas(ABC):
    @abstractmethod
    def jumlah_mahasiswa(self):
        pass

    @abstractmethod
    def jumlah_fakultas(self):
        pass

class Unikama(Universitas):
    def __init__(self, nama, jumlah_mahasiswa, jumlah_fakultas):
        self.nama = nama
        self.jumlah_mahasiswa_unikama = jumlah_mahasiswa
        self.jumlah_fakultas_unikama = jumlah_fakultas

    def jumlah_mahasiswa(self):
        return self.jumlah_mahasiswa_unikama

    def jumlah_fakultas(self):
        return self.jumlah_fakultas_unikama

universitas_pgri = Unikama("Universitas PGRI Kanjuruhan Malang", 10000, 6)

print("Nama Universitas        :", universitas_pgri.nama)
print("Jumlah Mahasiswa        :", universitas_pgri.jumlah_mahasiswa(), "Mahasiswa")
print("Jumlah Fakultas         :", universitas_pgri.jumlah_fakultas(), "Fakultas")
