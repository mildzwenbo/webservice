"""
@author:fei
@date:2018-08-30
@brief:历史净值页面的测试测试用例
"""


from pyvirtualdisplay import Display
import platform
import time
import unittest

from page.SafeManager.product_management.published_product.history_list import HistoryList, browser, history_list_url, manager_url
from common.log import logger

class TestHistoryList(unittest.TestCase):
    """对已发布产品中的历史净值页面的操作"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = HistoryList(cls.browser)
        cls.driver.open_url(manager_url)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == "Linux":
            cls.display.stop()


    def setUp(self):
        self.driver.yf_manager_login()
        time.sleep(2)
        self.driver.open_url(history_list_url)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_date_search(self):
        try:
            result = self.driver.date_search()
            logger.info('在日历输入框中输入日期，点击搜素，返回的结果为：%s' % result)
            self.assertEqual(result, '无数据')
        except Exception as msg:
            logger.info(msg)
            raise
