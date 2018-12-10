import os

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
fileList=[]

def nameInFile(dir,s):
    if s in os.path.split(dir)[1]:
        print(os.path.abspath(dir))
    if os.path.isfile(dir):
        return

    for dire in os.listdir(dir):
        nameInFile(os.path.join(dir,dire),s)
