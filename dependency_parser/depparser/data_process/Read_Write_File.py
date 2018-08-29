# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:06:11 2018

@author: huangxiancun
"""

import os




class Read_Write_File():
    
    
    def read_file():
        """
        读取文件
        """
        pass
    
    def write_file():
        """
        写入文件
        """
        pass
    
    def load_file_path():
        """
        load到当前文件路径
        """
        #load到data目录下
        data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
        #load当前文件路径
        data_path = os.path.join(data_dir, "test.conll_pre1")
        return data_path