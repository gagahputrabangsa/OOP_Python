class Awal:
    def __init__(self, gaji, golongan):
        self.gaji = gaji
        self.golongan = golongan

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji)

class Dosen(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji + 300000)


class Staff(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji * 2)


class Lainnya(Awal):
    def __init__(self, gaji, golongan):
        super().__init__(gaji, golongan)

    def print_gaji(self):
        print("Golongan", self.golongan, "Mendapatkan Gaji:", self.gaji)




