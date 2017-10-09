# coding:utf8
import ktsonguyento
songto = []
a = input('Nhập số đầu vào: ')
if a ==1:
    print 'Không có số nguyên tố nào trong khoảng này'
if a == 2:
    songto.append(2)
if a > 2:
    for i in range(2, a+1):
        if ktsonguyento.kt(i) == True:
            songto.append(i)
print 'Các số nguyên tố từ 1 tới',a,':',songto
print 'Từ 1 tới',a,'có',songto.__len__(),'số nguyên tố'