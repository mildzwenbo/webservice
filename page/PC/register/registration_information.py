"""
@author:fei
@date:2018-7-4
@brief:注册页面，输入注册信息
"""

import time


from page.PC.register.register_confirm import RegisterConfirm, browser, pc_url, register_confirm_url


class RegistrationInformation(RegisterConfirm):
    """注册信息页面的元素操作"""

    # 所有的输入框，列表中第三个为客户名称，第四个为手机号，第五个为验证码
    info_inputs_loc = ('class name', 'el-input__inner')

    # 勾选网络协议按钮
    info_select_loc = ('class name', 'el-checkbox__inner')

    # 网络协议按钮
    info_agreement_loc = ('class name', 'el-button--text')

    # 下一步按钮,列表中第三个
    info_next_step_loc = ('class name', 'el-button--medium')

    def info_personal_not_enter(self):
        """
        个人注册不输入任何信息，勾选网络协议点击下一步
        :return:
        """
        self.individual_investor('1')
        time.sleep(1)
        self.click(self.info_select_loc)
        time.sleep(1)
        self.find_elements(self.info_next_step_loc)[2].click()

    def info_personal_input_info(self, name, phone):
        """
        个人用户填写信息
        :return:
        """
        self.individual_investor('1')
        time.sleep(1)
        self.find_elements(self.info_inputs_loc)[2].send_keys(name)
        self.find_elements(self.info_inputs_loc)[3].send_keys(phone)
        self.find_elements(self.info_inputs_loc)[4].send_keys('AAAA')
        self.click(self.info_select_loc)
        time.sleep(1)
        self.find_elements(self.info_next_step_loc)[2].click()

    def info_institutions_not_enter(self):
        """
        机构注册不输入任何信息
        :return:
        """
        self.individual_investor('2')
        time.sleep(1)
        self.click(self.info_select_loc)
        time.sleep(1)
        self.find_elements(self.info_next_step_loc)[2].click()

    def info_institutions_input_info(self, institutions_name, name, phone):
        """
        输入信息
        :param institutions_name:
        :param name:
        :param phone:
        :return:
        """
        self.individual_investor('2')
        time.sleep(1)
        self.find_elements(self.info_inputs_loc)[0].send_keys(institutions_name)
        self.find_elements(self.info_inputs_loc)[1].send_keys(name)
        self.find_elements(self.info_inputs_loc)[3].send_keys(phone)
        self.find_elements(self.info_inputs_loc)[4].send_keys("AAAA")
        self.click(self.info_select_loc)
        time.sleep(1)
        self.find_elements(self.info_next_step_loc)[2].click()


if __name__ == '__main__':
    browser = browser()
    r = RegistrationInformation(browser)
    r.open_url(register_confirm_url)
    time.sleep(1)
    r.info_institutions_input_info('自动化机构用户1', 'test', '13944096337')
