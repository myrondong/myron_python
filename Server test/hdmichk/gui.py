#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import time
import threading
import os
import serialport
import keyboard
import sys

root = tkinter.Tk()


def quitfull():
    root.destroy()
    # exit(0)


def hook():
    keyboard.add_hotkey('ctrl+c', quitfull)
    keyboard.wait()


def kill_gui():
    th = threading.Thread(target=hook)
    th.setDaemon(True)  # 守护线程
    th.start()


def loop_windows():
    root = tkinter.Tk()
    root.configure(bg='white')
    root.attributes("-fullscreen", True)
    root.mainloop()


def show_wind():
    th = threading.Thread(target=loop_windows)
    th.setDaemon(True)  # 守护线程
    th.start()


def input_serial_cmd(ser, cmd1, cmd2):
    for i in range(3):
        res, status = serialport.PortStr(ser, cmd1, cmd2)
        if status:
            return res, status
    return "error", False


def check_hdmi(ser):
    i = 0
    while True:
        time.sleep(1)
        i = i + 1
        print('---')
        res, status = serialport.PortStr2(ser, 'CBHDMIRESULT\r', 'CBHDMIRESULT OK', 'CBHDMIRESULT CHECKING')
        if status:
            return res, status
        elif i == 30:
            return res, status


def run(ser, status):
    if status:
        print('OPEN HDMI HTP...')
        res, status = input_serial_cmd(ser, 'HDMI1\r\r', 'HDMI1 OK')
        if status:
            print('HDMI Checking...')
            res, status = check_hdmi(ser)
            time.sleep(1)
            if not status:
                ser.close()
                print('HDMI TEST FAIL')
                res, status = input_serial_cmd(ser, 'HDMI0\r\r', 'OK')
                sys.exit(1)
            print('CLOSE HDMI HTP...')
            res, status = input_serial_cmd(ser, 'HDMI0\r\r', 'OK')
            time.sleep(1)
            ser.close()
            print('HDMI TEST PASS')
        else:
            ser.close()
            print('HDMI TEST FAIL')
            sys.exit(1)
    else:
        ser.close()
        print('HDMI TEST FAIL')
        sys.exit(1)




if __name__ == '__main__':
    kill_gui()
    ser, status = serialport.SelectPort1('QueryCBHDMI\r', 'QUERYCBHDMI OK')
    print('Open white window')
    show_wind()
    run(ser, status)
    quitfull()
    sys.exit(0)
