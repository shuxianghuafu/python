#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib.pyplot as plt


fileObj = open("npart-xy.dat")
eventHead = fileObj.readline().strip().split()
IAEVT, MISS, IHNT2_1, IHNT2_3 = [int(x) for x in eventHead[:4]]
bimp = float(eventHead[4])

xprojPartList = []
yprojPartList = []

xtargPartList = []
ytargPartList = []

xprojPangguanList = []
yprojPangguanList = []

xtargPangguanList = []
ytargPangguanList = []

for i in range(IHNT2_1+IHNT2_3):
    track = fileObj.readline().strip().split()
    x, y = [float(i) for i in track[0:2]]
    JPandJT, NFPandNFT5 = [int(i) for i in track[2:4]]
    NFPandNFT3, NFPandNFT4 = [int(i) for i in track[5:7]]
    if JPandJT > 0:
        if NFPandNFT5 == 0:
            xprojPangguanList.append(x)
            yprojPangguanList.append(y)
        else:
            xprojPartList.append(x)
            yprojPartList.append(y)
    if JPandJT < 0:
        if NFPandNFT5 == 0:
            xtargPangguanList.append(x)
            ytargPangguanList.append(y)
        else:
            xtargPartList.append(x)
            ytargPartList.append(y)

fig = plt.figure(figsize=(10, 6), dpi=100)
ax = fig.add_subplot(1, 1, 1)

SIZE = 120
# Au
ax.scatter(xprojPangguanList, yprojPangguanList, s=SIZE,
           marker="o", color="#FFFFFF", edgecolor="red")
ax.scatter(xprojPartList, yprojPartList, s=SIZE, marker="o",
           color="#FF3E96", edgecolor="red")

# Cu
ax.scatter(xtargPangguanList, ytargPangguanList, s=SIZE,
           marker="o", color="#FFFFFF", edgecolor="blue")
ax.scatter(xtargPartList, ytargPartList, s=SIZE, marker="o",
           color="#00FFFF", edgecolor="blue")
#######################################################################
# single Au
xprojPangguanListMove = []
yprojPangguanListMove = []
AuXMove = 20
AuYMove = 8
for i in range(len(xprojPangguanList)):
    xprojPangguanListMove.append(xprojPangguanList[i]+AuXMove)
    yprojPangguanListMove.append(yprojPangguanList[i]+AuYMove)

xprojPartListMove = []
yprojPartListMove = []
for i in range(len(xprojPartList)):
    xprojPartListMove.append(xprojPartList[i]+AuXMove)
    yprojPartListMove.append(yprojPartList[i]+AuYMove)

ax.scatter(xprojPangguanListMove, yprojPangguanListMove, s=SIZE,
           marker="o", color="#FFFFFF", edgecolor="red")
ax.scatter(xprojPartListMove, yprojPartListMove, s=SIZE,
           marker="o", color="#FF3E96", edgecolor="red")

#####################################################################
# single Cu
xtargPangguanListMove = []
ytargPangguanListMove = []
CuXMove = 20
CuYMove = 8
for i in range(len(xtargPangguanList)):
    xtargPangguanListMove.append(xtargPangguanList[i]-CuXMove)
    ytargPangguanListMove.append(ytargPangguanList[i]-CuYMove)

xtargPartListMove = []
ytargPartListMove = []
for i in range(len(xtargPartList)):
    xtargPartListMove.append(xtargPartList[i]-CuXMove)
    ytargPartListMove.append(ytargPartList[i]-CuYMove)

ax.scatter(xtargPangguanListMove, ytargPangguanListMove, s=SIZE,
           marker="o", color="#FFFFFF", edgecolor="blue")
ax.scatter(xtargPartListMove, ytargPartListMove, s=SIZE,
           marker="o", color="#00FFFF", edgecolor="blue")

#####################################################################
# Au
xMeanAuPart = np.mean(xprojPartListMove)
yMeanAuPart = np.mean(yprojPartListMove)
# Cu
xMeanCuPart = np.mean(xtargPartListMove)
yMeanCuPart = np.mean(ytargPartListMove)

ax.annotate("Z", xy=(xMeanCuPart, yMeanCuPart),
            xytext=(xMeanAuPart+12, yMeanAuPart+4.8),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '<|-'},
            fontsize=24)
ax.annotate("$\Phi_{n}$", xy=(xMeanCuPart, yMeanCuPart),
            xytext=(xMeanCuPart+8, yMeanCuPart-8),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '<|-'},
            fontsize=24)
# line
line1x = np.linspace(xMeanCuPart+6, xMeanAuPart+10, 100)
line1y = 2./5. * line1x - 6
ax.plot(line1x, line1y, color='black', linestyle='--')
line2x = np.linspace(xMeanAuPart, xMeanAuPart+5, 100)
line2y = -line2x + yMeanAuPart + 21
ax.plot(line2x, line2y, color='black', linestyle="--")


# text
ax.text(xMeanAuPart+2, yMeanAuPart+8, 'Au', fontsize=24, color='red')
ax.text(xMeanCuPart-4, yMeanCuPart+8, 'Au', fontsize=24, color='blue')
ax.text(0, 12, "AMPT (b = 8fm)", fontsize=24, color='black',
        horizontalalignment='center',
        verticalalignment='center',
        alpha=1)

# 马赛克
ax.text(0, 9, "was created by xiaohai", fontsize=12, color='green',
        horizontalalignment="center",
        verticalalignment="center",
        alpha=1)

ax.set_axis_off()

plt.xlim(-35, 35)
plt.ylim(-20, 20)
plt.savefig("result.eps", fmt="eps")
plt.show()
