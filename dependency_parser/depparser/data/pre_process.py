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

def load_data(train_path,test_path,pre_train_output_path,pre_test_output_path,unique_path):
    """
    读取文件
    """
    train_data = pd.read_csv(train_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["one","two","three","four","five","six","seven","eight"])
    test_data = pd.read_csv(test_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["one","two","three","four","five","six","seven","eight"])
    #去掉Nan数据
    train_data.fillna("")
    test_data.fillna("")

    train_data_pre = train_data[["one","two","four","five","seven","eight"]]
    test_data_pre = test_data[["one","two","four","five","seven","eight"]]
    unique_data = pd.DataFrame(train_data_pre["eight"].unique())
    
    train_data_pre.to_csv(pre_train_output_path,index = False,sep = "\t")
    test_data_pre.to_csv(pre_test_output_path,index = False,sep = "\t")
    unique_data.to_csv(pre_unique_path,index = False,sep = "\t")

def processing_label():
    """
    处理标签
    """
    pass

def joint_data():
    """
    拼接成可以训练的数据
    """
    pass

if __name__ == "__main__":
    
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data/")

    train_path = os.path.join(data_dir,"train.conll")
    test_path = os.path.join(data_dir,"test.conll")
    

    pre_train_output_path = os.path.join(data_dir,"train.conll_pre")
    pre_test_output_path = os.path.join(data_dir,"test.conll_pre")  
    pre_unique_path = os.path.join(data_dir,"unique.txt")
    
    load_data(train_path,test_path,pre_train_output_path,pre_test_output_path,pre_unique_path)
    
    
    
    
    