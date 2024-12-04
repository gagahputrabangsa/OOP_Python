class Student:

    # Deklarasi variabel (instance & class)
    data_pribadi = "--- Data Pribadi ---"  # variabel class

    # Constructor
    def __init__(self, nama):
        self.nama = nama
        self.nim = None
        self.nilai = None

    # Method 
    def set_nim(self, nim):
        self.nim = nim

    # Method 
    def set_nilai(self, nilai):
        self.nilai = nilai

    # Method 
    def print_data(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Nilai:", self.nilai)

    
