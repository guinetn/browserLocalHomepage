## Python Logging Template
## No more print() or the default root logger

>python3 app.py

MyAwesomeProject/

app.py
    
import logger
log = logger.setup_applevel_logger(file_name = 'app_debug.log')
import mymodule
log.debug('Calling module function.')
mymodule.multiply(5, 2)
log.debug('Finished.')    



mymodule/

___init__.py 


module.py

import logger
log = logger.get_logger(__name__)
def multiply(num1, num2): # just multiply two numbers
    log.debug("Executing multiply function.")
    return num1 * num2
    






logger/
___init__.py 
from .logger import *


logger.py
import logging
import sys
APP_LOGGER_NAME = 'MyAwesomeApp'

def setup_applevel_logger(logger_name = APP_LOGGER_NAME, file_name=None): 
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)
    if file_name:
        fh = logging.FileHandler(file_name)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
    
def get_logger(module_name):    
   return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)
