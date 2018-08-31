from common.get_url import GetUrl
from common.find_element import FindElement, browser
import time
import threading
import configparser
from common.get_path import GetPath
from common.select_environment import Select

select = Select().select()

pc_url = GetUrl().get_pc_url() + '#/login'


class PCLogin(FindElement):
    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    conf_ptah = GetPath().get_conf_path('username.ini')
    conf.read(conf_ptah, encoding='utf-8')
    if select == '1':
        yf_pc_name = conf.get('test_name', 'yf_pc_name')
        lx_pc_name = conf.get('test_name', 'lx_pc_name')
        zj_pc_name = conf.get('test_name', 'zj_pc_name')
        pc_pwd = conf.get('test_name', 'pc_pwd')
    elif select == '0':
        yf_pc_name = conf.get('test_name', 'yf_pc_name')
        lx_pc_name = conf.get('test_name', 'lx_pc_name')
        zj_pc_name = conf.get('test_name', 'zj_pc_name')
        pc_pwd = conf.get('test_name', 'pc_pwd')
    mutex.release()

    login_elements_loc = ('class name', 'el-input__inner') #所有的输入框

    retail_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')  #个人投资者
    institution_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]')  #机构投资者
    client_investor_loc = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[3]')  #客户投资者

    organization_loc = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li') #基金公司的定位
    button_login_loc = ('css', '#app > div > form > div:nth-child(9) > div > button > span')
    object_loc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li/span')

    def yf_pc_login(self, name=yf_pc_name, password=pc_pwd, investor='1'):
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

    def lx_pc_login(self, name=lx_pc_name, password=pc_pwd, investor='1', select='1'):
        """
        :param name:
        :param password:
        :param investor:选择的类型，1为个人，2为机构，3为客户
        :param select：机构用户1代表自动化用户，2代表PC申请
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
                time.sleep(1)
                elements[3].click()
                time.sleep(1)
                self.click(self.organization_loc)
                time.sleep(1)
                elements[4].click()
                time.sleep(1)
                if select == '1':
                    self.click(('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[2]'))
                else:
                    self.click(self.object_loc)
                time.sleep(1)
                elements[5].send_keys('AAAA')
                time.sleep(1)
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

    def zj_pc_login(self, name=zj_pc_name, password=pc_pwd, investor='1'):
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
            time.sleep(1)
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
    browser.yf_pc_login()

