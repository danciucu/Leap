import globalvars
import pandas as pd
import os



class bridgeID():
    def __init__(self, arg):

        # import global variables
        globalvars.init()
        # get all bridge IDs
        globalvars.bridgeID = [name for name in next(os.walk(arg))[1] if '0' in name]