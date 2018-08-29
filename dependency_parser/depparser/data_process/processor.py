# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:05:14 2018

@author: zykj_hxc
"""

import os 




def initialize():
    """
    语料初始化
    """
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"data/")
    #print data_dir
    train_data_path = os.path.join(data_dir,"trian.conll_pre2")
    
    train_lines = read_corpus_from_file(train_data_path)
    train_sentences = [sentence for sentence in process_sentence(train_lines)]
    #print train_sentences
    return  extract_feature(train_sentences)
    


def read_corpus_from_file(file_path):
    """
    读取语料
    """
    f = open(file_path,"r")
    lines = f.readlines()
    f.close()
    return lines

def process_sentence(lines):
    
    """
    处理句子
    """
    sentence = []
    for line in lines:
        if not line.strip():
            yield sentence
            sentence = []
        else:
            sentence.append(line.decode('utf-8').strip().split(u'\t'))
    

def extract_feature(sentences):
    """
    抽取特征
    """
    
    features, tags = [], []
    for index in range(len(sentences)):
        feature_list, tag_list = [], []
        for i in range(len(sentences[index])):
            print i
            print len(sentences)
            feature = {"w0": sentences[index][i][0],
                       "p0": sentences[index][i][1],
                       "w-1": sentences[index][i-1][0] if i != 0 else "BOS",
                       "w+1": sentences[index][i+1][0] if i != len(sentences[index])-1 else "EOS",
                       "p-1": sentences[index][i-1][1] if i != 0 else "un",
                       "p+1": sentences[index][i+1][1] if i != len(sentences[index])-1 else "un"}
            feature["w-1:w0"] = feature["w-1"]+feature["w0"]
            feature["w0:w+1"] = feature["w0"]+feature["w+1"]
            feature["p-1:p0"] = feature["p-1"]+feature["p0"]
            feature["p0:p+1"] = feature["p0"]+feature["p+1"]
            feature["p-1:w0"] = feature["p-1"]+feature["w0"]
            feature["w0:p+1"] = feature["w0"]+feature["p+1"]
            feature_list.append(feature)
            tag_list.append(sentences[index][i][-1])
        features.append(feature_list)
        tags.append(tag_list)
        #print features[0]
        #print tags[0]
    return features, tags
    
    
    
    
if __name__ == "__main__":    
    
    feature,tags = initialize()
    print feature[0]
    print tags[0]
    
    
    
    
    
    
    
    
    


