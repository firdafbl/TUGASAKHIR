class Manusia: #cetak biru,def=fungsi,self=argumen,nama-umur=parameter
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f'Hallo, nama saya {self.nama} dan umur saya {self.umur}')

Manusia1 = Manusia('Firda', 20)
Manusia2 = Manusia('Royhan', 22)

Manusia1.sapa()
Manusia2.sapa()