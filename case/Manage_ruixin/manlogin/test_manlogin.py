from common.find_element import browser
from pyvirtualdisplay import Display
from page.SafeManager.ManageLogin import ManageLoginPage,ManageLoginUrl
from common.log import logger
import unittest
import platform


class TestLogin(unittest.TestCase):
    """管理端登录页面"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = ManageLoginPage(cls.driver)
        cls.browser.open_url(ManageLoginUrl)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.log = logger

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()

    def test_1(self):
        """用户名密码为空"""
        try:
            self.browser.sbm()
            self.assertEqual(self.browser.type_alarm2(),'用户不存在')
        except Exception as msg:
            self.log.info(msg)
            raise

    def test_2(self):
        """用户名密码正确登录"""
        try:
            self.browser.ManageLogin('13511055879','123456','')
            self.assertEqual(self.browser.type_username(),'金战军')
        except Exception as msg:
            self.log.info(msg)
            raise


if __name__ == "__main__":
    unittest.main()

