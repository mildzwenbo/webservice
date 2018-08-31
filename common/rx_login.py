"""
@author:
@date:
@brief:睿歆控制台登录
"""

from common.find_element import FindElement, browser
from common.get_url import GetUrl
import configparser
import threading
import os
import time

from common.select_environment import Select

select = Select().select()
url = GetUrl().rx_url


class RxLogin(FindElement):
    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    conf_path = os.path.join(os.path.join(path, 'config'), 'username.ini')
    conf.read(conf_path, encoding='utf-8')
    if select == '1':
        rx_name = conf.get('test_name', 'rx_name')
        rx_pwd = conf.get('test_name', 'rx_pwd')
    elif select == '0':
        rx_name = conf.get('name', 'rx_name')
        rx_pwd = conf.get('name', 'rx_pwd')
    mutex.release()

    name_loc = ('css', '#username')
    password_loc = ('css', '#password')
    verify_loc = ('css', '#verifyCode')
    login_button_loc = ('css', '#login_btn')

    def rx_login(self, name=rx_name, pwd=rx_pwd):
        self.send_keys(self.name_loc, name)
        self.send_keys(self.password_loc, pwd)
        self.send_keys(self.verify_loc, 'j')
        self.click(self.login_button_loc)
        time.sleep(2)


if __name__ == '__main__':
    driver = browser()
    h = RxLogin(driver)
    h.open_url(url)
    h.rx_login()
