"""
@author:fei
@date:2018-5-26
@brief:登录页面等测试用例， 没有写主持的测试用例
"""

import platform
from pyvirtualdisplay import Display
import time
import unittest
import ddt

from common.log import logger
from the_old_system_page.PC.login import PCLogin, browser, pc_url
from common.get_path import GetPath
from common.read_excel import ReadExcel


excel_path = GetPath().get_params_path('password.xlsx')
sheet = 'Sheet1'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestLogin(unittest.TestCase):
    """登录页面等测试用例"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = PCLogin(cls.driver)
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()

    def tearDown(self):
        time.sleep(2)

    def login(self, name, password, investor='1'):
        elements = self.browser.find_elements(self.browser.login_elements_loc)
        elements[0].send_keys(name)
        time.sleep(1)
        elements[1].send_keys(password)
        elements[2].click()
        time.sleep(1)
        if investor == '1':
            self.browser.click(self.browser.retail_loc)
            time.sleep(1)
            elements[3].click()
            time.sleep(1)
            self.browser.click(self.browser.organization_loc)
            time.sleep(1)
            elements[5].send_keys('AAAA')
            time.sleep(1)
            self.browser.click(self.browser.button_login_loc)
            time.sleep(1)
        else:
            if investor == '2':
                self.browser.click(self.browser.institution_loc)
            else:
                self.browser.click(self.browser.client_investor_loc)
            time.sleep(1)
            elements[3].click()
            time.sleep(1)
            self.browser.click(self.browser.organization_loc)
            time.sleep(1)
            elements[4].click()
            time.sleep(1)
            self.browser.click(self.browser.object_loc)
            time.sleep(1)
            elements[5].send_keys('AAAA')
            time.sleep(1)
            self.browser.click(self.browser.button_login_loc)
            time.sleep(1)

    def test_null(self):
        """不填写任何信息，点击登录按钮"""
        try:
            self.browser.login_button_click()
            error_loc = ('class name', 'el-form-item__error')
            elements = self.browser.find_elements(error_loc)
            time.sleep(1)
            name_error_text = elements[0].text
            password_error_text = elements[1].text
            investor_error_text = elements[2].text
            object_error_text = elements[3].text
            verification_error_text = elements[4].text

            self.assertEqual('必填项，不能为空', name_error_text)
            self.assertEqual('请输入密码', password_error_text)
            self.assertEqual('请选择投资者类型', investor_error_text)
            self.assertEqual('请选择基金管理人', object_error_text)
            self.assertEqual('请输入验证码', verification_error_text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    @ddt.data(*data)
    def test_login_investor(self, data):
        """个人用户登录、机构客户登录、产品客户登录"""
        try:
            self.login(data['name'], data['password'], data['investor'])
            user_name = (data['type'], data['selector'])
            text = self.browser.get_text(user_name)
            self.assertEqual(data['result'], text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_retrieve_password_click(self):
        """点击找回密码，进入到找回密码页面"""
        try:
            self.browser.retrieve_password_click()
            title = self.browser.get_title()
            self.assertEqual('基金运营管理平台', title)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

