# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:35:45 2018

@author: Jiacuo
"""
import sys
import os
import numpy as np
import pandas as pd
import time
import requests

url='http://coincap.io'

class coincap(object):
    def __init__(self):
        self.session=requests.session()
    
    def get_symbolist(self):
        """GET symbol list"""
        return self.session.get("%s/coins" % url).json()
    
    def get_slide(self, coin):
        front=self.session.get("%s/front" % url).json()
        for i in range (0, len(front)):
            if front[i]['short']==coin:
                return front[i]
    
    def get_global(self):
        """ GET total"""
        return self.session.get("%s/global" % url).json()
    
    def get_coin(self, coin):
        """ GET specific coin's data"""
        return self.session.get("%s/page/%s" % (url, coin)).json()
    
    def get_history(self, coin):
        """GET history data of the coin"""
        return self.session.get("%s/history/%s" % (url, coin)).json()
    
    def get_histerm(self, period, coin):
        """GET one coin's history during the specific period"""
        return self.session.get("%s/history/%dday/%s" % (url, period, coin)).json()



