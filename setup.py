# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:54:52 2024

@author: SWRM
"""

from setuptools import find_packages, setup
from typing import List

#this file creates the cursor for manuevoring through the files as packages
hypen="-e ."

def get_requirements(file_path: str)->List[str]:
    #open and read the requirements file
    with open(file_path) as file_obj:
        requirements_line=file_obj.readlines()
        #readlines creates a \n after reading a line, so replace with space
        requirements=[req.replace("\n"," ") for req in requirements_line]
        if hypen in requirements:
            requirements.remove(hypen)
        
        
        return requirements
    
    
    
setup(
       name="carservicemlporject",
       version="0.0.1",
       author="Simbarashe Rhyan William Mutyambizi",
       author_email="simbarashewilliammutyambizi@gmail.com",
       packages=find_packages(),
       install_requires=get_requirements("requirements.txt")
        )    