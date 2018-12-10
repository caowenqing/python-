import os
from datetime import datetime

# 利用os模块实现'ls -l'命令
# 输出文件的最后修改时间，文件类型，size，name，

pwd = os.path.abspath('.') #获取当前目录的绝对路径
cwd= os.getcwd();
print(cwd)
print('%s 的目录' % pwd)
print('%s%12s%10s    %s' % ('最后修改时间', '类型', 'size', '文件名'))

for f in os.listdir(pwd):
    f_size = os.path.getsize(f) #文件大小
    modified_time = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y/%m/%d %H:%M')
    f_type = '<DIR>' if os.path.isdir(f) else ''  #如果是子目录，类型是<DIR>
    print('%s%9s%9d   %s' %(modified_time, f_type, f_size, f))
