class calculate:
    def __init__(self):
        self.angka1 = 0
        self.angka2 = 0

    def input_angka(self):
        self.angka1 = float(input("Insert First Num: "))
        self.angka2 = float(input("Insert Second Num: "))

    def sum(self):
        return self.angka1 + self.angka2

calculate_simple = calculate()
print('======Sum Calculator====')
calculate_simple.input_angka()
hasil_penjumlahan = calculate_simple.sum()
print(f"Result: {hasil_penjumlahan}")
