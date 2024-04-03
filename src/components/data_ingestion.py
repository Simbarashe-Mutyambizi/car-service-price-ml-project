# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:53:27 2024

@author: SWRM
"""

import pandas as pd
import numpy
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from src.utils import connector
import sys 
from dataclasses import dataclass


class DataIngestion:
    def __init__(self):
        self.connection_string="mongodb+srv://simbarashewilliammutyambizi:XGM78EHOhzC3EyXY@cluster0.0dpurw7.mongodb.net/?retryWrites=true&w=majority"
        
    def DataIngestor(self):
        logging.info("Loading data from cloud database")
        try:
            df=connector(self.connection_string)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            return(
                train_set,
                test_set
                
                )
        except Exception as e:
            raise CustomException(e, sys)
            
            
if __name__=="__main__":
    obj=DataIngestion()
    train_set,test_set=obj.DataIngestor()
    print(test_set)
            
            
        

