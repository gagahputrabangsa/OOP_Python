class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
    def simpan_uang(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo {self.nama} bertambah {jumlah}. Saldo saat ini: {self.saldo}")

    
