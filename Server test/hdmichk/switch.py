
import subprocess
import serialport
import time
import logging
import os,sys


    
def SwitchTest():
  ser,status = serialport.SelectPort1('QueryTypeC\r', 'QUERYTYPEC OK')
  time.sleep(1)
  if status:
    a,b = serialport.PortStr(ser, 'Ch12USB1\r', 'CH12USB1 OK')
    if b:    
      time.sleep(1)
      usb_status = test_usb()
      if not usb_status:
        print("TypeC Test FAIL")      
        sys.exit(1)
  time.sleep(1)
  a,b = serialport.PortStr(ser, 'Ch12ABSwitch\r', 'CH12ABSWITCH OK')
  time.sleep(1)
  if b:  
    ser1,status1 = serialport.SelectPort1('QueryTypeC\r', 'QUERYTYPEC OK')
    time.sleep(1)
    if status1:
      a,b = serialport.PortStr(ser1, 'Ch12USB1\r', 'CH12USB1 OK')
      time.sleep(1)
      if b:
        usb_status = test_usb()
        if not usb_status:
          print("TypeC Test FAIL")
          sys.exit(1)
        time.sleep(1)  
        serialport.PortStr(ser1, 'Ch12USB0\r', 'CH12USB1 OK') 
        print("TypeC Test PASS")
        sys.exit(0)
  print("TypeC Test FAIL")      
  sys.exit(1)


def system_popen(cmd):
  p = subprocess.Popen(cmd,stdout =subprocess.PIPE,shell=True)
  out, error = p.communicate()
  outs= out.decode('utf-8')
  print(outs)
  if p.returncode != 0: return outs,False
  return outs,True

def test_usb():
  usb2_out,usb2_flag = system_popen("./usb.exe -t:2 -c:1")
  time.sleep(1)  
  usb3_out,usb3_flag = system_popen("./usb.exe -t:3 -c:1")
  if  usb2_flag and usb3_flag:
    if usb2_out.find("Test Result : PASS") !=-1 and usb2_out.find("Test Result : PASS"):
      return True
    else:

      return False
  else:
    return False
  
if __name__ == '__main__':
  SwitchTest()
         
