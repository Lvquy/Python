# coding: utf8
def ketqua(cung):
    a = open('conten.txt','r');
    str = a.read();
    if cung == 'Bạch dương':
        print str[1:1417] #bạch dương
    elif cung == 'Kim ngưu':
        print str[1420:2966] #kim ngưu
    elif cung == 'Song tử':
        print str[2969:4684] #song tử
    elif cung == 'Cự giải':
        print str[4687:6017] #cự giải
    elif cung == 'Sư tử':
        print str[6020:7403] #sư tử
    elif cung == 'Xử nữ':
        print str[7408:8868]#xử nữ
    elif cung == 'Thiên bình':
        print str[str.index('13') +2:str.index('14')]#thiên bình
    elif cung == 'Bọ cạp':
        print str[str.index('15')+2:str.index('16')]#thần nông
    elif cung =='Nhân mã':
        print str[str.index('17')+2:str.index('18')]#nhân mã
    elif cung == 'Ma kết':
        print str[str.index('19')+2:str.index('20')]#ma kết
    elif cung == 'Bảo bình':
        print str[str.index('21')+2:str.index('22')]#Bảo bình
    elif cung == 'Song ngư':
        print str[str.index('23')+2:str.index('24')]#Song ngư
    else:
        print 'lỗi'


