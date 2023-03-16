# Logs provide developers with an extra set of eyes that are 
# constantly looking at the flow that an application is going through. 
# They can store information, like which user or IP accessed the application.
# If an error occurs, then they can provide more insights than a stack trace
# by telling you what the state of the program was before it arrived at the 
# line of code where the error occurred.

import logging
import os
from datetime import datetime

# create log file function 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# path 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# set this log file into basic configration i.e into specific format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #  incaase of info we could print the message only
    level=logging.INFO,


)
# just to check whether evrything working fine or not till now
# if __name__=="__main__":
#     logging,info("Logging has started")
