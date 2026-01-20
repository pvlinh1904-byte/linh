class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return (self.w * self.h) 
    def perimeter(self):
        return (self.w + self.h) * 2 
    def scale(self, k):
        self.w *= k
        self.h *= k

w, h, k = map(float, input("w, h, k = ").split())
rec = Rectangle(w, h)
rec.scale(k)
print(f" {rec.area():.2f} {rec.perimeter():.2f}")