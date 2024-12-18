class Triangle:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    
def menu(self):
        print("\nPROGRAM TO CALCULATE TRIANGLE PERIMETER & AREA")
        print("1. Perimeter")
        print("2. Area")

    def calculate_perimeter(self):
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        side3 = float(input("Enter side 3: "))
        perimeter = side1 + side2 + side3
        return perimeter


    def calculate_area(self):
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        return area

