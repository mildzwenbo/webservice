"""
@author:fei
@date:2018-7-4
@brief:注册过程中确认页面所有的测试用例
"""

import pyvirtualdisplay
import platform
import unittest
import time

from common.log import logger
from page.PC.register.register_confirm import RegisterConfirm, register_confirm_url, browser, pc_url


class TestRegisterConfirm(unittest.TestCase):
    """对确认页面所有的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = RegisterConfirm(cls.browser)
        cls.driver.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.open_url(register_confirm_url)
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_login_click(self):
        """点击登录按钮，返回到等页面"""
        try:
            self.driver.login_click()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'title'))
            self.assertEqual('基金运营管理系统', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_individual_investor(self):
        """点击个人投资者进行注册，进入到验证页面"""
        try:
            self.driver.individual_investor('1')
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'el-step__title'))[0].text
            self.assertEqual('输入注册信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_institutional_investor(self):
        """点击机构投资者进行注册，进入到验证页面"""
        try:
            self.driver.individual_investor('2')
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'el-step__title'))[0].text
            self.assertEqual('输入注册信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_do_not_enter_the_fund_manager(self):
        """不输入基金管理人点击下一步，查看报错信息"""
        try:
            self.driver.do_not_enter_the_fund_manager()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-form-item__error'))
            self.assertEqual('请选择基金管理人', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
