# coding: utf8
class cung:
    def __init__ (self, ngay, thang):
        self.ngay = ngay
        self.thang = thang
    def ktcung(self):
        if (self.thang ==3 and self.ngay > 20) or (self.thang == 4 and self.ngay < 20):
            return 'Bạch dương'
        elif (self.thang == 4 and self.ngay > 19) or (self.thang==5 and self.ngay < 21):
            return 'Kim ngưu'
        if (self.thang ==5 and self.ngay > 20) or (self.thang == 6 and self.ngay < 22):
            return 'Song tử'
        elif (self.thang == 6 and self.ngay > 21) or (self.thang==7 and self.ngay < 23):
            return 'Cự giải'
        elif (self.thang == 7 and self.ngay > 22) or (self.thang==8 and self.ngay < 23):
            return 'Sư tử'
        elif (self.thang == 8 and self.ngay > 22) or (self.thang==9 and self.ngay < 23):
            return 'Xử nữ'
        elif (self.thang == 9 and self.ngay > 22) or (self.thang==10 and self.ngay < 24):
            return 'Thiên bình'
        elif (self.thang == 10 and self.ngay > 23) or (self.thang==11 and self.ngay < 22):
            return 'Bọ cạp'
        elif (self.thang == 11 and self.ngay > 21) or (self.thang==12 and self.ngay < 22):
            return 'Nhân mã'
        elif (self.thang == 12 and self.ngay > 21) or (self.thang==1 and self.ngay < 20):
            return 'Ma kết'
        elif (self.thang == 1 and self.ngay > 19) or (self.thang==2 and self.ngay < 19):
            return 'Bảo bình'
        elif (self.thang == 2 and self.ngay > 18) or (self.thang==3 and self.ngay < 21):
            return 'Song ngư'