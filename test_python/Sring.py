verse="野渡无人舟自横"
encodeRes=verse.encode('GBK')
print(encodeRes)
decodeRes=encodeRes.decode('GBK')
print(decodeRes)
try:
    resJie=verse[100:102]#明明也没有为什么不出错
except IndexError:
    print("不存在索引")

list=['a','b','c']
reslianjie="@".join(list)
print(reslianjie)#第一个元素前不加分割符号
print(reslianjie.count("@"))
print(reslianjie.upper())
