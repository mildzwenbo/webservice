"""
@author:fei
@date:2018-7-2
@brief:信息纰漏页面的历史净值页面的操作测试用例
"""

import unittest
import time
import platform
import pyvirtualdisplay

from page.PC.disclosure.net_value_of_history import NetValueOfHistory, pc_url, browser, disclosure_url
from common.log import logger


class TestVetValueOfHistory(unittest.TestCase):
    """
    对信息纰漏历史净值页面的测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.sty = platform.platform()
        if cls.sty[:5] == "Linux":
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = NetValueOfHistory(cls.browser)
        cls.driver.open_url(pc_url)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.sty[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_pc_login()
        self.driver.open_url(disclosure_url)

    def tearDown(self):
        time.sleep(1)

    def test_report_click(self):
        """
        点击报告，以“报告类型”做对比
        :return:
        """
        try:
            self.driver.report_click()
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'el-form-item__label'))[3].text
            self.assertEqual('报告类型：', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_net_value_click(self):
        """
        点击报告，在点击历史净值，以“净值日期”做对比
        :return:
        """
        try:
            self.driver.report_click()
            self.driver.net_value_click()
            text = self.driver.find_elements(('class name', 'el-form-item__label'))[1].text
            self.assertEqual("净值日期：", text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_search(self):
        try:
            time.sleep(2)
            self.driver.net_value_product_name_input('资舟投资基金R3')
            self.driver.net_value_date_input()
            self.driver.net_value_search_click()
            time.sleep(1)
            text_loc = ('xpath', '//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div')
            text = self.driver.get_text(text_loc)
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()



