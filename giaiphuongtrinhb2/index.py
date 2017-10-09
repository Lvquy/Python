#coding:utf8
def giaipt(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        return 'Vô nghiệm'
    if delta ==0:
        x1 = (-b/2*a)
    else:
        x1 = (-b- delta**0.5)/2*a
        x2 = (-b + delta ** 0.5)/2*a
    return x1,x2
a = input('Nhập hằng số  a: ')
b = input('Nhập hằng số b: ')
c = input('Nhập  hằng số c: ')
print giaipt(a,b,c)