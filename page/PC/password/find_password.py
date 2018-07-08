"""
@author:xin
@date:2018-7-5
@brief:投资者PC端：登录页面-找回密码
"""

import time
from common.pc_login import PCLogin, browser
from common.redis_client import RedisClient

from common.get_url import GetUrl
pc_url = GetUrl().get_pc_url() + '#/forgotPassword'


class ForgotPassword(PCLogin):
    text_block = ('class name', 'el-input__inner')  # 页面所有文本框定位
    all_investor = ('class name', 'el-select-dropdown__item')  # 投资者类型下拉框信息定位
    next_step = ('class name', 'el-button--medium')  # 页面下一步按钮定位

    def change_password(self, phone, investor):
        input_textbox = self.find_elements(self.text_block)
        drop_down = self.find_elements(self.all_investor)
        next_button = self.find_elements(self.next_step)
        input_textbox[0].send_keys(phone)
        time.sleep(1)
        input_textbox[1].click()
        if investor == '1':
            drop_down[0].click()
            time.sleep(1)
            input_textbox[2].click()
            self.find_elements(self.all_investor)[3].click()
            time.sleep(1)
            input_textbox[4].send_keys('AAAA')
            next_button[1].click()
        elif investor == '2':
            drop_down[1].click()
            time.sleep(1)
            input_textbox[2].click()
            self.find_elements(self.all_investor)[3].click()
            input_textbox[3].click()
            self.find_elements(self.all_investor)[5].click()
            input_textbox[4].send_keys('AAAA')
            next_button[1].click()
        else:
            drop_down[2].click()
            time.sleep(1)
            input_textbox[2].click()
            self.find_elements(self.all_investor)[3].click()
            input_textbox[3].click()
            self.find_elements(self.all_investor)[4].click()
            input_textbox[4].send_keys('AAAA')
            next_button[1].click()

    def input_phone(self, number):
        # 输入手机号码
        self.find_elements(self.text_block)[1].send_keys(number)

    def select_personage_investor(self):
        # 选择个人投资者
        self.find_elements(self.text_block)[1].click()
        self.find_elements(self.all_investor)[0].click()

    def select_organization_investor(self):
        # 选择机构投资者
        self.find_elements(self.text_block)[1].click()
        self.find_elements(self.all_investor)[1].click()

    def select_investor(self):
        # 选择个人、产品投资者
        self.find_elements(self.text_block)[1].click()
        self.find_elements(self.all_investor)[2].click()

    def select_custodian(self):
        """选择基金管理人"""
        self.find_elements(self.text_block)[2].click()
        self.find_elements(self.all_investor)[3].click()

    def select_organization_name(self):
        """选择机构投资者名称"""
        self.find_elements(self.text_block)[2].click()
        self.find_elements(self.all_investor)[5].click()

    def select_product_name(self):
        """选择机构投资者名称"""
        self.find_elements(self.text_block)[2].click()
        self.find_elements(self.all_investor)[4].click()

    def input_verify(self, code='AAAA'):
        """输入验证码"""
        self.find_elements(self.text_block)[4].send_keys(code)

    def click_next_step(self):
        """点击页面下一步按钮"""
        self.find_elements(self.next_step)[1].click()

    def input_phone(self, number):
        """输入手机号码"""
        self.find_elements(self.text_block)[0].send_keys(number)

    def input_get_code(self, phone):
        """获取正确的验证码"""
        self.find_elements(self.next_step)[0].click()
        time.sleep(1)
        code = RedisClient()
        number = code.get_code(phone)
        self.find_elements(self.text_block)[5].send_keys(number)

    def new_password(self, pwd):
        """输入新的密码"""
        self.find_elements(self.text_block)[6].send_keys(pwd)

    def confirm_password(self, pwd):
        """输入再次输入新的密码"""
        self.find_elements(self.text_block)[7].send_keys(pwd)






if __name__ == '__main__':
    driver = browser()
    f = ForgotPassword(driver)
    f.open_url(pc_url)
    f.input_get_code('15822816936')







