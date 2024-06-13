class Hewan:                        #class utama
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        pass                        #tdk di eksekusi

class Kucing(Hewan):                #hewan=kata khusus kucing=kata umum/
    def suara(self):
        return('Meow')              #return=mengembalikan/menampilkan nilai tsb
    
class Anjing(Hewan):
    def suara(self):
        return('Guk guk')
    
class Ayam(Hewan):
    def suara(self):
        return('Kukuruyuk')
    
Kucing = Kucing('Momo')
Anjing = Anjing('Donggo')
Ayam = Ayam('Cocka')

print(f'{Kucing.nama} bersuara {Kucing.suara()}')
print(f'{Anjing.nama} bersuara {Anjing.suara()}')
print(f'{Ayam.nama} bersuara {Ayam.suara()}')