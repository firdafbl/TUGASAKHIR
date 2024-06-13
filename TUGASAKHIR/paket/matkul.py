class MataKuliah:
    def __init__(self, nama_mk, kode_mk, sks):
        self.nama_mk = nama_mk
        self.kode_mk = kode_mk
        self.sks = sks

    def info(self):
        print("-----------------------------------------------------------------------")
        print(f"Nama Matkul             : {self.nama_mk}")
        print(f"Kode Matkul             : {self.kode_mk}")
        print(f"SKS                     : {self.sks}")
        print("-----------------------------------------------------------------------")

MataKuliah1 = MataKuliah ("Pemrograman Lanjut", "TIF471", 3)
MataKuliah2 = MataKuliah ("Pendidikan Pancasila", "MPK106", 2)
MataKuliah3 = MataKuliah ("Sistem Basis Data", "TTI223", 3)

MataKuliah1.info()
MataKuliah2.info()
MataKuliah3.info()
