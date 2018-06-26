from common.get_url import GetUrl
from common.find_element import FindElement, browser
import time

manager_url = GetUrl().get_admin_url()


class ManagerLogin(FindElement):

    all_input = ('class name', 'layui-input')#管理端登录页面所有文本框定位
    login_button = ('id', 'login-btn')#管理端登录页面登录按钮定位

    def manager_login(self, name, password):
        elements = self.find_elements(self.all_input)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        self.click(self.login_button)


if __name__ == '__main__':
    driver = browser()
    browser = ManagerLogin(driver)
    browser.open_url(manager_url)
    browser.manager_login('15822816936', '123456')