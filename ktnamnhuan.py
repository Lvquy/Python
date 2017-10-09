#!/usr/bin/python
# -*- coding: utf8 -*-
def kt(nam):
    if nam % 19 == 0 or nam % 19 ==  3 or nam % 19 == 6 or nam % 19 ==  9 or nam % 19 ==  11 or nam % 19 ==  14 or nam % 19 ==  17 :
        return True
    return False
print kt(input('Nhập năm cần kt: '))
