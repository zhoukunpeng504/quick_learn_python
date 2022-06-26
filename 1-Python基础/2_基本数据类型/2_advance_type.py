# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 高级数据类型
# 列表 list  元组 tuple  字典 dict  集合 set
# 补充：有序字典 collections.OrderedDict
# 要求：
# 1. 掌握list常用方法 和列表解析的用法。
# 2. 掌握元组的多种写法 并理解元组是不可变的。
# 3. 掌握字典的常用方法 及 一行代码完成字典的合并。掌握collections.OrderedDict和dict的区别和应用场景。
# 4. 掌握用{}的形式创建集合。

# list常用方法
a = [1,2,3,4,5,1]
print(a.count(1))  # 列表中 值等于1的元素的个数
a.append(6)
print(a)
a.pop(1)  # 删除索引位置为1的元素。
print(a)
a.remove(3)  # 删除值等于3的元素
print(a)
a.sort()  # 对a排序
print(a)
a.reverse()  # 对a逆序
print(a)
b = [i for i in a if i>3]  # 列表解析
print(b)
c = [j for j in [i for i in a if i>3] if j >4]  # 列表解析的嵌套使用
print(c)
a = [1,2,3]      # 两个列表拼接
b = [4,5,6]
print(a+b)
print("###########")


# tuple(元组是不可变的！) 常用方法，
# 元组的多种写法
a = 1,2
b = (1,2)
def incr_(a, b):
	a += 1
	b += 1
	return a,b
c = incr_(0,1)
d = tuple((i for i in [1,2,3]  if i<3))  # 类似于列表解析的一种写法, (i for i in [1,2,3]  if i<3) 生成一个生成器对象，其可转为元组或列表
e = tuple(list((i for i in [1,2,3]  if i<3)))
f = tuple([1,2])
print(a == b == c == d == e ==f)
# 元组常用方法
print(f.count(1))   # 元组中值等于1的个数
print(f[::-1], f[:2], f[-2:])
a = (1,2,3)      # 两个元组拼接
b = (4,5,6)
print(a+b)
print("###########")



# dict 字典
a = {1:2, '2':3, (1,2):33}  # 数字、字符串、元组均可作为字典的key
# 筛选部分元素
a = {k:v  for k,v in a.items() if k!=1}
b = [k for k in a.keys() if k!='2']
c = [v for v in a.values() if v!=33]
print(a,b,c)
# 两个字典合并
a = {'1':1, "2":2}
b = {'3':3, '1':999}
c = dict(a,**b)
d = {i:j  for i,j in list(a.items()) + list(b.items())}
print(c,d)


# set 集合
a = {i for i in (1,2,3,4,5,22) if i>3 }
print(a, type(a))





