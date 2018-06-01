"""
@author:xin
@date:2018-5-29
@brief:身份信息-修改密码页码所有元素定位
"""

from page.PC.IdentityInformation.IdentityPage import IdentityInfo, pc_url, browser


class ChangePassword(IdentityInfo):
    password_input = ('class name', 'el-input__inner')  #身份信息页面-修改密码页面，所有文本框定位
    confirm_button = ('xpath', '//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/button')

    def old_pwd(self, text):
        """当前登录密码文本内容框输入"""
        elements = self.find_elements(self.password_input)[0]
        elements.send_keys(text)

    def new_pwd(self, text):
        """新的登录密码文本内容框输入"""
        elements = self.find_elements(self.password_input)[1]
        elements.send_keys(text)

    def affirm_pwd(self, text):
        """确认新的登录密码文本内容框输入"""
        elements = self.find_elements(self.password_input)[2]
        elements.send_keys(text)

    def click_confirm(self):
        """点击确认按钮"""
        self.click(self.confirm_button)


if __name__ == '__main__':
    driver = browser()
    cpwd = ChangePassword(driver)
    cpwd.open_url(pc_url)
    cpwd.pc_login("15822816936","abc123456")
