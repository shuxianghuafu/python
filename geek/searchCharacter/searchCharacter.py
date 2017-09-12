#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
The file was created by xiaohai to search
some characters in a directory.
"""


import os
import re


def search_psi3and3_example(directory, searchPattern):
    results = {}
    if os.path.isdir(directory):
        for (dirPath, dirNames, fileNames) in os.walk(directory):
            for eachFile in fileNames:
                if os.path.splitext(eachFile)[1] == ".cxx":
                    fileObj = open(str(dirPath) + "/" + str(eachFile))
                    try:
                        allLines = fileObj.readlines()
                    except UnicodeDecodeError:
                        continue
                    finally:
                        fileObj.close()
                    for eachLine in allLines:
                        result = re.search(searchPattern, eachLine)
                        if result:
                            findResult = str(dirPath) + "/" + str(eachFile)
                            results[findResult] = findResult
    return results


if __name__ == '__main__':
    directory = "/home/jinxiaohai"
    searchPattern = "psi3"
    results = search_psi3and3_example(directory, searchPattern)
    for key in results:
        print(results[key])
