#!/usr/bin/env python3




import sys


#from xlwt import *

from openpyxl import Workbook


from CBULine import *
from DeductionLine import *

import CBULoader
import DeductionLoader

import ReconciledEntry 


from os import listdir
from os.path import isfile, join
import os
import datetime



def Test():
    mapTest={}
    mapTest["a"]=9
    mapTest["b"]=3
    for key,val in mapTest.items():
        print(key,val)
    
    
