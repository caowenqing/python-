# -*- coding: utf-8 -*-
def normalize(name):
    nameUpdate=name.lower()
    nameUpdate=name[0].upper()+nameUpdate[1:]
    return nameUpdate
    
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
