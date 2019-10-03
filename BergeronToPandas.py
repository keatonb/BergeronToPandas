#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:36:16 2019

Description at https://github.com/keatonb/BergeronToPandas

Made to read synthetic white dwarf color tables from 
http://www.astro.umontreal.ca/~bergeron/CoolingModels/

@author: keatonb
"""

#from __future__ import print_function
import collections
import pandas as pd
import numpy as np

def BergeronToPandas(filename):
    """Read white dwarf synthetic color tables to Pandas DataFrames
    
    Parameters:
    filename (str): path and filename of synthetic color tables file
    
    Returns:
    OrderedDict:of Pandas DataFrames
    """
    #Set up empty ordered dict to hold tables
    d = collections.OrderedDict()
    
    #Things are slightly different if this file contains info about one WD mass
    #Or measurements for either DAs/DBs on a logg,Teff grid
    masstrack = True    
    if filename[-2] == 'D':
        masstrack = False
    
    with open(filename) as f:
        #keep looking for additional tables
        while True:
            line = f.readline()
            #If there is another line, read another table
            if line:
                #First number is number of rows in table
                nrowsstr = line.split()[0]
                nrowsint = int(nrowsstr)
                #Recorded different
                if not masstrack:
                    nrowsstr = line.split()[1]
                    nrowsint = int(nrowsstr)*int(line.split()[0])
                    
                #Followed by table description that we use as dict key
                tablename = line.split(nrowsstr)[1].split('          ')[0].strip()
                #Then names of output columns
                colnames = f.readline().replace('log g','logg').split()
                
                #Set up empty list to hold rows of data
                data = []
                #Iterate over data and add to list
                for i in range(int(nrowsint)):
                    vals = [float(item) for item in f.readline().split()]
                    data.append(vals)
                data=np.array(data)
                
                #Convert to Pandas DataFrame
                df = pd.DataFrame(data=data,columns=colnames)
                #And add to OrderedDictionary
                d[tablename] = df
                
            else:
                return d