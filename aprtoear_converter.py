#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:14:55 2021
Converting APR to EPR

@author: maven
"""


class AprtoEarConverter:
    def __init__(self, apr, no_compounding):
        self.apr = apr
        self.no_compounding = no_compounding
        
    def calculate_ear(self):
        if self.no_compounding == 1:
            ear = self.apr
        elif self.no_compounding == 2:
            ear = (((1+(self.apr)/2))**2)-1
        elif self.no_compounding == 4:
            ear = (((1+(self.apr)/4))**4)-1
        elif self.no_compounding == 12:
            ear = (((1+(self.apr)/12))**12)-1
        elif self.no_compounding == 365:
            ear = (((1+(self.apr)/365))**365)-1
        else:
            print('Not Valid')
        return ear


