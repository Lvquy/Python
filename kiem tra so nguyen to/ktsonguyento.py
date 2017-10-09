def kt(so):

    if so == 1:
        return False
    if so == 2:
        return True
    if 2<so<99999:
        for i in range(2,int(so*0.5)+1):
            if so % i ==0:
                return False
        return True
    else:
        return None