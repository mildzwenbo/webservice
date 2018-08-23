"""
@author:liuxin
@ad_date:2018-8-8
@brief:数据维护-操作日志页面测试用例
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time
import os

from page.SafeManager.data_maintenance.operation_log import OperationLog, browser, manager_url
from common.log import logger


class Operation(unittest.TestCase):
    """对数据维护-操作日志页面所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(5120, 2880))
            cls.display.start()
        cls.browser = browser()
        cls.driver = OperationLog(cls.browser)
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
        self.driver.click_log_bar()

    def tearDown(self):
        time.sleep(1)

    def test_a_name(self):
        """查询：上传人查询结果"""
        try:
            self.driver.upload_heir('招商银行')
            self.driver.click_query_button()
            time.sleep(1)
            number = self.driver.query_number()
            self.assertEqual(number, '454')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_b_time(self):
        """查询：上传时间查询结果"""
        try:
            self.driver.upload_time('2018-08-07')
            self.driver.click_query_button()
            number = self.driver.query_number()
            self.assertEqual(number, '2')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_c_result(self):
        """查询：上传结果-成功查询结果"""
        try:
            self.driver.succeed_result()
            time.sleep(1)
            number = self.driver.query_number()
            self.assertEqual(number, '1254')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_d_result(self):
        """查询：上传结果-失败查询结果"""
        try:
            self.driver.loser_result()
            time.sleep(1)
            number = self.driver.query_number()
            self.assertEqual(number, '12')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_e_result(self):
        """查询：上传结果-全部查询结果"""
        try:
            self.driver.loser_result()
            time.sleep(1)
            self.driver.all_result()
            time.sleep(1)
            number = self.driver.query_number()
            self.assertEqual(number, '1266')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_f_result(self):
        """查询：查询结果为空"""
        try:
            self.driver.upload_heir('1234')
            self.driver.click_query_button()
            text = self.driver.find_element(('class name', 'el-table__empty-text')).text
            self.assertEqual(text, '无数据')

        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_g_download_file(self):
        """下载附件链接"""
        try:
            self.driver.click_file()
            time.sleep(1)
            each = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Download')
            if len(os.listdir(each)) > 0:
                result = True
                self.driver.delete_file(each)
            else:
                result = False
            self.assertTrue(result)
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_h_loser(self):
        """结果>失败链接"""
        try:
            self.driver.loser_result()
            time.sleep(1)
            self.driver.click_loser()
            time.sleep(1)
            text = self.driver.find_element(('class name', 'el-dialog__title')).text
            self.assertEqual(text, '失败原因')
        except Exception as msg:
            logger.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

