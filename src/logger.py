# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:55:19 2024

@author: SWRM
"""

import logging
import os
from datetime import datetime


log_structure=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#create the path
log_file_path=os.path.join(os.getcwd(),"logs",log_structure)
os.makedirs(log_file_path,exist_ok=True)



logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)