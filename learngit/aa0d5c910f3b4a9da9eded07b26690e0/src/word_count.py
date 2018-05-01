#! /usr/bin/env python
# -*- coding: utf-8 -*-

def wordcount(filepath):
    dic = {}
    file = open(filepath,"r")
    # 读取文件
    for line in file.readlines():

        for word in line.strip().split(" "):

            if word in dic:

                dic[word] = dic[word]+1
            else:
                dic[word] = 1
    file.close()
    # 放入字典

    t = len(max(dic,key=len))
    for word in sorted(sorted(dic.items()),key= lambda x:x[1],reverse= True):
        print(word[0]+":"+" "*(t-len(word[0])+1)+"*"*word[1])
    # 输出