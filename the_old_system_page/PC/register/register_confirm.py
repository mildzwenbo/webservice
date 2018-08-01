"""
@author:fei
@date:2018-7-4
@brief:登录页面点击"注册"进入到的确认页面
"""


from common.pc_login import PCLogin, browser, pc_url
from common.get_url import GetUrl


import time

register_confirm_url = GetUrl().pc_url + r'#/signUpindex'


class RegisterConfirm(PCLogin):
    """注册页面的确定页面多有元素的操作"""

    # 选择类型，列表中第一个为个人，第二个为机构
    select_type_loc = ('class name', 'el-radio')

    # 选择基金管理人对话框
    fund_manager_loc = ('class name', 'el-input__inner')

    # 选择的基金管理人
    select_fund_manager_loc = ('class name', 'el-select-dropdown__item')

    # 下一步按钮
    next_step_loc = ('class name', 'el-button--primary')

    # 登录按钮
    login_loc = ('class name', 'el-button--text')

    def individual_investor(self, select_type):
        """
        点击个人投资者或者机构投资者，点击下一步
        :return:
        """
        if select_type == '1':
            self.find_elements(self.select_type_loc)[0].click()
        else:
            self.find_elements(self.select_type_loc)[1].click()
        self.click(self.fund_manager_loc)
        time.sleep(1)
        self.click(self.select_fund_manager_loc)
        self.click(self.next_step_loc)

    def login_click(self):
        """
        点击确认按钮
        :return:
        """
        self.click(self.login_loc)

    def do_not_enter_the_fund_manager(self):
        """
        不输入基金管理人的情况下点击下一步
        :return:
        """
        self.find_elements(self.select_type_loc)[0].click()
        self.click(self.next_step_loc)


if __name__ == '__main__':
    driver = browser()
    r = RegisterConfirm(driver)
    r.open_url(register_confirm_url)
    time.sleep(2)
    r.individual_investor('2')
