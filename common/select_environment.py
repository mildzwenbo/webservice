"""
@author:fei
@date:2018-08-30
@brief:判断环境是那个环境
"""

import threading
import configparser
from common.get_path import GetPath

class Select():

    def select(self):
        each = GetPath()
        mysql_conf_path = each.get_conf_path('select.ini')
        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        conf = configparser.ConfigParser()
        conf.read(mysql_conf_path, encoding='utf-8')
        select = conf.get('select', 'select')
        mutex.release()
        return select


if __name__ == '__main__':
    a = Select().select()
    print(a)