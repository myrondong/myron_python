
#from cros.factory.utils import type_utils

import serial
import time
import glob
import logging

# Fail if does not find the port
def SelectPort(Query_instruction, Query_reply_instruction, baudrate = 115200):
#    ports = ["/dev/ttyUSB0","/dev/ttyUSB1","/dev/ttyUSB2","/dev/ttyUSB3","/dev/ttyUSB4",
#             "/dev/ttyUSB5","/dev/ttyUSB6","/dev/ttyUSB7","/dev/ttyUSB8","/dev/ttyUSB9"]
    ports=glob.glob('/dev/ttyUSB*')
    for port in ports:
        try:
            ser = serial.Serial(port, baudrate, timeout = 0.5)
            logging.info('The currently open serial port is %s'%port)
            ser.write(Query_instruction.encode('gbk'))
            reply_instruction = ser.readline()
            reply_instruction = str(reply_instruction)
            reply_instruction = reply_instruction[2:-3]  
            logging.info('The currently read return is %s' %reply_instruction)
            print('The currently read return is %s' %reply_instruction)
            if Query_reply_instruction == reply_instruction:
              logging.info('The tested serial port is connected successfully!')
              return ser,True
            else:
                logging.info('The current serial port is incorrect, will continue to search for the correct serial port!')
        except OSError:
            logging.info('No such file or directory: %s ' %port)
    logging.info('Port Error!')  
    return 'Port Error!',True


# Loop detect the port untill find the port
def SelectPort1(Query_instruction, Query_reply_instruction, baudrate = 115200):
#    ports=glob.glob('/dev/ttyUSB*')
    while True:
      time.sleep(0.1)
      ports=glob.glob('/dev/ttyUSB*')
      for port in ports:
          try:
              ser = serial.Serial(port, baudrate, timeout = 0.5)
              logging.info('The currently open serial port is %s' %port)
              ser.write(Query_instruction.encode('gbk'))
              reply_instruction = ser.readline()
              reply_instruction = str(reply_instruction)
              reply_instruction = reply_instruction[2:-3]              
              logging.info('The currently read return is %s' % reply_instruction)
              print('The currently read return is %s' %reply_instruction)
              if Query_reply_instruction == reply_instruction:
                logging.info('The tested serial port is connected successfully!')
                return ser,True
              else:
                  logging.info('The current serial port is incorrect, will continue to search for the correct serial port!')
          except OSError:
              logging.info('No such file or directory: %s '%port)
def PortHex(ser, send_message, return_message = None):
    ser.write(send_message.decode('hex'))
    if return_message != None:
        read_message = ser.readline()
        logging.info('Got %r' ,read_message)
        if return_message == read_message:
            return read_message
        else:
            ser.close()
            logging.info('Test Error!')
    else:
        logging.info('No return!')

# No retrun when not get the right message
def PortStr(ser, send_message, return_message = None):
    ser.write(send_message.encode('gbk'))
    if return_message != None:
        read_message = ser.readline()
        read_message = str(read_message)
        read_message = read_message[2:-3] 
        logging.info('Got %s' %read_message)
        print('Got %s' %read_message)
        if return_message == read_message:
            return read_message,True
        else:
            logging.info('Test Error!')
            return 'Test Error!',False
    else:
        logging.info('No return!')
        return 'No return!',False

def PortStr2(ser, send_message, return_message,return_message2):
    ser.write(send_message.encode('gbk'))
    if return_message != None:
        read_message = ser.readline()
        read_message = str(read_message)
        read_message = read_message[2:-3] 
        logging.info('Got %s' %read_message)
        print('Got %s' %read_message)
        if return_message == read_message:
            return read_message,True
        elif return_message2 ==read_message:
            return read_message,False
        else:

            #ser.close()
            logging.info('Test Error!')
            return 'Test Error!',False
    else:
        logging.info('No return!')
        return 'No return!',False

# Retrun '' when not get the right message 
def PortStr1(ser, send_message, return_message = None):
    ser.write(send_message.encode('gbk'))
    if return_message != None:
        read_message = ser.readline()
        read_message = str(read_message)
        read_message = read_message[2:-3] 
        logging.info('Got %r' ,read_message)
        print('Got %r' ,read_message)
        if return_message == read_message:
            return read_message
        else:
            return ''
    else:
        logging.info('No return!')

