"""
@author:xin
@date:2018-5-28
@brief:身份信息页面测试用例
"""

import platform
from pyvirtualdisplay import Display
import time
import unittest


from common.log import logger
from page.PC.IdentityInformation.IdentityPage import IdentityInfo, browser, pc_url

#@unittest.skip('pass')
class TestIdentityInfo(unittest.TestCase):
    """身份信息页面测试用例"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(800, 900))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = IdentityInfo(cls.driver)
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
        self.browser.pc_login('15822816936','abc123456')

    def tearDown(self):
        time.sleep(2)

    def test_password_skip(self):
        """点击进入修改密码页面"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            current_page = ('class name', "no-redirect")
            text = self.browser.get_text(current_page)
            self.assertEqual('修改密码', text)
            time.sleep(1)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_change_phone(self):
        """点击进入更换手机号页面"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_phone()
            phone_page = ('class name', "no-redirect")
            text = self.browser.get_text(phone_page)
            self.assertEqual('更换手机号', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise
    #@unittest.skip('pass')

    def test_edit_information(self):
        """点击进入修改个人信息页面"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_edit()
            message_page = ('class name', "no-redirect")
            text = self.browser.get_text(message_page)
            self.assertEqual('修改个人投资者基本信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()


