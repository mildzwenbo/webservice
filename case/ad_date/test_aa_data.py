"""
@author:liuxin
@ad_date:2018-8-6
@brief:数据维护-所有产品页面测试用例
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time

from selenium.webdriver.common.keys import Keys
from page.SafeManager.data_maintenance.product import Product, browser, manager_url
from common.log import logger


class AllProducts(unittest.TestCase):
    """对数据维护-所有产品页面所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(5120, 2880))
            cls.display.start()
        cls.browser = browser()
        cls.driver = Product(cls.browser)
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
        self.driver.lx_manager_login()
        self.driver.click_bar()

    def tearDown(self):
        time.sleep(1)

    def test_a_name_query(self):
        """查询：基金名称查询结果"""
        try:
            self.driver.query_name('乾韬')
            self.driver.click_query()
            number = self.driver.query_number()
            self.assertEqual(number, '7')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_b_code_query(self):
        """查询：基金编码查询结果"""
        try:
            self.driver.query_code('SN3597')
            self.driver.click_query()
            fund_name = ('class name', 'el-tooltip')
            value = self.driver.find_elements(fund_name)[2].text
            self.assertEqual(value, 'SN3597')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_c_group_query(self):
        """查询：基金名称、基金编码查询结果"""
        try:
            self.driver.query_name('乾韬')
            self.driver.query_code('SN')
            self.driver.click_query()
            number = self.driver.query_number()
            self.assertEqual(number, '3')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_d_all_query(self):
        """查询：查询全部数据"""
        try:
            self.driver.query_name('乾韬')
            self.driver.query_code('SN')
            self.driver.click_query()
            input_name = self.driver.find_elements(self.driver.fund_query)[0]
            input_name.send_keys(Keys.CONTROL, 'a')
            input_name.send_keys(Keys.BACKSPACE)
            input_name = self.driver.find_elements(self.driver.fund_query)[1]
            input_name.send_keys(Keys.CONTROL, 'a')
            input_name.send_keys(Keys.BACKSPACE)
            self.driver.click_query()
            time.sleep(1)
            number = self.driver.query_number()
            self.assertEqual(number, '22')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_e_empty_query(self):
        """查询：查询结果为空"""
        try:
            self.driver.query_name('qwe')
            self.driver.click_query()
            value = self.driver.null_number()
            self.assertEqual(value, '无数据')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_f_data(self):
        """点击操作>数据维护连接跳转"""
        try:
            self.driver.click_date()
            time.sleep(1)
            data_calendar = ('class name', 'hovers')
            value = self.driver.find_element(data_calendar).text
            self.assertEqual(value, '数据日历')
        except Exception as msg:
            logger.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

