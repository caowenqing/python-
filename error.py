#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复

# -*- coding: utf-8 -*-

from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            print("input error!")
            return 0

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
    r = calc('12 + 345 + qq')
    print('12 +345 +qq =',r)

main()

