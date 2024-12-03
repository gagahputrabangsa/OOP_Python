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

