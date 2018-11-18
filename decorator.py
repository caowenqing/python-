# -*- coding: utf-8 -*-
import time, functools


def metric(fn):  
    start=time.time()  
    def decorator(*args, **kw): 
        stop=time.time()      
        print('%s executed in %s ms' % (fn.__name__, stop-start))
        return fn(*args, **kw)    
    return decorator

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
