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

    def run(self):
        self.menu()
        choice = int(input("Enter choice: "))

        if choice == 1:
            perimeter = self.calculate_perimeter()
            print(f"\nTriangle Perimeter: {perimeter:.1f} cm")
        elif choice == 2:
            area = self.calculate_area()
            print(f"\nTriangle Area: {area:.1f} cm^2")
        else:
            print("Invalid choice!")

        print("\nThank you for using this program!")


# Example Usage
name = input("Name: ")
nim = input("NIM: ")
triangle = Triangle(name, nim)
triangle.run()
