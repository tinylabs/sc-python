#!/bin env python3
#
# Main UI after supercomputer has booted
#
from papirus import PapirusTextPos


# Main entry point
def start_ui ():
    disp = PapirusTextPos (False, rotation=270)
    disp.AddText ("UI running")
    disp.WriteAll ()
    
