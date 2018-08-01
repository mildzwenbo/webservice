"""
@author:fei
@date:2018-08-01
@brief:登录页面所有元素的测试用例
"""


import time

from common.find_element import FindElement, browser
from common.get_url import GetUrl


login_url = GetUrl().get_admin_url() + r'#/login'


class Login(FindElement):
    """登录页面的所有元素的定位以及操作"""

    #登录页面所有输入框元素定位，0手机号， 1密码， 2所属机构， 3验证码
    all_input_loc = ('class name', 'el-input__inner')

    # 登录和重置按钮, 0登录， 1重置
    buttons_loc = ('class name', 'el-button')

    #所属的机构
    select_elements = ('class name', 'el-select-dropdown__item')


    def no_input(self):
        self.find_elements(self.buttons_loc)[0].click()

    def login(self):
        """
        正常登录
        :return:
        """
        input_elements = self.find_elements(self.all_input_loc)
        input_elements[0].send_keys('13888888888')
        input_elements[1].send_keys('123456')
        input_elements[2].click()
        time.sleep(1)
        self.find_elements(self.select_elements)[0].click()
        input_elements[3].send_keys('abc')
        self.find_elements(self.buttons_loc)[0].click()

    def agency_disabled_login(self):
        """
        机构已经停用登录
        :return:
        """
        input_elements = self.find_elements(self.all_input_loc)
        input_elements[0].send_keys('13888888888')
        input_elements[1].send_keys('123456')
        input_elements[2].click()
        time.sleep(1)
        self.find_elements(self.select_elements)[1].click()
        input_elements[3].send_keys('abc')
        self.find_elements(self.buttons_loc)[0].click()

    def reset_click(self):
        """点击重置按钮，清空所有输入"""
        input_elements = self.find_elements(self.all_input_loc)
        input_elements[0].send_keys('13888888888')
        input_elements[1].send_keys('123456')
        input_elements[2].click()
        time.sleep(1)
        self.find_elements(self.select_elements)[0].click()
        input_elements[3].send_keys('abc')
        self.find_elements(self.buttons_loc)[1].click()





if __name__ == '__main__':
    driver = browser()
    l = Login(driver)
    l.open_url(login_url)
    time.sleep(1)
    l.reset_click()

