"""
@author:fei
@date:2018-7-6
@brief:注册后完事基本信息与风险评定等级页面
"""

import time

from common.get_url import GetUrl
from common.pc_login import PCLogin, browser
from page.PC.register.input_pwd import InputPwd, pc_url, register_confirm_url

personage_basic_info_url = GetUrl().get_pc_url() + r'#/improveIndividualCusInfo?customerGuid=9a605082-b669-4153-9577-a63a3a327758&customerType=CUSTOMERTYPE%2FINDIVIDUAL&institutionGuid=e31f504f-a106-4e0a-973b-311732c15e1c'


class PersonageBasicInfo(InputPwd):
    """注册后，完善基本信息页面元素的操作"""

    # 确认勾选
    basic_pledge_loc = ('class name', 'el-checkbox__inner')
    # 下一步按钮，下标为1
    basic_next_step_loc = ('class name', 'el-button--medium')
    # 证件类型选择，下标为2
    basic_select_type_button_loc = ('class name', 'el-input__inner')
    #选择不同的类型
    basic_select_type_loc = ('class name', 'el-select-dropdown__item')
    # 身份证输入框
    basic_identity_input_loc = ('id', 'id-x-sfz')

    def basic_next_step_click(self):
        """
        什么都不填写，直接点击下一步
        :return:
        """
        self.click(self.basic_pledge_loc)
        self.js_scroll_end(0, 2000)
        time.sleep(1)
        self.click(self.basic_next_step_loc)

    def basic_inputs(self):
        """
        只选择了证件类型
        :return:
        """
        self.find_elements(self.basic_select_type_button_loc)[2].click()
        time.sleep(1)
        self.find_elements(self.basic_select_type_loc)[2].click()

    def basic_identity(self):
        """
        选择了身份证，输入不正确的格式
        :return:
        """
        self.find_elements(self.basic_select_type_button_loc)[2].click()
        time.sleep(1)
        self.find_elements(self.basic_select_type_loc)[0].click()
        self.send_keys(self.basic_identity_input_loc, 'bbb')

    def basic_correct_info(self):
        """
        输入正确的信息，到点击下一步
        :return:
        """
        self.click(self.basic_pledge_loc)
        self.find_elements(self.basic_select_type_button_loc)[2].click()
        time.sleep(1)
        self.find_elements(self.basic_select_type_loc)[3].click()
        self.send_keys(self.basic_identity_input_loc, 'bbb')
        time.sleep(1)
        self.click(self.basic_next_step_loc)


if __name__ == '__main__':
    browser = browser()
    a = PersonageBasicInfo(browser)
    a.open_url(personage_basic_info_url)
    time.sleep(1)
    a.basic_correct_info()

