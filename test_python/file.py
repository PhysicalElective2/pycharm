#file=open('aa.txt','r',encoding='GBK')
# file.seek(2) #只能是2 的倍数，因为GBK 一个中文两个字节
# string=file.read(2)
# print(string)
import os
print(os.getcwd()) #为什么这里和交互界面的输出不一样
with open('aa.txt', 'r', encoding='GBK') as file:
    number=0
    while True:
        number+=1
        line=file.readline()
        if line=='':
            break
        print(number,line,end="")
dir =os.walk(r"D:\1_topFile")
for i in dir:
    print(i,"\n")
print(os.stat(r'D:\1_topFile\邵熙.doc'))