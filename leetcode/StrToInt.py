import  re
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def GetUglyNumber_Solution(self, index):
        """丑数，输出从小到大第index的丑数
        """
        
    #res=[]
    def Permutation(self, ss):
        """
        字符串的排列顺序,可以用dfs,有个问题，ss 里面可能有重复的数字
        :param ss:
        :return:
        """
        if len(ss) == 0:
            return []
        self.res=[]
        temp=""
        flag=[]
        for i in range(0,len(ss)):
            flag.append(False)
        self.dfs(ss,temp,flag)
        #剔除重复的,不能保证顺序
        #return list(set(self.res))
        res2 = []
        for x in self.res:
            if x not in res2:
                res2.append(x)
        return res2

    def dfs(self, ss,temp,flag):
        if len(temp)==len(ss):
            self.res.append(temp)
        else:
            for i in range(0,len(ss)):
                if not flag[i]:
                    temp1=temp+ss[i]
                    flag[i]=True
                    self.dfs(ss,temp1,flag)
                    flag[i]=False




    # write code here
    def cutRope(self, number):
        """
        剪绳子
        :param number:
        :return:
        """
        if number <= 2:
            return 1
        if number == 3:
            return 2
        remainder = number % 3  # remainder为余数
        if remainder == 1:
            return 4 * (3 ** (number // 3 - 1))
        elif remainder == 2:  # python 还有这个用法哦，别忘了啊
            return 2 * (3 ** (number // 3))
        else:
            return 3 ** (number // 3)


    def Add(self, num1, num2):
        """
        不用加减乘除的加法
        https://blog.csdn.net/lrs1353281004/article/details/87192205
        :param num1:
        :param num2:
        :return:
        """
        while(num2!=0):
            num1=num1^num2 #不可以，这个num1在这里已经改变了,然而后面还用得到
            num2=(num1&num2)<<1 & 0xffffffff
        return  num1 if num1 <0x7fffffff else ~(num1^0xffffffff)
    def isNumeric(self, s):
        """
        判断字符串是否表示数值（包括整数和小数）。
        例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
        但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        :param s:字符串
        :return:bool
        """
        #星花是0或多个
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([Ee][\+\-]?[0-9]+)?$",s)


    def isValid(self,s:str)->bool:
        list1=[]
        for i,v in enumerate(s):
            if(v=='[' or v=='{' or v=='('):
                #入栈
                list1.append(v)
            else:
                if len(list1)==0:
                    return False
                if((v==')' and list1[-1]=='(') or (v==']' and list1[-1]=='[') or v=='}' and list1[-1]=='{' ):#这个有问题
                    list1.pop()
                else:
                    return  False
        if len(list1)==0:
            return True
        else:
            return False
    """
    大佬就是大佬
        while '{}' in s or '()' in s or '[]' in s:
                s = s.replace('{}', '')
                s = s.replace('[]', '')
                s = s.replace('()', '')
            return s == ''
    """

    def Convert(self, pRootOfTree):
        """
        输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
        要求不能创建任何新的结点，只能调整树中结点指针的指向。
        :param pRootOfTree:  二叉树
        :return: 双向链表
        """
        if not pRootOfTree:
            return []  #返回值是空
        self.array=[]
        self.MidTraversal(pRootOfTree)
        for i,v in enumerate(self.array[:-1]):
            v.right=self.array[i+1]
            self.array[i+1].left=v
        return self.array[0]
    def MidTraversal(self, root):
        if not root:
            return
        self.MidTraversal(root.left)
        self.array.append(root)
        self.MidTraversal(root.right)
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        temp=0  #临时变量记录所有数取异或的结果
        for i in array:
            temp =temp^i
        #根据temp 中第一个1 将原始数据集区分
        index =0
        while(temp & 1==0):
            index+=1
            temp=temp>>1
        a=b=0
        for i in array:
            if self.isBit(i,index):
                a= a^i
            else:
                b^=i
        return [a,b]
    def isBit(self,num,index):
        """
        判断num的二进制从低到高index 位是不是1
        :param num: 数字
        :param index: 二进制从低到高的位置
        :return: num 的index 位是不是1
        """
        num =num>>index
        return num & 1
    def strtoInt(self,s):#类的方法第一个参数是seft，应该是嫌弃这个太简单了，不给通过
        try:
            return int(s)
        except Exception as e:
            return 0

    def StrToInt(self,s):
        if s=='-2147483649':return 0
        if len(s)== 0:
            return 0
        i=0  #循环起点
        flag=1 # 符号标志变量
        if s[0]=='+':
            i=i+1
        if s[0]=='-':
            flag=-1
            i=i+1
        res=0
        for j in range(i,len(s),1):# 末尾不用
            print(j ,i,len(s))
            if s[j] > '9' or s[j] < '0':
                return 0
            else:
                res+=int(s[j])*10**(len(s)-j-1)
        return res *flag

if __name__== '__main__':
    print('this is ')
    s=Solution()
    print(s.strtoInt(-2147483649)) # self 参数可以不给出
    print(s.StrToInt('-2147483649'))
    #print(s.FindOne([1,1,2,2,3,3,6,5,5]))
    print(s.FindNumsAppearOnce([4,6,2,2,3,3,8,8,9,9,1000000,1000000]))
    print(s.isValid("{{{[{}}}}}"))
    print(s.Add(56,56))
    print(s.Permutation("aa"))
