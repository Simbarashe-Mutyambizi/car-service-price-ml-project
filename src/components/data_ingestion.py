# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:53:27 2024

@author: SWRM
"""

import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils import connector
import sys 



class DataIngestion:
    def __init__(self):
        self.connection_string="mongodb+srv://simbarashewilliammutyambizi:XGM78EHOhzC3EyXY@cluster0.0dpurw7.mongodb.net/?retryWrites=true&w=majority"
        
    def DataIngestor(self):
        logging.info("Loading data from cloud database and cleaning")
        try:
            df=connector(self.connection_string)
            df.dropna(inplace=True)
            df.drop_duplicates(inplace=True)
            df.drop(["TechSupport","Company"],inplace=True,axis=1)
            bins=np.linspace(df["Customer-Age"].min(),df["Customer-Age"].max(),4)
            groups=["Post-teen","Mature","Senior"]
            df["Customer_age_group"]=pd.cut(df["Customer-Age"],labels=groups,bins=bins,include_lowest=True)
            return df
            
                 
        except Exception as e:
            raise CustomException(e, sys)
            
'''            
if __name__=="__main__":
    obj=DataIngestion()
    df=obj.DataIngestor()
    print(df)
            
 '''           
        

