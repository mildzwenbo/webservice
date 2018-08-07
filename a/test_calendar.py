"""
@author:liuxin
@date:2018-8-7
@brief:数据维护-所有产品-数据日历页面测试用例
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time

from page.SafeManager.data_maintenance.data_calendar import Calendar, browser, manager_url
from common.log import logger


class DataCalendar(unittest.TestCase):
    """对数据维护-所有产品-数据日历页面所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(5120, 2880))
            cls.display.start()
        cls.browser = browser()
        cls.driver = Calendar(cls.browser)
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
        self.driver.click_date()

    def tearDown(self):
        time.sleep(1)

    def test_a_log(self):
        """点击数据日历页面的操作日志按钮测试用例"""
        try:
            self.driver.click_log()
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '操作日志')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_b_import_data(self):
        """点击数据日历页面的导入数据按钮测试用例"""
        try:
            self.driver.click_import_data()
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '导入数据')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_c_return(self):
        """点击数据日历页面的返回列表按钮测试用例"""
        try:
            self.driver.click_return()
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '所有产品')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_d_crumbs(self):
        """点击数据日历页面可点击的面包屑链接测试用例"""
        try:
            self.driver.click(self.driver.crumbs)
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '所有产品')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_e_cancel_delete(self):
        """点击数据日历页面取消删除估值表测试用例"""
        try:
            self.driver.click_delete_excel()
            self.driver.cancel_button()
            time.sleep(1)
            text = self.driver.find_element(('class name', 'el-message__content')).text
            self.assertEqual(text, '已取消删除')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_f_sure_delete(self):
        """点击数据日历页面确定删除估值表测试用例"""
        try:
            self.driver.click_delete_excel()
            self.driver.sure_button()
            time.sleep(1)
            text = self.driver.find_element(('class name', 'el-message__content')).text
            self.assertEqual(text, '成功删除估值表')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_g_empty_delete(self):
        """点击数据日历页面空删除估值表测试用例"""
        try:
            self.driver.click_delete_excel()
            time.sleep(1)
            text = self.driver.find_element(('class name', 'el-message__content')).text
            self.assertEqual(text, '没有估值表可以删除')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_h_import_return(self):
        """点击导入数据页面，返回按钮测试用例"""
        try:
            self.driver.click_import_data()
            self.driver.click_log()
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '数据日历')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_i_log(self):
        """点击导入数据页面，操作日志按钮测试用例"""
        try:
            self.driver.click_import_data()
            self.driver.click_operate()
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '操作日志')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_j_crumbs(self):
        """点击导入数据页面可点击的面包屑链接测试用例"""
        try:
            self.driver.click_import_data()
            self.driver.click(self.driver.crumbs)
            time.sleep(1)
            log_text = self.driver.find_element(('class name', 'hovers')).text
            self.assertEqual(log_text, '所有产品')
        except Exception as msg:
            logger.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

