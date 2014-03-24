#######################################
#
# managers.py
# ---------------------------------------
# In this file, we define basic managers for low-level 
# database manipulation.
#
#######################################

import os
import codecs

from .poetrymanagers.textpm import TextPM

def PoetryManager(class_type, prefix):
    '''Factory Method'''
    if class_type == "text":
        return TextPM(prefix)
    else:
        raise Exception, "No such manager"

