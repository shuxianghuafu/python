#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import os
import sys
import shutil
import subprocess


fileObj = open('qt.cpp', 'w')

DIR1 = "/home/xiaohai/Software/qt/install/5.9.1/gcc_64/include/QtWidgets"
files = os.listdir(DIR1)
for eachFile in files:
    if eachFile.startswith('Q'):
        fileObj.write('#include <QtWidgets'+'/'+eachFile+'>'+'\n')

DIR2 = "/home/xiaohai/Software/qt/install/5.9.1/gcc_64/include/QtCore"
files = os.listdir(DIR2)
for eachFile in files:
    if eachFile.startswith('Q'):
        fileObj.write('#include <QtCore'+'/'+eachFile+'>'+'\n')

DIR3 = "/home/xiaohai/Software/qt/install/5.9.1/gcc_64/include/QtGui"
files = os.listdir(DIR3)
for eachFile in files:
    if eachFile.startswith('Q'):
        fileObj.write('#include <QtGui'+'/'+eachFile+'>'+'\n')
