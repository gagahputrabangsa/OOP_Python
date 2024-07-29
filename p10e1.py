from shapes import Triangle, Square, Rectangle, Circle, Parallelogram
# Contoh penggunaan
print("==========================\nNama: Gagah Putra Bangsa\nNim: 064002100036\n==========================\nPraktikum 10\n==========================")
triangle = Triangle(5, 8)
print("Luas Segitiga:", triangle.calculate_area())

square = Square(4)
print("Luas Persegi:", square.calculate_area())

rectangle = Rectangle(5, 10)
print("Luas Persegi Panjang:", rectangle.calculate_area())

circle = Circle(3)
print("Luas Lingkaran:", circle.calculate_area())

parallelogram = Parallelogram(5, 8)
print("Luas Jajar Genjang:", parallelogram.calculate_area())
