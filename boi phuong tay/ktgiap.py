# coding: utf8
def giap(nams):
    i = (int(nams) - 3) % 10
    j = (int(nams) - 3) % 12
    if i == 1:
        can_new = 'Giáp '
    if i == 2:
        can_new = 'Ất '
    if i == 3:
        can_new = 'Bính '
    if i == 4:
        can_new = 'Đinh '
    if i == 5:
        can_new = 'Mậu '
    if i == 6:
        can_new = 'Kỷ '
    if i == 7:
        can_new = 'Canh '
    if i == 8:
        can_new = 'Tân '
    if i == 9:
        can_new = 'Nhâm '
    if i == 0:
        can_new = 'Quý '
    if j == 1:
        chi_new = 'Tý'
    if j == 2:
        chi_new = 'Sửu'
    if j == 3:
        chi_new = 'Dần'
    if j == 4:
        chi_new = 'Mão'
    if j == 5:
        chi_new = 'Thìn'
    if j == 6:
        chi_new = 'Tỵ'
    if j == 7:
        chi_new = 'Ngọ'
    if j == 8:
        chi_new = 'Mùi'
    if j == 9:
        chi_new = 'Thân'
    if j == 10:
        chi_new = 'Dậu'
    if j == 11:
        chi_new = 'Tuất'
    if j == 0:
        chi_new = 'Hợi'
    return can_new + chi_new
