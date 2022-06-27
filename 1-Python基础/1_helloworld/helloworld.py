# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 目的： 感受Python的灵活与敏捷。
# 要求：
# 1. 掌握print函数用法(sep end参数)。
# 2. 掌握命名规范。(所有函数、变量、均以 student_li 形式命名。所有类均以 MyStudent形式命名 )
# 3. Python语言的精妙之处在于面向过程，用少量易读的代码实现业务。
# 4. 养成写注释的习惯，关键处要加注释。


# 形式1，直接输出
print("######①#####")
hello_str = 'hello world!'
print(hello_str)


# 形式2， 利用for循环逐个字符输出。
print("######②#####")
for i in hello_str:
    print(i, end='')
else:
    print('')

# 形式3， 逆序输出
print("######③#####")
print(hello_str[::-1])

# 形式4， 对字符排序后输出
print("######④#####")
print(''.join(sorted(hello_str)))


# 形式5，分割为两个单词
print("######⑤#####")
for w in hello_str.rstrip("!").split():
    print(w)

