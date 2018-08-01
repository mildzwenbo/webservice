"""
@author:fei
@date:2018-7-31
@brief:首页所有元素的测试用例
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time


from page.SafeManager.home.home import Home, browser, manager_url
from common.log import logger



class TestHome(unittest.TestCase):
    """对首页所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.browser = browser()
        cls.driver = Home(cls.browser)
        cls.driver.open_url(manager_url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_manager_login()

    def tearDown(self):
        time.sleep(1)


    def test_product_management_click(self):
        """点击快捷入口产品管理"""
        try:
            self.driver.product_management_click()
            text = self.driver.get_text(('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.list_head > p > span > span:nth-child(1)'))
            self.assertEqual(text, '产品管理')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_data_management_click(self):
        """点击快捷入口数据维护"""
        try:
            self.driver.data_management_click()
            text = self.driver.get_text(('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.list_head > p > span > span:nth-child(1)'))
            self.assertEqual(text, '数据维护')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_system_management_click(self):
        """点击快捷入口系统管理"""
        try:
            self.driver.system_management_click()
            text = self.driver.get_text(('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.list_head > p > span > span:nth-child(1)'))
            self.assertEqual(text, '系统管理')
        except Exception as msg:
            logger.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

