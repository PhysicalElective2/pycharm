import random
num=[random.randint(10,100) for i in range(11)]
price =[10,20,30,40]
halfPrice=[item*0.5 for item in price if item>20] #  python 这么牛逼还了得
print(halfPrice)
print(num)
arr =[[j for j in range(5)] for i in range(4)]  #太牛逼了吧
print(arr)
c="dd",45 #不用括号也可以定义元组
print(type(c))
tupleres=tuple(range(10,20,2)) #用tuple 创建元组
print(tupleres)
dictionary=dict()
print(type(dictionary))
name =['a','b','c','d']
grade=[1,2,3,4]
resZip=zip(name,grade) ##zip是什么东西啊
print(resZip)
dic=dict(resZip)
print(dict(resZip))
print(dic['a']if 'a' in dic else '字典里没有这个')
print(dic['v']if 'v' in dic else '字典里没有这个')
print(dic.get('a','没有'))
print(dic.get('hh','没有'))
print(dic.items())
# for item in dic.items():
#     print(item)
#     print(item[0])
# for key,val in dic.items():
#     print(key)
#     print(val)

print(dic.values())
randomDic={i:random.randint(10,100) for i in range(1,10)}
zipres=zip(name,grade)
tuidao={i:j for i,j in zipres}#推导表达式厉害啊
tuidao2={i:j for i,j in zipres}
print(resZip)
for i in resZip:
    print(i)
print("result tuidao")
print(tuidao)
print(tuidao)
print(randomDic)
#集合
