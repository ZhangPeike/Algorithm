#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''写一个函数，读入一个文本文件，
1.用正则表达式输出文件中所有Email地址
2.先将文件中的字母转化为数字，然后将数字倒序的方式排序后输出'''
#导入需要用的模块, re模块有正则表达式相关函数, os与sys包含操作程序参数\文件路径等
import re
import os
import sys
#读入参数: 一个文件
file = sys.argv[1]
#打开文件
with open(file, "r") as f_txt:
    #读入第一行
    line = f_txt.readline()
    #构造一个空数组(准备排序)
    num_list=[]
    #当该行不为空(文件结尾)
    while line:
        #对该行的每个字符转为数字(ord(cha)), 加入到num_list
        for cha in line:
            num_list.append(ord(cha))
        #利用re的搜索函数, 通过正则表达式查找*@*.*
        result = re.search(
            r'[0-9a-zA-Z\_]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+', line)
        #搜索结果不为空时才处理
        if result:
            index = result.span()
            #空字符串
            valid_email = ''
            #遍历搜索结果
            for i in range(index[0], index[1]):
                valid_email = valid_email+line[i]
            #打印邮箱名
            print valid_email
            # print index
        #读入下一行
        line = f_txt.readline()
    #对所有字符转成的数字进行转换
    num_list.sort(None,None,True)
    for x in num_list:
         print x
       # print email
