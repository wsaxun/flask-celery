import subprocess
import logging
from datetime import datetime
import os

logger = logging.getLogger('debug')

def cur_date():
    '''get year and month'''
    d = datetime.now()
    return '%4d%02d'%(d.year,d.month)

def cur_day():
    '''get year month day'''
    d = datetime.now()
    return '%4d%02d%02d'%(d.year,d.month,d.day)

def cur_timestamp():
    '''get year month、day、hour、minute、second、second'''
    d = datetime.now()
    return '%4d%02d%02d%02d%02d%02d'%(d.year,d.month,d.day,d.hour,d.minute,d.second)

def fetch_log_file(root,file_base_name):
    '''get log file name'''
    sub_log_folder = cur_date()
    log_dir_path = os.path.abspath(os.path.join(root,'logs/',sub_log_folder))
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
    log_file = os.path.join(log_dir_path,file_base_name)
    return log_file

def setup_logger(root,file_base_name,level=logging.DEBUG,enable_logger=True):
    '''set logger'''
    if not enable_logger:
        return
    file_name = fetch_log_file(root,file_base_name)
    file_handler = logging.FileHandler(file_name,mode='a',encoding='utf-8',delay=False)
    log_format = '%(asctime)s %(levelname)s:%(message)s'
    debug_formatter = logging.Formatter(log_format)
    file_handler.setFormatter(debug_formatter)
    global logger
    logger.setLevel(level)
    logger.addHandler(file_handler)

if __name__ == '__main__':
    pass
