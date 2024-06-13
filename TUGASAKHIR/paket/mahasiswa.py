class Mahasiswa:
    def __init__(self, nama, nama_kel, tugas, jml_anggota):
        self.nama = nama
        self.nama_kel = nama_kel
        self.tugas = tugas
        self.jml_anggota = jml_anggota

    def data(self):
        print("-----------------------------------------------------------------------")
        print(f"Saya                    : {self.nama}")

    def nama_kelompok(self):
        print(f"Kelompok                : {self.nama_kel}")

    def jumlah_anggota(self):
        print(f"Kelompok saya berjumlah : {self.jml_anggota} Orang")

class Kelompok1(Mahasiswa):
    def tugas_kelompok1(self):
        print()
        print("~ Kita ditugaskan untuk membuat Algoritma dan Struktur Data ~")

class Kelompok2(Mahasiswa):
    def tugas_kelompok2(self):
        print()
        print("~ Kita ditugaskan untuk membuat Pemrograman Berorientasi Objek(OOP) ~")

class Kelompok3(Mahasiswa):
    def tugas_kelompok3(self):
        print()
        print("~ Kita ditugaskan untuk membuat Pemrograman Jaringan ~")
        print("-----------------------------------------------------------------------")

kel1 = Kelompok1("Firda Febiola", 1, "Tugas 1", 5)
kel2 = Kelompok2("Bunga Citra Anggraeni", 2, "Tugas 2", 4)
kel3 = Kelompok3("Royhan", 3, "Tugas 3", 6)

kel1.data()
kel1.nama_kelompok()
kel1.jumlah_anggota()
kel1.tugas_kelompok1()

kel2.data()
kel2.nama_kelompok()
kel2.jumlah_anggota()
kel2.tugas_kelompok2()

kel3.data()
kel3.nama_kelompok()
kel3.jumlah_anggota()
kel3.tugas_kelompok3()
