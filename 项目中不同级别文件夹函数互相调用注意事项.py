#项目中多文件之间函数互相调用
import sys
#调用这个文件上一级文件
sys.path.append('..')
#调用这个文件上上一级文件
#sys.path.append('..\..') 

#lns为该python文件上一级文件夹，test_sum为该lns文件夹中的test_sum.py文件
from lns import test_sum
a = test_sum.sum1(3,5)
print(a)

#重点：这个主要涉及到python文件运行起点的问题
