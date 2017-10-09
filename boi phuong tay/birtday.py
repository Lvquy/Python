#!/usr/bin/python
# -*- coding: utf8 -*-
from datetime import datetime, date
import time
import random, boi
from ktcung import *
import ktgiap
localtime = time.localtime(time.time())
now = datetime.now()
nam = now.year
thang = now.month
ngay = now.day
kq =  ['sau 1 ngày nữa','sau 2 ngày nữa','sau 1 năm nữa', 'sau 20 năm nữa T_T ', 'sau 1 tháng nữa', 'sau 2 tháng nữa', 'sau ngày tận thế','vào ngày mai','...']
k = 'y'
while(k =='y'):
    if (localtime.tm_hour > 0) and (localtime.tm_hour < 5 ):
        print 'Giờ này Bạn nên đi ngủ...'
    if (localtime.tm_hour > 5) and( localtime.tm_hour <12):
        print 'Chào buổi sáng!!!'
    if (localtime.tm_hour > 12) and (localtime.tm_hour < 18):
        print 'Chào buổi chiều'
    if (localtime.tm_hour >18):
        print 'Chào buổi tối!!'
    ten = raw_input('Tên bạn là gì? ')
    gtinh = raw_input('Giới tính: ')
    ngays1 = raw_input('Mời bạn nhập ngày sinh: ')
    thangs1 = raw_input('Mời bạn nhập tháng sinh: ')
    nams = input('Mời bạn nhập năm sinh: ')
    ngays = int(ngays1)
    thangs = int(thangs1)

    a = cung(int(ngays), int(thangs))
    somayman= random.randrange(1,100,1)
    tuoitho = ['60','100','61','62','63','64','65','66','70','71','72','75','76','80','85','86','87','90''91','92','200','300','400','10000']
    if (nam - nams) > 17:
        if gtinh == 'nam' or gtinh == 'Nam' or gtinh == 'NAM':
            honnhan=raw_input('Bạn có bạn gái rồi chứ? ')
        else:
            honnhan=raw_input('Bạn có bạn trai rồi chứ? ')
    else:
        print 'Ăn nhanh chóng lớn nhé bé ^^ ',ten
    if nams>0 and nams< nam +1 and thangs>0 and thangs <13 and ngays>0 and ngays < 32 :
       sinhnhat = date(nams, thangs, ngays)
       ngaysinhnhat = date(nam, thangs, ngays)
       print '-------------------------'
       print 'Xin chào bạn',ten.title()
       print 'Hôm nay là ngày:',ngay,'tháng',thang,'năm',nam
       print 'Bạn thuộc cung:',a.ktcung()
       print  'Năm nay bạn', nam -nams,'tuổi.','năm tuổi âm lịch của bạn là năm:',ktgiap.giap(nams),',','Bạn đã sống được',(datetime.date(now) - sinhnhat).days, 'ngày.','(',((datetime.date(now) - sinhnhat).days)*24,')', 'Giờ'
       if (nam -nams) >17:
           if (honnhan == 'rồi' or honnhan == 'roi' or honnhan == 'Rồi' or honnhan == 'RỒI' or honnhan == 'ROI' or honnhan == 'Roi'):
               print 'Chúc bạn luôn hạnh phúc bên người yêu!'
           else:
               if gtinh == 'nam' or gtinh =='NAM' or gtinh =='Nam':
                   print 'Bạn gái của bạn sẽ xuất hiện',random.choice(kq)
               else:
                   print 'Bạn trai của bạn sẽ xuất hiện',random.choice(kq)
       else:
           print 'Đủ 18t đi anh chờ nhé' ,ten
       if thangs < thang or (thangs == thang and ngays < ngay):
        print 'Sinh nhật năm nay của bạn đã qua',(datetime.date(now)-ngaysinhnhat).days,'ngày' ,'(',ngays,'-', thangs, '-',nam,')'
        print 'Bạn còn sống được khoảng', int(int(random.choice(tuoitho)) - (nam - nams)), 'năm nữa'
        print 'Số may mắn của bạn hôm nay là:',somayman
        print 'Bạn có muốn biết thêm về tính cách con người bạn không?'
        b = input('Nhấn 1 để xem tính cách bạn: ')
        if b == 1:
            print boi.ketqua(a.ktcung())
        print '********code by Lv Quý *************'
        k = raw_input('Bạn muốn tiếp tục? Y/N ')
       else:
           if ngaysinhnhat == datetime.date(now):
               print 'Chúc mừng sinh nhật bạn',ten.title(), 'nhé!'
               print 'Bạn còn sống được khoảng', int(int(random.choice(tuoitho)) - (nam - nams)), 'năm nữa'
               print 'Số may mắn của bạn hôm nay là:', somayman

               print 'Bạn có muốn biết thêm về tính cách con người bạn không?'
               b = input('Nhấn 1 để xem tính cách bạn: ')
               if b == 1:
                   print boi.ketqua(a.ktcung())

               print '********code by Lv Quý *************'
               k = raw_input('Bạn muốn tiếp tục? Y/N ')
           else:
            print 'Còn',(ngaysinhnhat - datetime.date(now)).days, 'ngày nữa đến sinh nhật bạn','(',ngays,'-', thangs, '-',nam,')'
            print 'Bạn còn sống được khoảng', int(int(random.choice(tuoitho)) - (nam - nams)), 'năm nữa'
            print 'Số may mắn của bạn hôm nay là:', somayman

            b = input('Nhấn 1 để xem tính cách bạn: ')
            if b ==1:
                print boi.ketqua(a.ktcung())
            print '********code by Lv Quý *************'
            k = raw_input('Bạn muốn tiếp tục? Y/N ')
    else:
      print 'Vui lòng nhập đúng định dạng ngày tháng năm'
      print '********code by Lv Quý *************'
      k = raw_input('Bạn muốn tiếp tục? Y/N ')