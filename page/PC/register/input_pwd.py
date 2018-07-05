"""
@author:fei
@date:2018-7-5
@brief:注册也买最后对密码的测试用例
"""

import time

from page.PC.register.code import Code, browser, pc_url, register_confirm_url


class InputPwd(Code):
    """注册过程中输入密码的元素操作"""

    # 输入密码和再次输入密码输入框，列表中的第七个和第八个
    pwd_input_pwd_loc = ('class name', 'el-input__inner')

    # 确定按钮,列表中的第三个
    # __pwd_confirm_loc = ('class', 'el-button--primary')
    pwd_confirm_loc = ('css', '#app > div > form > div.el-form-item.el-form-item--feedback.el-form-item--medium > div > button:nth-child(2)')

    def pwd_input(self, pwd1='', pwd2=''):
        """
        输入第一次密码和第二次密码，点击确定按钮
        :param pwd1: 第一次输入密码
        :param pwd2: 第二次输入密码
        :return:
        """
        self.code_input()
        time.sleep(1)
        self.find_elements(self.pwd_input_pwd_loc)[6].send_keys(pwd1)
        self.find_elements(self.pwd_input_pwd_loc)[7].send_keys(pwd2)
        time.sleep(1)
        # self.find_elements(self.__pwd_confirm_loc)[2].click()
        self.click(self.pwd_confirm_loc)


if __name__ == '__main__':
    driver = browser()
    p = InputPwd(driver)
    p.open_url(pc_url)
    p.open_url(register_confirm_url)
    time.sleep(1)
    p.pwd_input()