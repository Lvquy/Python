# coding: utf8
def ketqua(cung):
    a = open('conten.txt','r');
    str = a.read();
    if cung == 'Bạch dương':
        print str[str.index('1')+1:str.index('2')] #bạch dương
    elif cung == 'Kim ngưu':
        print str[str.index('3')+1:str.index('4')] #kim ngưu
    elif cung == 'Song tử':
        print str[str.index('5')+1:str.index('6')] #song tử
    elif cung == 'Cự giải':
        print str[str.index('7')+1:str.index('8')] #cự giải
    elif cung == 'Sư tử':
        print str[str.index('9')+1:str.index('10')] #sư tử
    elif cung == 'Xử nữ':
        print str[str.index('11')+2:str.index('12')]#xử nữ
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
    a.close()


