from common.get_url import GetUrl
from common.get_path import GetPath
from common.find_element import FindElement, browser
import time
import threading
import configparser

manager_url = GetUrl().get_admin_url()

from common.select_environment import Select

select = Select().select()


class ManagerLogin(FindElement):
    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    conf_ptah = GetPath().get_conf_path('username.ini')
    conf.read(conf_ptah, encoding='utf-8')
    if select == '1':
        zj_manage_name = conf.get('test_name', 'zj_manage_name')
        lx_manage_name = conf.get('test_name', 'lx_manage_name')
        yf_manage_name = conf.get('test_name', 'yf_manage_name')
        manage_pwd = conf.get('test_name', 'manage_pwd')
    elif select=='0':
        zj_manage_name = conf.get('name', 'zj_manage_name')
        lx_manage_name = conf.get('name', 'manage_name')
        yf_manage_name = conf.get('name', 'manage_name')
        manage_pwd = conf.get('name', 'manage_pwd')
    mutex.release()

    all_input = ('class name', 'layui-input')#管理端登录页面所有文本框定位
    all_inputs = ('class name', 'el-input__inner')
    login_button = ('id', 'login-btn')#管理端登录页面登录按钮定位
    login_buttons = ('class name', 'el-button')
    select_elements = ('class name', 'el-select-dropdown__item')

    def zj_manager_login(self, name=zj_manage_name, password=manage_pwd):
        elements = self.find_elements(self.all_input)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        self.click(self.login_button)
        time.sleep(3)

    def lx_manager_login(self, name=lx_manage_name, password=manage_pwd):
        elements = self.find_elements(self.all_inputs)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        elements[2].click()
        time.sleep(1)
        select_elements = self.find_elements(self.select_elements)
        select_elements[0].click()
        elements[3].send_keys('abc')
        self.find_elements(self.login_buttons)[0].click()
        time.sleep(1)

    def yf_manager_login(self, name=yf_manage_name, password=manage_pwd):
        elements = self.find_elements(self.all_inputs)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        elements[2].click()
        time.sleep(1)
        select_elements = self.find_elements(self.select_elements)
        select_elements[0].click()
        elements[3].send_keys('abc')
        self.find_elements(self.login_buttons)[0].click()
        time.sleep(1)


if __name__ == '__main__':
    driver = browser()
    browser = ManagerLogin(driver)
    browser.open_url(manager_url)
    browser.yf_manager_login()
