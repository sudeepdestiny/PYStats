# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:21:39 2019

@author: 1596657
"""

import numpy as np
from scipy.stats import binom
np.random.seed(1)
data=binom.rvs(n=1,p=0.5,size=10000)
count = np.bincount(data)
print('Heads : '  + str(count[0]) + ' tails : ' + str(count[1])) 
