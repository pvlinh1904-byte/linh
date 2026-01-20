class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def nam_nhuan(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def inValid(self):
        d = self.day
        m = self.month
        y = self.year
        if y <= 0 or not (1 <= m <= 12):
            return False
        so_ngay = [31, 29 if self.nam_nhuan() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return (1 <= d <= so_ngay[m -1])
    
    def next_day(self):
        d = self.day
        m = self.month
        y = self.year
        so_ngay = [31, 29 if self.nam_nhuan() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if d < so_ngay[m - 1]:
            d += 1

        else:
            d = 1
            m += 1
            if m == 13:
                m = 1
                y += 1
        return (f"{d:02d}/{m:02d}/{y}")
    
    def previous_day(self):
        d = self.day
        m = self.month
        y = self.year
        so_ngay = [31, 29 if self.nam_nhuan() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if d > 1:
            d -= 1
        
        else:
            m -= 1
            if m == 0:
                m = 12
                y -= 1
            d = so_ngay[m - 1]
        return (f"{d:02d}/{m:02d}/{y}")
linh = input().strip()
d, m, y = map(int, linh.split("/"))
date = Date(d, m, y)
if not date.inValid():
    print("INVALID")
else:
    print(date.next_day())
    print(date.previous_day())