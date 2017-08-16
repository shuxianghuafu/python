#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""

import math


class LorentzVector(object):
    """Documentation for LorentzVector
    """
    def __init__(self, Px, Py, Pz, Energy):
        self.Px = float(Px)
        self.Py = float(Py)
        self.Pz = float(Pz)
        self.Energy = float(Energy)

    def GetPx(self):
        return self.Px

    def GetPy(self):
        return self.Py

    def GetPz(self):
        return self.Pz

    def GetE(self):
        return self.Energy

    def SetPx(self, Px):
        self.Px = float(Px)

    def SetPy(self, Py):
        self.Py = float(Py)

    def SetPz(self, Pz):
        self.Pz = float(Pz)

    def SetE(self, Energy):
        self.Energy = Energy

    def Pt(self):
        return math.sqrt(self.Px**2 + self.Py**2)

    def Rapidity(self):
        return 0.5*math.log((self.GetE()+self.GetPz())
                            / (self.GetE()-self.GetPz()))


if __name__ == '__main__':
    l = LorentzVector(3, 3, 3, 36)
    print("{0:8.4g} {1:8.4g} {2:8.4g} {3:8.4g}".
          format(l.GetPx(), l.GetPy(), l.GetPz(), l.GetE()))
    print("{0:8.4g} {1:8.4g}".format(l.Pt(), l.Rapidity()))
