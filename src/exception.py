# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:55:05 2024

@author: SWRM
"""

import sys

#creation of error that grabs the error and error details 
def get_error_details(error,error_detail:sys):
    ##grab the error details
    _,_,error_dets=error_detail.exc_info()
    filename=error_dets.tb_frame.f_code.co_filename
    error_line=error_dets.tb_lineno
    error_sentence=str(error)
    
    error_contents=f"The error occurred in file {filename} on line {error_line}, the details are {error_sentence}"
    return error_contents


class CustomException(Exception):
    def __init__(self,error_contents,error_details:sys):
        super().__init__(error_contents)
        self.error_message=get_error_details(error_contents,error_details)
        
    def __str__(self):
        return self.error_message
        
        
            

