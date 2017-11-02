#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import os


def totalList():
    result = []
    for i in range(5200):
        result.append(i)
    return result


def modify(fileName):
    allNumber = totalList()
    currentNumber = []
    with open(fileName) as f:
        for eachLine in f:
            amptTotalName = eachLine.strip().split('/')[8]
            amptNumber = int(amptTotalName.split('_')[2])
            currentNumber.append(amptNumber)
    finalResult = []
    for j in allNumber:
        if j not in currentNumber:
            finalResult.append(j)
    print(finalResult)


if __name__ == '__main__':
    fileList = os.getcwd() + '/' + 'trim.list'
    modify(fileList)
