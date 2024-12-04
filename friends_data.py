class Student:

    # Deklarasi variabel (instance & class)
    data_pribadi = "--- Data Pribadi ---"  # variabel class

    # Constructor untuk inisialisasi objek Student
    def __init__(self, nama):
        self.nama = nama
        self.nim = None
        self.nilai = None

