"""
@author:fei
@date:2018-08-01
@brief:对登录页面的测试用例
"""

from pyvirtualdisplay import Display
import unittest
import platform
import time

from common.log import logger
from page.SafeManager.login.login import Login, browser, login_url


class TestLogin(unittest.TestCase):
    """对登录页面的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.sty = platform.system()
        if cls.sty == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.browser = browser()
        cls.driver = Login(cls.browser)
        cls.driver.open_url(login_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.sty == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        time.sleep(1)

    def tearDown(self):
        pass


    def test_not_input(self):
        """不输入任何信息，对错误提示进行判断"""
        try:
            self.driver.no_input()
            targets_text = ('class name', 'el-form-item__error')
            time.sleep(1)
            texts = self.driver.find_elements(targets_text)
            name_error_text = texts[0].text
            institutions_text = texts[1].text
            code_text = texts[2].text
            self.assertEqual(name_error_text, '必填项')
            self.assertEqual(institutions_text, '请选择基金管理人')
            self.assertEqual(code_text, '请输入验证码')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_login(self):
        """正常登录"""
        try:
            self.driver.login()
            text = self.driver.get_text(('id', 'user'))
            self.assertEqual(text, '王云飞')
        except Exception as msg:
            logger.info(str(msg))
            raise

    @unittest.skip('pass')
    def test_agency_disabled_login(self):
        """机构已经被停用"""
        try:
            self.driver.agency_disabled_login()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual(text, '机构已被停用')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_reset_click(self):
        """点击清空按钮"""
        try:
            self.driver.reset_click()
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'el-input__inner'))[0].get_attribute('placeholder')
            self.assertEqual(text, '请输入手机号')
        except Exception as msg:
            logger.info(str(msg))
            raise

if __name__ == '__main__':
    unittest.main()
