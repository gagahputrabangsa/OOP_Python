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

        @staticmethod
    def print_data_teman(nomor_teman, teman):
        print("--- Data Teman", nomor_teman, "---")
        teman.print_data()

# main block function
if __name__ == "__main__":
    
    
    # Obj Creation
    murid1 = Student("Gagah Putra B")
    murid2 = Student("Agfan Herru Pratama H")
    murid3 = Student("I Made N A")
    murid4 = Student("Nathanael W")



