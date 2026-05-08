#poly -> many phism -> form
#operator overloading


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i + ",self.img, "j")

num1 = Complex(1,3)
num1.showNumber()