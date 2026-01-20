class Point:
    def __init__(self, hoanh_do, tung_do):
        self.hoanh_do = hoanh_do
        self.tung_do = tung_do
    def thuoc_truc_hoanh(self):
        return self.tung_do == 0
    def thuoc_truc_tung(self):
        return self.hoanh_do == 0
    def khoang_cach(self):
        return (self.hoanh_do **2 + self.tung_do ** 2) ** 0.5
x, y = map(int, input().split())

point = Point(x, y)
if point.thuoc_truc_hoanh():
    print("thuoc truc hoanh")
else:
    print("ko thuoc truc hoanh")
if point.thuoc_truc_tung():
    print("thuoc truc tung")
else:
    print("ko thuoc truc tung")
print(f"{point.khoang_cach():.2f}")