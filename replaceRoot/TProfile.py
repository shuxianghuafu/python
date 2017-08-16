#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""document of the module"""


import math


class TProfile(object):
    """Documentation for TProfile
    """
    def __init__(self, Name, Title, Bins, Xmin, Xmax, Ymin, Ymax):
        self.Name = str(Name)
        self.Title = str(Title)
        self.NBins = int(Bins)
        self.BinWidth = (float(Xmax)-float(Xmin)) / self.NBins
        # 使用列表进行处理---->>>枕头书
        self.BinList = [[0.]*self.NBins]
        self.BinErrorList = [0.]*self.NBins

    def Fill(self, Value):
        for i in range(self.NBins):
            if Value >= i*self.BinWidth and Value < (i+1)*self.BinWidth:
                self.BinList[i].append(Value)
        self.Deal()

    def Deal(self):
        self.AverageBin = [0.]*self.NBins
        StandardDeviation = [0.]*self.NBins
        for i in range(len(self.BinList)):
            self.AverageBin[i] = sum(self.BinList[i]) / len(self.BinList[i])
        for i in range(len(self.BinList)):
            """遍历每一个Bin"""
            Sumj = 0.
            for j in self.BinList[i]:
                """遍历该Bin的每一元素，求出sigma."""
                Sumj = Sumj + math.pow(j-self.AverageBin[i], 2)
            StandardDeviation[i] = math.sqrt(1./len(self.BinList[i])*Sumj)
            self.BinErrorList[i] = StandardDeviation[i] / math.sqrt(
                len(self.BinList[i]))


if __name__ == '__main__':
    import random

    pro = TProfile("name", "title", 100, 0, 3, 0, 1)
    for w in range(1000):
        pro.Fill(random.uniform(0, 3))

    print(pro.AverageBin)
