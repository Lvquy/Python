#!/usr/bin/python
# -*- coding: utf8 -*-
from datetime import datetime
from datetime import date
import time;
import random
localtime = time.localtime(time.time())
now = datetime.now()
nam = now.year
thang = now.month
ngay = now.day
kq =  ['1 ngày','2 ngày','1 năm', '20 năm nữa ', '1 tháng', '2 tháng']
k = 'y'
while(k =='y'):
    if (localtime.tm_hour > 0) and (localtime.tm_hour < 5 ):
        print 'Giờ này Bạn nên đi ngủ...'
    if (localtime.tm_hour > 5) and( localtime.tm_hour <12):
        print 'Chào buổi sáng!!!'
    if (localtime.tm_hour > 12) and (localtime.tm_hour < 18):
        print 'Chào buổi chiều'
    else:
        print 'Chào buổi tối!!'
    ten = raw_input('Tên bạn là gì? ')
    gtinh = raw_input('Giới tính: ')
    ngays = input('Mời bạn nhập ngày sinh: ')
    thangs = input('Mời bạn nhập tháng sinh: ')
    nams = input('Mời bạn nhập năm sinh: ')
    if (nam - nams) > 18:
        if gtinh == 'nam' or gtinh == 'Nam' or gtinh == 'NAM':
            honnhan=raw_input( 'Bạn có bạn gái rồi chứ? ')
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
       print  'Năm nay bạn', nam -nams,'tuổi.' ,'Bạn đã sống được',(datetime.date(now) - sinhnhat).days, 'ngày.','(',((datetime.date(now) - sinhnhat).days)*24,')', 'Giờ'
       if honnhan == 'rồi' or honnhan == 'roi' or honnhan == 'Rồi' or honnhan == 'RỒI' or honnhan == 'ROI' or honnhan == 'Roi':
           print 'Chúc bạn luôn hạnh phúc bên người yêu!'
       else:
           if gtinh == 'nam' or gtinh =='NAM' or gtinh =='Nam':
               print 'Bạn gái của bạn sẽ xuất hiện sau',random.choice(kq),'nữa'
           else:
               print 'Bạn trai của bạn sẽ xuất hiện sau',random.choice(kq),'nữa'
       if thangs < thang or (thangs == thang and ngays < ngay):
        print 'Sinh nhật năm nay của bạn đã qua',(datetime.date(now)-ngaysinhnhat).days,'ngày' ,'(',ngays,'-', thangs, '-',nam,')'
        print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'
        print '********Một Sản phẩm của Lv Quý*************'
        k = raw_input('Bạn muốn tiếp tục? Y/N ')
       else:
           if ngaysinhnhat == datetime.date(now):
               print 'Chúc mừng sinh nhật bạn',ten.title(), 'nhé!'
               print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'
               print '********Một Sản phẩm của Lv Quý************'
               k = raw_input('Bạn muốn tiếp tục? Y/N ')
           else:
            print 'Còn',(ngaysinhnhat - datetime.date(now)).days, 'ngày nữa đến sinh nhật bạn','(',ngays,'-', thangs, '-',nam,')'
            print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'
            print '********Một Sản phẩm của Lv Quý************'
            k = raw_input('Bạn muốn tiếp tục? Y/N ')

    else:
      print 'Vui lòng nhập đúng định dạng ngày tháng năm'
      print '********Một Sản phẩm của Lv Quý************'
      k = raw_input('Bạn muốn tiếp tục? Y/N ')