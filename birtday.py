#!/usr/bin/python
# -*- coding: utf8 -*-
from datetime import datetime
from datetime import date
now = datetime.now()
nam = now.year
thang = now.month
ngay = now.day
k = 'y'
while(k =='y'):
    ten = raw_input('Tên bạn là gì? ')
    ngays = input('Mời bạn nhập ngày sinh: ')
    thangs = input('Mời bạn nhập tháng sinh: ')
    nams = input('Mời bạn nhập năm sinh: ')
    if nams>0 and nams< nam +1 and thangs>0 and thangs <13 and ngays>0 and ngays < 32 :
       sinhnhat = date(nams, thangs, ngays)
       ngaysinhnhat = date(nam, thangs, ngays)
       print 'Xin chào bạn',ten.title()
       print 'Hôm nay là ngày:',ngay,'tháng',thang,'năm',nam
       print  'Năm nay bạn', nam -nams,'tuổi.' ,'Bạn đã sống được',(datetime.date(now) - sinhnhat).days, 'ngày.','(',((datetime.date(now) - sinhnhat).days)*24,')', 'Giờ'

       if thangs < thang or (thangs == thang and ngays < ngay):
        print 'Sinh nhật năm nay của bạn đã qua',(datetime.date(now)-ngaysinhnhat).days,'ngày' ,'(',ngays,'-', thangs, '-',nam,')'
        print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'
       else:
           if ngaysinhnhat == datetime.date(now):
               print 'Chúc mừng sinh nhật bạn',ten.title(), 'nhé!'
               print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'
           else:
            print 'Còn',(ngaysinhnhat - datetime.date(now)).days, 'ngày nữa đến sinh nhật bạn','(',ngays,'-', thangs, '-',nam,')'
            print 'Bạn còn sống được khoảng', int(60 - (nam - nams)), 'năm nữa'

    else:
      print 'Vui lòng nhập đúng định dạng ngày tháng năm'