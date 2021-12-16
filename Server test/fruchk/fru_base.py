#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess


def run_cmd(cmd):
    #    m_logger.debug(cmd)
    print(cmd)
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    while p.poll() is None:
        pass
    out, err = p.communicate()
    #    m_logger.debug(str(out)+' '+str(p.returncode))
    print(out, p.returncode)
    return out, p.returncode


def ipmi_cmd(ipmi_env, arg):
    if ipmi_env["ip"] is None:
        command = "ipmitool "
    else:
        command = "ipmitool -H %s -U %s -P %s -I lanplus " % (ipmi_env["ip"], ipmi_env["user"], ipmi_env["passwd"])

    command += ' '.join(arg)
    return run_cmd(command)


def check_ipmitool():
    try:
        output = run_cmd("ipmitool -V")
        if (output[1] == 0):
            return True
    except:
        print("ipmitool is not installed; " \
              "Please install ipmitool !!!")
        return False