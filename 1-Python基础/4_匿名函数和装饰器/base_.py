# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 匿名函数和装饰器
# 要求：
# 1.学会不定长参数的用法(*args, **kwargs)。
# 2.学会利用匿名函数进行复杂排序
# 2.学会装饰器的使用(装饰器就是一个函数，python的开发框架中大量出现装饰器)


# 对a进行排序。 排序规则：a中元素是个长度不定的元组，根据这些元组的最大值对a进行排序。
def get_key(*args):
	return max(args)
# get_key = lambda x:max(*x)
a = [(1,2), (2, 88), (3,33), (66,2), (1,2,3)]
a.sort(key=get_key)  # 用到了不定长参数的用法。（搜Python不定长参数 或者 Python args kwargs）
#a.sort(key=lambda x:max(*x))    # 通过匿名函数实现， 匿名函数再次体现了Python的简洁
print(a)


# 利用装饰器打印一个函数的执行时间
import time
def calculate_time(fun):
	def _fun(*args, **kwargs):
		start_time = time.time()
		res = fun(*args, **kwargs)
		end_time = time.time()
		print(f"function used {end_time-start_time:.10f} s")  # .10f代表小数点后保留10位
		return res
	return _fun


@calculate_time
def add(a,b):
	return a+b


c = add(1,2)
print(c)

a = [1,2]

def tet1(*args, **kwargs):
	return args

tet1(a)
