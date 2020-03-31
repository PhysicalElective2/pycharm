class MyClass:
    '''my class'''
    def __init__(self):#定义的时候必须有这个self 参数，但是，创建对象的时候可以不指定
        print("this is my class")
        self.__name="class1"  #实例属性定义在初始化方法中
    @property
    def getName(self):
        return self.name ##实现可读取但是不可以修改
    @property
    def say(self):
        print("属性方法")
        return "say method"
    def fly(self,word):
        print(word)
    pass
a=MyClass() #并没有显示帮助信息啊
print(a)
a.fly("I can fly")
MyClass.kkk="ok" # 动态给类添加属性，这还了得
print(a.kkk)
print(a.name)
print(a.say)
a.name='ffff'
print(a.getName)
try:
    pass
except ZeroDivisionError:
    print()