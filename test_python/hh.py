print(1+1)
import sys
import keyword
'''
你好
'''
print('Python %s on %s' % (sys.version, sys.platform))
print(keyword.kwlist)
print(type(keyword.kwlist))
print(id(keyword.kwlist))# id 获取内存地址
a=10
b=11
print(str(a+b))#转化为字符串
tip=input("please input")# 输入都作为字符串读取 
print(type(tip))
grade=[98,100]
print(sum(grade,5))##学会看参数列表。。。
"""
你好
"""