# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
import os

mypath = "C:\GitHub\Python"

files = []
dirs = []

for (dirpath, dirnames, filenames) in os.walk(mypath):
    files.extend(filenames)
    dirs.extend(dirnames)
    break

print(dirs)
print(len(files))
print(files)


def func2(x):
    return x**2

def func1(x):
    """
    Test function
    :type x: int
    :return:
    """
    return x+1

y = 1

c = func1(y)

print(c)
