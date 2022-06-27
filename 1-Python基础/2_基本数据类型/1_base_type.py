# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 基本数据类型：
# int float str bool
# 目的： 掌握四种基本数据类型的常用方法。
# 要求：
# 1. 重点掌握字符串的常用方法和字符串索引的使用。 △ △ △


# int
a = 1
b = 2
print(a/b, a//b) # // 如果结果是小数，则向小的方向取整。

# float
a = 1.1
b = 2.1
print(a+b)

# str
# ① 单引号 双引号  三引号的用法。
a = 'hello world'  # 一般情况用单引号 和 双引号没有区别
b = "hello world"
aa = 'hello "world"'  # 如果字符串内含有单引号，那就用双引号
bb = "hello 'world'"  # 如果字符串内含有双引号，就用单引号
cc = ''' 'hello'  "world" '''  # 如果字符串内含有单引号，双引号。 就用三引号
print(a, b, aa, bb, cc)

# ② 字符串格式化
a = 123
b = 1.1
c = "test string"
d1 = f"{a}, {b}, {c}"    # python3中新引入的语法特性。
d2 = "%d, %.1f, %s" % (a,b,c)
d3 = "{}, {}, {}".format(a, b, c)
print(d1, d2, d3, d1 == d2 == d3, sep='\n')
# ③ split方法 ：字符串分割(按空字符分割)
a = 'aa bb  cc    dd     ee    \n   ff\t gg \r kk'
b = a.split()
print(b)
# ④ splitlines方法： 字符串分割(按行分割)
text = '''国际新闻早报：

【摩洛哥内政部：移民冲击摩边防致18人死亡】

据摩洛哥官方通讯社摩通社25日报道，2000多名来自撒哈拉以南非洲地区的移民24日试图翻越摩洛哥边境铁丝围栏进入西班牙。

报道援引摩洛哥内政部消息说，5名试图越境的移民在冲突现场丧生，13人受重伤后于24日晚在摩医院不治身亡。'''
text_lines = text.splitlines()
print(text_lines)  # 带空行
# ⑤ join, replace,find, rfind, count  strip startswith
print("\n".join(text_lines))
print(text.replace("移民",'民众'))  # 把所有移民替换为民众
print(text.replace("移民",'民众', 1)) # 把第一个移民替换为民众
print(text.find("早报"))      # 从开头寻找第一个早报出现的位置
print(text.rfind("医院"))     # 从末尾寻找第一个医院出现的位置
print(text.count('移民'))     # 计算移民出现的次数

# ⑥ 字符串索引常用形式 [:4]  [-4:]  [4:-4]  [::-1]
text = '0123456789'
print(text[:4])   # 等价于 [0:4]
print(text[-4:])  # 从倒数第四个字符开始 到末尾
print(text[4:-4]) # 从正数第五个字符开始 到末尾第四个字符(不包含它)
print(text[::-1]) # 对字符串逆序





