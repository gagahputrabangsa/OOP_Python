import math

class Volume:
    def hitung_volume(self, sisi=None, panjang=None, lebar=None, tinggi=None, jari_jari=None):
        if sisi is not None:
            return sisi ** 3  # Volume kubus
        elif panjang is not None and lebar is not None and tinggi is not None:
            return panjang * lebar * tinggi  # Volume balok
        elif jari_jari is not None and tinggi is not None:
            return math.pi * jari_jari ** 2 * tinggi  # Volume tabung
        else:
            return "Parameter tidak valid"

# Membuat objek dari kelas Volume
v = Volume()

print("===================\nNama: Gagah Putra B\nNim: 064002100036\n===================")
# calc cubic's vol
sisi_kubus = 5
volume_kubus = v.hitung_volume(sisi=sisi_kubus)
print(f"Volume kubus dengan sisi {sisi_kubus} adalah: {volume_kubus}cm^3")


