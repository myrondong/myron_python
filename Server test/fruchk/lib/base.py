import logging
import os
import sys
import prettytable as pt
import configparser

"""
    V1.00.10 2021/5/24 author by Myron.
    Copyright (C) 2021 Myron. All Rights Reserved.
"""
fail_int = 30
pass_int = 29
title_int = 28
error_code_int = 27
percentage_int = 26
test_int = 25
copyright_int = 24
table_int = 23


class MyronLog(logging.Logger):

    def __init__(self, path,mode='w'):
        """
        Fuc: log standardization.

        Log levels are title copyright pass fail info warn percent error errorcode and table.

        V1.00.00 2021/5/10 author by Myron.

        Copyright (C) 2021 Myron. All Rights Reserved.

        :param path:log path

        :param mode:log write mode (default is 'w')
        """
        self.log_dll = self._logger(path, mode)
        ss = pt.PrettyTable()
        self.tb = ss

    def _logger(self, log_path, mode):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger

    def _test_dll(self):
        logging.addLevelName(title_int, "TEST")
        self.log_dll.log(title_int, msg=sys.argv[0].split('/')[-1])

    def title_dll(self, detail, times, version='V1.00.00', author='Myron'):
        self._test_dll()
        time = str(times).split('/')[0]

        author = 'by %s' % author
        logging.addLevelName(test_int, "HEAD")
        # msg = detail + ', ' + version + ', ' + times + ', ' + author
        msg = '%s, %s, %s, %s' % (detail, version, times, author)
        len_int = len(msg) + 10

        self.log_dll.log(test_int, msg="-" * len_int)
        self.log_dll.log(test_int, msg="|    " + msg + "    |")
        self.log_dll.log(test_int, msg="-" * len_int)

        self._copyright_dll('Copyright © %s Myron Dong. All rights reserved.' % time)

    def _copyright_dll(self, msg):
        logging.addLevelName(copyright_int, "Copr.")
        self.log_dll.log(copyright_int, msg)

    def pass_dll(self):
        logging.addLevelName(pass_int, "PASS")
        self.log_dll.log(pass_int, "PASS")

    def info_dll(self, msg):
        self.log_dll.log(logging.INFO, msg=msg)

    def error_dll(self, msg):
        self.log_dll.log(logging.ERROR, msg=msg)

    def warn_dll(self, msg):
        self.log_dll.log(logging.WARNING, msg)

    def percent_dll(self, number):
        numbers = -1
        if 0 <= number <= 100:
            numbers = number
        logging.addLevelName(percentage_int, "Percentage")
        self.log_dll.log(percentage_int, numbers)

    def error_code_dll(self, msg):
        logging.addLevelName(error_code_int, "ErrorCode")
        self.log_dll.log(error_code_int, msg)

    def fail_dll(self):
        logging.addLevelName(fail_int, "FAIL")
        self.log_dll.log(fail_int, "FAIL")

    def table_file_names_first(self, list_file_names):
        """
        create table head
        :param list_file_names:
        :return:
        """
        self.tb.field_names = list_file_names

    def table_data_second(self, list_data_items):
        """
        insert table data
        :param list_data_items:
        :return:
        """
        self.tb.add_row(list_data_items)

    def table_dll_third(self, theme="TABLE"):
        """
        print table
        :param theme: table name
        :return:
        """
        logging.addLevelName(table_int, 'TABLE')
        self.log_dll.log(table_int, "%s\n%s" % (theme, self.tb))

    def info_dll_table(self, tite, msg):
        logging.addLevelName(table_int, 'TABLE')
        self.log_dll.log(logging.INFO, msg="%s\n%s" % (tite, msg))

