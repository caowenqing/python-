# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if(a==0):
        x1=x2=-c/b,
        return (x1)
    else:
        delta=b*b-4*a*c
        if(delta<0):
            print("此方程无解")
        else:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            return (x1,x2)


#测试代码
print('quadratic(0, 1, 1) =', quadratic(0, 1, 1))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(0, 1, 1) != -1.0:
    print('测试失败')
elif quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
