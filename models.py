#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 00:21:50 2019

@author: Maksym Tymkovych
"""

from math import pi, sin, cos, sqrt

class SliderCrankModel:
    def __init__(self, crank_length, rod_length):
        self.crank_length = crank_length
        self.rod_length = rod_length
        self.phi = 0
        self.x = 0
        self.y = 0
    
    def getSliderPosition(self):
        return self.x + self.crank_length * cos(self.phi) + sqrt(self.rod_length**2 - (self.crank_length*sin(self.phi))**2)

if __name__ == '__main__':
    model = SliderCrankModel(10.0, 25.0)
    print model.getSliderPosition()
    model.phi = pi
    print model.getSliderPosition()