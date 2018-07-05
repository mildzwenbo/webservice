"""
@author:fei
@date:2018-7-5
@brief:注册页面的获取验证码
"""

from page.PC.register.registration_information import RegistrationInformation, pc_url, register_confirm_url, browser
from common.redis_client import RedisClient
import random


import time


class Code(RegistrationInformation):
    """获取验证码页面"""

    # 短信信息输入框，列表中第五个
    code_input_loc = ('class name', 'el-input__inner')
    # 获取验证码按钮
    code_get_code_loc = ('class name', 'el-button--primary')
    # 下一步按钮，列表中第三个
    code_next_step_loc = ('class name', 'el-button--medium')

    r = RedisClient()

    each = random.randint(1000, 9999)
    phone = '1290000' + str(each)

    def code_input(self, name='test', phone=phone, error_code='2'):
        """
        机构和个人的短信验证一致
        :param phone:电话号码
        :param name:个人用户的名称
        :param error_code:0为输入错误的验证码，1为不输入验证码， 2为输入正确的验证码
        :return:
        """
        time.sleep(1)
        self.info_personal_input_info(name, phone)
        time.sleep(2)

        if error_code == '0':
            self.find_elements(self.code_input_loc)[5].send_keys('000000')
        elif error_code == '1':
            pass
        else:
            self.find_elements(self.code_get_code_loc)[0].click()
            time.sleep(1)
            code = self.r.get_code(phone)
            self.find_elements(self.code_input_loc)[5].send_keys(code)
        time.sleep(1)
        self.find_elements(self.code_next_step_loc)[2].click()


if __name__ == '__main__':
    driver = browser()
    c = Code(driver)
    c.open_url(pc_url)
    c.open_url(register_confirm_url)
    time.sleep(1)
    c.code_input('13944096337')


