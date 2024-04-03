# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:00:02 2024

@author: SWRM
"""

from pymongo import MongoClient 
import pandas as pd 





def connector(connection_string):
    client = MongoClient(connection_string)  
    myDb=client["OK_database"]
    table=myDb["Car service"]
    cursor = table.find({})  # Query all documents; add filters if needed
    
    # Convert the cursor to a list of dictionaries
    data = list(cursor)
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    return df



        