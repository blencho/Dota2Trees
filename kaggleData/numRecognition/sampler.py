'''
Created on Jul 7, 2013

@author: jcochran
'''
from numpy import random as r


"""
===============
Write test sample
of 1/5 size
===============
"""

test_read = open("test.csv",'r')
test_write = open("test_sample.csv",'w')

for line in test_read:
    if r.randint(0,high=5) == 3:
        test_write.write(line)
        
test_read.close()
test_write.close()



"""
===============
Write train sample
===============
"""

train_read = open("train.csv", 'r')
train_write = open("train_sample.csv",'w')

for line in train_read:
    if r.randint(0,high=5) == 3:
        train_write.write(line)
        
train_read.close()
train_write.close()