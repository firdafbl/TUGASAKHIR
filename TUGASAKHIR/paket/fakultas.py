from abc import ABC, abstractmethod

class Fakultas(ABC):
    def nama_fakultas(self):
        pass
    def jumlah_prodi(self):
        pass

class FST(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Sains dan Teknologi"
    def jumlah_prodi(self):
        return 5
    
class FEB(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Ekonomi dan Bisnis"
    def jumlah_prodi(self):
        return 3
    
class FH(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Hukum"
    def jumlah_prodi(self):
        return 1
    
class FP(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Peternakan"
    def jumlah_prodi(self):
        return 1
    
class FBS(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Bahasa dan Sastra"
    def jumlah_prodi(self):
        return 3
    
class FIP(Fakultas):
    def nama_fakultas(self):
        return "Fakultas Ilmu Pendidikan"
    def jumlah_prodi(self):
        return 5
    
    print("-----------------------------------------------------------------------")
def fakultas_info(fakultas: Fakultas):
    print(f"Nama Fakultas           : {fakultas.nama_fakultas()}")
    print(f"Jumlah Prodi            : " + str (fakultas.jumlah_prodi()) + " Program Studi")
    print("-----------------------------------------------------------------------")

fst = FST();
feb = FEB();
fh  = FEB();
fp  = FP();
fbs = FBS(); 
fip = FIP(); 

fakultas_info(fst);
fakultas_info(feb);
fakultas_info(fh);
fakultas_info(fp);
fakultas_info(fbs);
fakultas_info(fip);
