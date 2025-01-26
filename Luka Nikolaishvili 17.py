class Rectangle:
    def __init__(self, width, length, feri):
        self.feri = feri
        self.length = length
        self.width = width


    def fartobi(self):
        return self.width * self.length

    def perimetri(self):
        return 2 * (self.width + self.length)


    def __str__(self):
        return (f"perimetri aris: {self.perimetri()}\n"
                f"fartobi aris: {self.fartobi()}\n"
                f"feri aris: {self.feri}\n")


obj1 = Rectangle(1, 5, "lurji")
obj2 = Rectangle(3, 3, "mwvane")
obj3 = Rectangle(3, 7, "yviteli")


print(obj1)
print(obj2)
print(obj3)