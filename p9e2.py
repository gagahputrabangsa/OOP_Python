class p9e2:
    @staticmethod
    def methodTambahInt(x, y):
        return x + y

    @staticmethod
    def methodTambahfloat(x, y):
        return x + y

myNum1 = p9e2.methodTambahInt(8, 5)
myNum2 = p9e2.methodTambahfloat(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)



class p9e2:
    @staticmethod
    def tambah(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return p9e2.tambah_int(x, y)
        elif isinstance(x, float) and isinstance(y, float):
            return p9e2.tambah_double(x, y)
        else:
            return "Unsupported types for addition"

