class Mahasiswa:

    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.nama = "Urname"
        self.nim = "064xxxxxx"
        self.fakultas = "Industrial Faculty"
        self.hobi = "Reading"

    def hitung_luas_persegi_panjang(self):
        return self.panjang * self.lebar

    def info_persegi_panjang(self):
        return f"{self.nama} {self.nim}\n----->PROGRAM MENGHITUNG LUAS PERSEGI PANJANG<-----\nPersegi panjang dengan panjang {self.panjang}cm dan lebar {self.lebar}cm memiliki luas sebesar {self.hitung_luas_persegi_panjang()}cm^2"

