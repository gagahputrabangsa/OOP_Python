import math

class Volume:
    def hitung_volume(self, sisi=None, panjang=None, lebar=None, tinggi=None, jari_jari=None):
        if sisi is not None:
            return sisi ** 3  #cubic
        elif panjang is not None and lebar is not None and tinggi is not None:
            return panjang * lebar * tinggi  # beam
        elif jari_jari is not None and tinggi is not None:
            return math.pi * jari_jari ** 2 * tinggi  # tube
        else:
            return "Parameter tidak valid"

#obj creating
v = Volume()

print("===================\nNama: Gagah Putra B\nNim: 064002100036\n===================")
# calc cubic's vol
sisi_kubus = 5
volume_kubus = v.hitung_volume(sisi=sisi_kubus)
print(f"Volume kubus dengan sisi {sisi_kubus} adalah: {volume_kubus}cm^3")

# calc beam's vol
panjang_balok = 4
lebar_balok = 3
tinggi_balok = 6
volume_balok = v.hitung_volume(panjang=panjang_balok, lebar=lebar_balok, tinggi=tinggi_balok)
print(f"Volume balok dengan panjang {panjang_balok}, lebar {lebar_balok}, dan tinggi {tinggi_balok} adalah: {volume_balok}cm^3")

# calc tube's vol
jari_jari_tabung = 2
tinggi_tabung = 8
volume_tabung = v.hitung_volume(jari_jari=jari_jari_tabung, tinggi=tinggi_tabung)
print(f"Volume tabung dengan jari-jari {jari_jari_tabung} dan tinggi {tinggi_tabung} adalah: {volume_tabung}cm^3")


