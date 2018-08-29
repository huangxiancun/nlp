# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 15:16:48 2018

@author: zykj_hxc
"""

import os 

import pandas as pd

data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
train_path = os.path.join(data_dir, "test.conll_pre1")
#train_label_path = os.path.join(data_dir,"train_label.txt")
test_label_path = os.path.join(data_dir,"tmp_test.txt")


output_path = os.path.join(data_dir,"unique.txt")

re1 = pd.read_csv(train_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["one","two","three","four","five","six"])
re2 = pd.read_csv(test_label_path,sep= '\t',index_col=False,skip_blank_lines= False, names=["www"])
#input_f = sys.argv[1]
#output_f = "result.txt"

#fout = opne(output_f, 'w')
"""with open(output_f,"w")as fout,open(train_path,"r") as fin:
    sen = ""
    for i, token in  enumerate(fin):
        token_conll = token.strip().split("\t")
        print token_conll
        if len(token_conll)!= 10:
            fout.write("%s\n"%sen)
            sen = ""
        else:
            sen += '%s'%token_conll[2]
    #print sen
"""
#print re2.head(10)
re1 = re1.fillna("")
re1_unique = pd.DataFrame(re1["six"].unique())
#re2 = re2.fillna("")
#rint re1.head(10)
#new_re = re1[["two","three","four"]]
#new_re["wwww"]=re2[["www"]]
#print new_re.head(10)
re1_unique.to_csv(output_path,index= False,sep="\t")
        
        

 