import datetime
import subprocess
import logging, sys

Project = "H4JZD_4BP"

dic_all = {}
dic_std = {
    'time_std': datetime.datetime.now(),

}
def _logger(log_path, mode):
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


log = _logger('test.log', 'w')


def hex_to_str(char_hex):

    str_int = '0x%s' %char_hex
    try:
        return chr(int(str_int,16))
    except:
        log.info('convert ASCII code error')
        sys.exit(1)


def ipmi_cmd(cmd):
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        log.info('cmd execute error')
        sys.exit(1)
    out = str(out.decode('utf-8')).strip()
    return out


def get_dic_info(cmd,name):
    str_out = ipmi_cmd(cmd)
    list_hex_char = str_out.split(' ')
    str_back = None
    for item_char in list_hex_char:
        str_back = str_back + hex_to_str(item_char)
    if len(str_back) > 2:
        dic_all[name] = str_back
    else:
        log.info('execute cmd error')

if __name__ == '__main__':
