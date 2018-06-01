"""
@author:fei
@date：2018-5-23
@brief:读取配置文件
"""

import configparser
import threading
import os


class GetUrl(object):

    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    conf_path = os.path.join(os.path.join(path, 'config'), 'url.ini')
    conf.read(conf_path, encoding='utf-8')
    if conf.get('select', 'select') == '1':
        admin_url = conf.get('TESTURL', 'SafeManager')
        pc_url = conf.get('TESTURL', 'pc_url')
    else:
        admin_url = conf.get('URL', 'SafeManager')
        pc_url = conf.get('URL', 'pc_url')
    mutex.release()

    def get_admin_url(self):
        return self.admin_url

    def get_pc_url(self):
        return self.pc_url


if __name__ == '__main__':
    pc = GetUrl().get_pc_url()
    ad = GetUrl().get_admin_url()
    print(pc)
    print(ad)

