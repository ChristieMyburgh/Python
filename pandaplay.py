# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import os

files = []

mypath = "C:\GitHub\Python"

for (dirpath, dirnames, filenames) in os.walk(mypath):
    files.extend(filenames)



def func1(x):
    return x+1

y = 1

c = func1(y)

print(c)
