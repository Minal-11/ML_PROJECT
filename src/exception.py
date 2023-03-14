import sys 
#  this sys library bascially help in functioning in python 
# This module provides access to some variables used or maintained by 
# the interpreter and to functions that interact strongly with the interpreter. It is always available
from src.logger import logging

# function which gives you the message how your message looks like wrt to custom exception

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# create own custom exception class  inhertited from exception

class CustomException(Exception):
#  overriden the innit function

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
#  finally print the error message varibale 

    def __str__(self):
        return self.error_message
    
