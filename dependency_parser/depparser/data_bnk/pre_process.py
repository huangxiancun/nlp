# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:10:43 2018

@author: zykj_hxc
"""

import os 
#import sys
import pandas as pd


#train_file = sys.argv[1]
#test_file = sys.argv[2]



data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")

train_path = os.path.join(data_dir,"train.conll")
test_path = os.path.join(data_dir,"test.conll")

pre_train_output_path = os.path.join(data_dir,"train.conll_pre")
pre_test_output_path = os.path.join(data_dir,"test.conll_pre")

train_data = pd.read_csv(train_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["one","two","three","four","five","six","seven","eight"])
test_data = pd.read_csv(train_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["one","two","three","four","five","six","seven","eight"])

print train_data.head(10)
print test_data.head(10)