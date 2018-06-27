from common.get_url import GetUrl
from common.get_path import GetPath
from common.find_element import FindElement, browser
import time
import threading
import configparser

manager_url = GetUrl().get_admin_url()


class ManagerLogin(FindElement):
    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    conf_ptah = GetPath().get_conf_path('username.ini')
    conf.read(conf_ptah, encoding='utf-8')
    if conf.get('select', 'select') == '1':
        manage_name = conf.get('name', 'manage_name')
        manage_pwd = conf.get('name', 'manage_pwd')
    else:
        manage_name = conf.get('name', 'manage_name')
        manage_pwd = conf.get('name', 'manage_pwd')
    mutex.release()

    all_input = ('class name', 'layui-input')#管理端登录页面所有文本框定位
    login_button = ('id', 'login-btn')#管理端登录页面登录按钮定位

    def manager_login(self, name=manage_name, password=manage_pwd):
        elements = self.find_elements(self.all_input)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        self.click(self.login_button)
        time.sleep(3)


if __name__ == '__main__':
    driver = browser()
    browser = ManagerLogin(driver)
    browser.open_url(manager_url)
    browser.manager_login()