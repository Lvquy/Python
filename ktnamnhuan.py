#!/usr/bin/python
# -*- coding: utf8 -*-
class ktnhuan():
    def __init__(self,nam):
        self.nam = nam
    def ktnam(self):
        if self.nam % 4 == 0 and self.nam % 100 != 0 or (self.nam % 400 == 0 and self.nam % 100 != 0):
            return 'Nhuận'
        else:
           return 'Không nhuận'
i = 1
while i == 1:
    a = ktnhuan(input('nhập năm:'))
    print a.ktnam()
    i = input('Nhập 1 để tiếp tục: ')
else:
    print 'Xin chào'
