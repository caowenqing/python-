# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fa(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    for i in range(len(s)):
        if(s[i]=='.'):
            List1=s[:i]
            List2=s[i+1:]
            times=len(List2)
            break
    return reduce(fa, map(char2num, List1))+reduce(fa, map(char2num, List2))/pow(10,times)
    
    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
