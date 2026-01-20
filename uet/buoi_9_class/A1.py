class Cylinder:
    def __init__(self, bankinh, chieucao):
        self.bankinh = bankinh
        self.chieucao = chieucao
    def dien_tich_be_mat(self):
        pi = 3.14
        return 2 * pi * self.bankinh ** 2 + 2 * pi * self.bankinh * self.chieucao
    def the_tich(self):
        pi = 3.14
        return pi * self.bankinh ** 2 * self.chieucao
r, h = map(float, input().split())
cylinder = Cylinder(r, h)
a = cylinder.dien_tich_be_mat()
b = cylinder.the_tich()
print(f"{a:.2f} {b:.2f}")