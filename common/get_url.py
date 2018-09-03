"""
@author:fei
@date：2018-5-23
@brief:读取配置文件
"""

import configparser
import threading
import os

from common.select_environment import Select

select = Select().select()



class GetUrl(object):

    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    conf_path = os.path.join(os.path.join(path, 'config'), 'url.ini')
    conf.read(conf_path, encoding='utf-8')
    if select == '1':
        manage_url = conf.get('TESTURL', 'SafeManager')
        pc_url = conf.get('TESTURL', 'pc_url')
        rx_url = conf.get('TESTURL', 'rx_url')
    elif select == '0':
        manage_url = conf.get('URL', 'SafeManager')
        pc_url = conf.get('URL', 'pc_url')
        rx_url = conf.get('URL', 'rx_url')
    mutex.release()

    def get_admin_url(self):
        return self.manage_url

    def get_pc_url(self):
        return self.pc_url

    def get_rx_url(self):
        return self.rx_url


if __name__ == '__main__':
    pc = GetUrl().get_pc_url()
    ad = GetUrl().get_admin_url()
    print(pc)
    print(ad)

