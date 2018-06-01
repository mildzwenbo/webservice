"""
@author:fei
@date:2018-5-28
@brief:PC端登录页面所有元素的定位及其操作
"""

from common.find_element import FindElement, browser
from common.get_url import GetUrl


pc_url = GetUrl().get_pc_url() + '#/manlogin'


class PCLogin(FindElement):

    login_elements_loc = ('class name', 'el-input__inner') #所有的输入框
    retail_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')  #个人投资者
    institution_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]')  #机构投资者
    client_investor_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[3]')  #客户投资者

    organization_loc = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li') #基金公司的定位

    object_loc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span')#投资者选择

    button_login_loc = ('css', '#app > div > form > div:nth-child(9) > div > button > span')#登录按钮

    retrieve_password_loc = ('css', '#app > div > form > div:nth-child(8) > button') #找回密码

    def input_name(self, name):
        """输入用户名"""
        elements = self.find_elements(self.login_elements_loc)
        elements[0].send_keys(name)

    def input_password(self, password):
        """输入密码"""
        elements = self.find_elements(self.login_elements_loc)
        elements[2].send_keys(password)

    def investor_type_click(self):
        """点击投资者类型"""
        elements = self.find_elements(self.login_elements_loc)
        elements[3].click()

    def retail_click(self):
        """选择个人投资者"""
        self.click(self.retail_loc)

    def institution_click(self):
        """选中机构投资者"""
        self.click(self.institution_loc)

    def client_investor_click(self):
        """选客户构投资者"""
        self.click(self.client_investor_loc)

    def fund_manager_click(self):
        """点击基金管理人"""
        elements = self.find_elements(self.login_elements_loc)
        elements[3].click()

    def organization_click(self):
        """选择基金公司"""
        self.click(self.organization_loc)

    def object_click(self):
        """点击机构投资者"""
        elements = self.find_elements(self.login_elements_loc)
        elements[4].click()

    def object_select_click(self):
        """选择机构投资者"""
        self.click(self.object_loc)

    def input_verification(self):
        """输入验证码"""
        elements = self.find_elements(self.login_elements_loc)
        elements[5].send_keys('AAAA')

    def login_button_click(self):
        """点击登录"""
        self.click(self.button_login_loc)

    def retrieve_password_click(self):
        """找回密码"""
        self.click(self.retrieve_password_loc)


if __name__ == '__main__':
    driver = browser()
    browser = PCLogin(driver)
    browser.open_url(pc_url)
    browser.retrieve_password_click()


