#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__='hailin'


import sys #访问sys模块的所有功能

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,world")
    elif len(args) == 2:
        print("Hello,%s" % args[1])
    else:
        print('Too many arguments!')
        
# 主要用于测试，在其他模块中被引用时，判断失败
if __name__ == '__main__':
    test()  