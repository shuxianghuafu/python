#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import os
import shutil
import subprocess


def forLib(DIR):
    result = []
    if os.path.exists(DIR):
        files = os.listdir(DIR)
        for eachfile in files:
            if (os.path.isfile(DIR + '/' + eachfile)
                and eachfile.startswith('libopencv')
                and eachfile.endswith('.so')):
                result.append(eachfile)
    return result


def dealWithLib(libList):
    for eachLib in libList:
        name = str(eachLib.split(".")[0])
        newName = name.replace('lib', '-l')
        print(newName, end=' ')


if __name__ == '__main__':
    DIR = "/usr/lib64"
    resultLib = forLib(DIR)
    dealWithLib(resultLib)
