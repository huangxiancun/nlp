# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 07:34:06 2018

@author: zykj_hxc
"""

from config import get_config
from corpus import get_corpus
from sklearn.externals import joblib


class Predict():
    
    def __init__(self):
        self.config = get_config()
        self.corpus = get_corpus()
        self.corpus.initialize()
        self.model = None
        
    def load_model(self,name='model'):
        model_path = self.config.get('model', 'model_path').format(name)
        self.model = joblib.load(model_path)
        
    def predict(self, sentences):
        """
        预测
        """
        self.load_model()
        features, _ = self.corpus.extract_feature(sentences)
        return self.model.predict(features)
    
    def test(self):
        x_test, y_test = self.corpus.generator(train=False)
        y_predict = self.model.predict(x_test)
        return y_predict
if __name__ == '__main__':
    
    pre = Predict()
    pre.test()
    
    
    