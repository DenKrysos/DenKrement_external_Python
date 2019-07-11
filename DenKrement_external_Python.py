#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
DenKrement_external_Python -- 

DenKrement_external_Python further description
    - Basic, Connectivity:
    - Basic, Msg send & receive:
    - Basic, Msg Format
                >>Dennis Krummacker<<
                
Notes:
    - 

It defines:
    - Interface for Interchanging Data at Runtime with the internal running ContextBroker-Mechanism of the C-Program DenKrement

@author:     Dennis Krummacker

@copyright:  2018 DFKI, Kaiserlautern. All rights reserved.

@license:    license

@contact:    dennis.krummacker@gmail.com
@deffield    updated: 13.08.2018
'''

 


from package.ansiescape import *  # @UnusedImport @UnusedWildImport
from package.communication.inter_programm.socket import *  # @UnusedWildImport
# from package.WindowManager_XServer import *  # @UnusedImport @UnusedWildImport
import sys  # @UnusedImport
# import math
# import time


try:
    input = raw_input  # @UndefinedVariable @ReservedAssignment
except NameError:
    pass
##Or Alternative:
# try:
#     import __builtin__
#     input = getattr(__builtin__, 'raw_input')
# except (ImportError, AttributeError):
#     pass



if sys.version_info < (3,):#Compatibility, because xrange has changed to range from Python 2.x to 3
    range = xrange  # @UndefinedVariable @ReservedAssignment
    
    



    
    
#-----------------------------------------------------

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
    









    
    
    
def Example_PythonDummy_Main():
    err=0  # @UnusedVariable
    global global_var
    
    sock_C=Unix_Socket_C_Python_Connect()
    msg=Msg_Python_C()
    msg.set_socket(sock_C)
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #That was a first temporary Test:
    #msg.recv()
    #msg.Debug_print_msg()
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    msg_testsend=Msg_Python_C()
    msg_testsend.set_socket(sock_C)
    
    #Register for Context as Consumer
    msg_testsend.prep_msg(DenKr_InfBroker_Msg_Type__Management,DenKr_InfBroker_Msg_SubType__Management__RegConsumerSocket,0,"","mcctrl"+"\x00"+"cake"+"\x00")#+"\x00")
        #defacto such a msg has to end with "Double-Null-Termination. On '\0' for ending the last string and one for ending the Message completely. But the sending function adds one last '\0' by itself
    msg_testsend.send()
    
    #send Info about a Context
    #    use String-Message
    msg_testsend.prep_msg(DenKr_InfBroker_Msg_Type__Raw,0,0,"cake","test from Py")
    msg_testsend.send()
    
    #send Info about a Context
    #    use Byte-Object-Message
    temp=1004
    msg_testsend.prep_msg(DenKr_InfBroker_Msg_Type__Raw,0,0,"cake",temp.to_bytes(4, byteorder=ENDIANESS_SEND))
    msg_testsend.send()
    
    #send Request about a Context
    msg_testsend.prep_msg(DenKr_InfBroker_Msg_Type__Request,0,0,"cake","")
    msg_testsend.send()
    
    try:
        while 1:
            err=msg.recv()
            if err==0:
                break
            msg.Debug_print_msg()
    except Exception:
        msg.close_socket();
    

    
#Workaround to be able to split Consumer and Producer Input (Info vs Request):
#   Just connect two times. Create two sockets, connect subsequently and use them for the different purposes, i.e. register Consumer over one socket and register Producer over the other.
def main(argv):
    print('Number of arguments:', len(argv), 'arguments.')
    print('Argument List:', str(argv))
    SET_ansi_escape_use()
    printansi(ansi_blue,"""I can even use colors!\n""")
    Example_PythonDummy_Main()
    
    
if __name__ == '__main__': main(sys.argv[1:])
