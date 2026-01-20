class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def nam_nhuan(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def khong_hop_le(self):
        if self.month < 1 or self.month > 12:
            return False
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.nam_nhuan():
            max_day = 29
        else:
            max_day = days_in_month[self.month - 1]
        return 1 <= self.day <= max_day
    
    def next_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.nam_nhuan():
            max_day = 29
        else:
            max_day = days_in_month[self.month - 1]
        if self.day < max_day:
            return Date(self.day + 1, self.month, self.year)
        else:
            if self.month < 12:
                return Date(1, self.month + 1, self.year)
            else:
                return Date(1, 1, self.year + 1)
s = input().strip()
d, m, y = map(int, s.split('/'))
date = Date(d, m, y)
if not date.khong_hop_le():
    print("INVALID")
else:
    next_d = date.next_day()
    print(f"{next_d.day:02d}/{next_d.month:02d}/{next_d.year}")