


import sys  # @UnusedImport
from socket import *  # @UnusedWildImport
from package.ansiescape import *  # @UnusedWildImport


    
#-----------------------------------------------------
SOCKET_PYTHON_C = "\0DenKrement_SOCKET_Python_C"
MSGTYPE_WIDTH_TO_C = 1 # 1 Byte (uint8_t)
MSGSUBTYPE_WIDTH_TO_C = 1 # 1 Byte (uint8_t)
MSGSRC_WIDTH_TO_C = 4
MSGLEN_WIDTH_TO_C = 8 # 8 Byte (uint64_t)
MSGFLAGS_WIDTH_TO_C = 1 # 1 Byte (uint8_t)
ENDIANESS_SEND = 'big' # 'big' or 'little'
#-----------------------------------------------------
MSG_TYPE_PY_C_MISC = b'\x00\x00'
MSG_TYPE_PY_C_GOT_BLOCK = b'\x00\x01'
MSG_TYPE_PY_C_WANT_BLOCK = b'\x00\x02'
MSG_TYPE_PY_C_DUMMY = b'\xFF\xFE'
MSG_TYPE_PY_C_ERR = b'\xFF\xFF'
#-----------------------------------------------------
#//Msg-Types:
DenKr_InfBroker_Msg_Type__Generic = 0
DenKr_InfBroker_Msg_Type__Request = DenKr_InfBroker_Msg_Type__Generic + 1
DenKr_InfBroker_Msg_Type__Management = DenKr_InfBroker_Msg_Type__Request + 1
DenKr_InfBroker_Msg_Type__Raw = DenKr_InfBroker_Msg_Type__Management + 1
DenKr_InfBroker_Msg_Type__KeyEqualValue_CSV = DenKr_InfBroker_Msg_Type__Raw + 1
#//Msg-Subtypes:
DenKr_InfBroker_Msg_SubType__Management__General = 0
DenKr_InfBroker_Msg_SubType__Management__RegConsumerSocket = DenKr_InfBroker_Msg_SubType__Management__General + 1
DenKr_InfBroker_Msg_SubType__Management__RegConsumerCallback = DenKr_InfBroker_Msg_SubType__Management__RegConsumerSocket + 1
DenKr_InfBroker_Msg_SubType__Management__RegProducerSocket = DenKr_InfBroker_Msg_SubType__Management__RegConsumerCallback + 1
DenKr_InfBroker_Msg_SubType__Management__RegProducerCallback = DenKr_InfBroker_Msg_SubType__Management__RegProducerSocket + 1
DenKr_InfBroker_Msg_SubType__Management__RemoveConsumerSocket = DenKr_InfBroker_Msg_SubType__Management__RegProducerCallback + 1
DenKr_InfBroker_Msg_SubType__Management__RemoveConsumerCallback = DenKr_InfBroker_Msg_SubType__Management__RemoveConsumerSocket + 1
DenKr_InfBroker_Msg_SubType__Management__RemoveProducerSocket = DenKr_InfBroker_Msg_SubType__Management__RemoveConsumerCallback + 1
DenKr_InfBroker_Msg_SubType__Management__RemoveProducerCallback = DenKr_InfBroker_Msg_SubType__Management__RemoveProducerSocket + 1
#//  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
#//  -  - CSV-Subtypes  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
DenKr_InfBroker_Msg_SubType__KeyEqualValue_CSV__General = 0
DenKr_InfBroker_Msg_SubType__KeyEqualValue_CSV__int = DenKr_InfBroker_Msg_SubType__KeyEqualValue_CSV__General + 1
DenKr_InfBroker_Msg_SubType__KeyEqualValue_CSV__str = DenKr_InfBroker_Msg_SubType__KeyEqualValue_CSV__int + 1
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------


    
def DennTrisC_C_Connection_Loss__Client():
    printansi(ansi_red,"Error")
    printf(": Lost Connection to C-Program.\n")
    printf("TODO: DennKrementC_C_Connection_Loss\n")
    
    
def DennTrisC_C_Connection_Loss__Server():
    printansi(ansi_red,"Error")
    printf(": Lost Connection to C-Program.\n")
    printf("TODO: DennKrementC_C_Connection_Loss\n")
    
    
    
def Unix_Socket_C_Python_Server():
    try:
        #NOTE: UNIX-Sockets used to connect the Python and the C Program locally.
        #Registration in the abstract namespace (Using a "String" as Address with preceding '\0')
        sock_C_listen = socket(AF_UNIX, SOCK_STREAM)
        sock_C_listen.bind(SOCKET_PYTHON_C)
        # Create a backlog queue for up to 1 connection.
        sock_C_listen.listen(1)    
        # Blocks until a connection arrives. A tuple (connected_socket, None) is returned
        # upon connection. Note we get the first argument and throw away the rest.
        sock_C = sock_C_listen.accept()[0]#Assign the first Connection to use it
        
        # Close it
        sock_C_listen.close()
        del sock_C_listen
        
        return sock_C
    except KeyboardInterrupt:
        pass
    
    
    
def Unix_Socket_C_Python_Connect():
    try:
        #NOTE: UNIX-Sockets used to connect the Python and the C Program locally.
        #Registration in the abstract namespace (Using a "String" as Address with preceding '\0')
        sock_C = socket(AF_UNIX, SOCK_STREAM)
        sock_C.connect(SOCKET_PYTHON_C)
        
        return sock_C
    except KeyboardInterrupt:
        pass
    
    
    
    
def msgsize_to_X_Byte(msgstr,x=MSGLEN_WIDTH_TO_C):
    """Delivers a Byte-Object Back. It contains the length of the given String.\n Second parameter determines the Bit-Width of the returned result. Default 4 Byte if not given.\n If the String-length in Byte-Representation doesn't fit into the wanted Bit-Width the return-Value is a single Byte with '00000000' as Content (i.e. b'\x00')"""
    strlen=len(msgstr)
#     max0=255 # 2^8-1
#     max1=65535 # 2^16-1
#     max2=16777215 # 2^24-1
#     max3=4294967295 # 2^32-1
#     if strlen>max3:
#         #Error: To large
#         return -1
#     elif strlen>max2:
#         return (b'\xstrlen%max0')
#     elif strlen>max1:
#         return (b'\xstrlen%max0')
#     elif strlen>max0:
#         return (b'\xstrlen%max0')
#     else:
    try:
        return (strlen).to_bytes(x, byteorder=ENDIANESS_SEND)
    except OverflowError:
        print("ERROR: Bad Msg-Size Calculation (Size too large)")
        return b"\x00"
    
    
   
    
    
    
    
    
class Msg_Python_C(object):
    instance_counter = 0
    #------------------------------------------------------------------------------------------
    def __init__(self):
        """Explain it!"""
        Msg_Python_C.instance_counter += 1
        """Initialize some Stuff"""
        self.type = 0
        self.subtype = 0
        self.src = 0
        self.len = 0
        self.flags = 0
        self.context = ""
        self.msg = b""
        self._sock=0
    #------------------------------------------------------------------------------------------
    def __del__(self):
        Msg_Python_C.instance_counter -= 1
    #------------------------------------------------------------------------------------------
    def recv(self):
        """Returns: 1 - proper operation. 0 - socket closed. -1 - other socket error"""
        try:
            recv_msg = self._sock.recv(MSGTYPE_WIDTH_TO_C)
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            #print(recv_msg)
            #self.type=self.type.from_bytes(recv_msg,byteorder=ENDIANESS_SEND)
            self.type=self.type.from_bytes(recv_msg,byteorder=sys.byteorder)
            #
            recv_msg = self._sock.recv(MSGSUBTYPE_WIDTH_TO_C)
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            #print(recv_msg)
            #self.subtype=self.subtype.from_bytes(recv_msg,byteorder=ENDIANESS_SEND)
            self.subtype=self.subtype.from_bytes(recv_msg,byteorder=sys.byteorder)
            #
            recv_msg = self._sock.recv(MSGSRC_WIDTH_TO_C)
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            #print(recv_msg)
            #self.src=self.src.from_bytes(recv_msg,byteorder=ENDIANESS_SEND)
            self.src=self.src.from_bytes(recv_msg,byteorder=sys.byteorder)
            #print(self.src)
            #
            recv_msg = self._sock.recv(MSGLEN_WIDTH_TO_C)
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            #print(recv_msg)
            #self.len=self.len.from_bytes(recv_msg,byteorder=ENDIANESS_SEND)
            self.len=self.len.from_bytes(recv_msg,byteorder=sys.byteorder)
            #print(self.len)
            #
            recv_msg = self._sock.recv(MSGFLAGS_WIDTH_TO_C)
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            #print(recv_msg)
            #self.flags=self.flags.from_bytes(recv_msg,byteorder=ENDIANESS_SEND)
            self.flags=self.flags.from_bytes(recv_msg,byteorder=sys.byteorder)
            #
            if self.len==0:
                return 1
            #TODO
            recv_msg = self._sock.recv(self.len)
            # When the socket is closed cleanly, recv unblocks and returns ""
            if not recv_msg:
                print("DenKrement(C-Hub) closed connection")
                return 0
            self.msg = recv_msg
            self.msg_parse_context()
            return 1
        except ConnectionResetError:
            DennTrisC_C_Connection_Loss__Client()
        except ConnectionAbortedError:
            DennTrisC_C_Connection_Loss__Client()
        except KeyboardInterrupt:
            pass
        except UnboundLocalError:
            pass
    def msg_parse_context(self):
        if (self.type == DenKr_InfBroker_Msg_Type__Generic) or (self.type == DenKr_InfBroker_Msg_Type__Request) or (self.type == DenKr_InfBroker_Msg_Type__Raw) or (self.type == DenKr_InfBroker_Msg_Type__KeyEqualValue_CSV):
            temp=self.msg.decode('utf-8')
            self.context, temp = temp.split("\x00",1)
            self.msg = bytes(temp,'UTF-8')
            self.context
    #------------------------------------------------------------------------------------------
    def send(self):
        """Just prepare my variables and then call this one. I use my variables to pack the sending message."""
        """You don't need to set the len & src variables."""
#         sendmsg = self.type.to_bytes(MSGTYPE_WIDTH_TO_C, byteorder=ENDIANESS_SEND)
#         sendmsg = sendmsg + self.subtype.to_bytes(MSGSUBTYPE_WIDTH_TO_C, byteorder=ENDIANESS_SEND)
#         sendmsg = sendmsg + self.src.to_bytes(MSGSRC_WIDTH_TO_C, byteorder=ENDIANESS_SEND)
#         sendmsg = sendmsg + self.len.to_bytes(MSGLEN_WIDTH_TO_C, byteorder=ENDIANESS_SEND)
#         sendmsg = sendmsg + self.flags.to_bytes(MSGFLAGS_WIDTH_TO_C, byteorder=ENDIANESS_SEND)
        #self.len = len(self.msg)+len(self.context)+2 # +1, Null-terminating msg | +1, Null-terminating context
        if 0 < len(self.context):
            self.len = len(self.context)+1
        else:
            self.len = 0
        if 0 < len(self.msg):
            self.len = self.len + len(self.msg)+1
        sendmsg = self.type.to_bytes(MSGTYPE_WIDTH_TO_C, byteorder=sys.byteorder)
        sendmsg = sendmsg + self.subtype.to_bytes(MSGSUBTYPE_WIDTH_TO_C, byteorder=sys.byteorder)
        sendmsg = sendmsg + self.src.to_bytes(MSGSRC_WIDTH_TO_C, byteorder=sys.byteorder)
        sendmsg = sendmsg + self.len.to_bytes(MSGLEN_WIDTH_TO_C, byteorder=sys.byteorder)
        sendmsg = sendmsg + self.flags.to_bytes(MSGFLAGS_WIDTH_TO_C, byteorder=sys.byteorder)
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if 0 < len(self.context):
            if type(self.context) is type("a"):#someString
                sendmsg = sendmsg + bytes(self.context,'UTF-8')
                sendmsg = sendmsg + bytes("\x00",'UTF-8')
                #TODO: Check Null-Termination Consistency
            else:
                print('Please use string for Context.')
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if 0 < len(self.msg):
            if type(self.msg) is type("a"):#someString
                sendmsg = sendmsg + bytes(self.msg,'UTF-8')
                sendmsg = sendmsg + bytes("\x00",'UTF-8')
            elif type(self.msg) is type(b"a"):#someByteArray
                sendmsg = sendmsg + self.msg
                sendmsg = sendmsg + bytes("\x00",'UTF-8')
            else:
                print('Please use string or Byte-Array to send.')
                return -1
        #print(sendmsg)
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self._sock.send(sendmsg)
        return 0
    def prep_msg(self, msgtype, msgsubtype, msgflags, context, msg):
        self.type = msgtype
        self.subtype = msgsubtype
        self.flags = msgflags
        self.context = context
        self.msg = msg
    #------------------------------------------------------------------------------------------
    def set_socket(self, sock):
        self._sock = sock
    #------------------------------------------------------------------------------------------
    def close_socket(self):
        self._sock.close()
    #------------------------------------------------------------------------------------------
    def Debug_print_msg(self):
        print('Type: ', self.type, 'SubType: ', self.subtype, 'Src: ', self.src, 'Size: ', self.len, 'Flags: ', self.flags)
        print('Context: ', self.context)
        print('Msg (Bytes):', self.msg)
    #------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------
    
    
    
    
    