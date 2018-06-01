from common.get_url import GetUrl
from common.find_element import FindElement, browser
import time

pc_url = GetUrl().get_pc_url() + '#/manlogin'


class PCLogin(FindElement):

    login_elements_loc = ('class name', 'el-input__inner') #所有的输入框

    retail_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')  #个人投资者
    institution_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]')  #机构投资者
    client_investor_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[3]')  #客户投资者

    organization_loc = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li') #基金公司的定位
    button_login_loc = ('css', '#app > div > form > div:nth-child(9) > div > button > span')
    object_loc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span')

    def pc_login(self, name, password, investor='1'):
        """
        :param name:
        :param password:
        :param investor:选择的类型，1为个人，2为机构，3为客户
        :return:
        """
        elements = self.find_elements(self.login_elements_loc)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        elements[2].click()
        time.sleep(1)
        if investor == '1':
            self.click(self.retail_loc)
            time.sleep(1)
            elements[3].click()
            time.sleep(1)
            self.click(self.organization_loc)
            time.sleep(1)
            elements[5].send_keys('AAAA')
            time.sleep(1)
            self.click(self.button_login_loc)
        else:
            if investor == '2':
                self.click(self.institution_loc)
            else:
                self.click(self.client_investor_loc)
            time.sleep(1)
            elements[3].click()
            time.sleep(1)
            self.click(self.organization_loc)
            time.sleep(1)
            elements[4].click()
            time.sleep(1)
            self.click(self.object_loc)
            time.sleep(1)
            elements[5].send_keys('AAAA')
            time.sleep(1)
            self.click(self.button_login_loc)
        time.sleep(2)


if __name__ == '__main__':
    driver = browser()
    browser = PCLogin(driver)
    browser.open_url(pc_url)
    browser.pc_login('15822816936', 'abc123456', '1')
