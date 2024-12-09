class Dog:

    def __init__(self, nama, jenis=None, umur=None, warna=None):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.warna = warna

    def set_name(self, nama):
        self.nama = nama

    def set_color(self, warna):
        self.warna = warna

    
