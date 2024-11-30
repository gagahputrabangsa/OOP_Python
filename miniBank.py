class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
    def simpan_uang(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo {self.nama} bertambah {jumlah}. Saldo saat ini: {self.saldo}")

    def tarik_uang(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi.")
        else:
            self.saldo -= jumlah
            print(f"{jumlah} berhasil ditarik. Saldo saat ini: {self.saldo}")


# Contoh penggunaan
rekening1 = RekeningBank("Ali", 1000000)


