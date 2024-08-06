import globalvars
import os



class bridgeID():
    def __init__(self, arg):

        # import global variables
        globalvars.init()

        try:
            globalvars.bridgeID = os.listdir(arg)
            print(globalvars.bridgeID)
            globalvars.error_message = ''
        except:
            globalvars.error_message = "Error: Bridge Database Was Not Imported!"