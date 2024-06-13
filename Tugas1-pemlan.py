class Perpustakaan:
    def __init__(self,buku):
        self.buku = buku

    def pinjam(self):
        pass

class Perpustakaan1(Perpustakaan):
    def pinjam(self):
        return('Pemrograman')
        
class Perpustakaan2(Perpustakaan):
    def pinjam(self):
        return('Basis Data')
    
class Perpustakaan3(Perpustakaan):
    def pinjam(self):
        return('Web Dasar')
    
perpustakaan1 = Perpustakaan1('Nabilla')
perpustakaan2 = Perpustakaan2('Leuna')
perpustakaan3 = Perpustakaan3('Firda')
    
print(f'{perpustakaan1.buku} meminjam buku {perpustakaan1.pinjam()}')
print(f'{perpustakaan2.buku} meminjam buku {perpustakaan2.pinjam()}')
print(f'{perpustakaan3.buku} meminjam buku {perpustakaan3.pinjam()}')