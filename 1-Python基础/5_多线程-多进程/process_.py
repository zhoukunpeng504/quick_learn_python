# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/24
# 多线程 多进程
# 1. 线程池的使用。 由于GIL机制，python一个进程只能利用一个cpu，但是可以使用多线程提高IO密集型程序的效率(如网络爬虫)
# 2. 多进程的使用。
from multiprocessing import Pool


def handle(*args):
	while 1:
		pass


pool = Pool(10)
pool.map(handle,[1,2,3,4,5])



