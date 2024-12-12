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

