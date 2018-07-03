"""
@author:fei
@date:2018-7-2
@brief:信息纰漏页面的报告页面的操作测试用例
"""

import platform
import pyvirtualdisplay
import unittest
import time
import ddt

from common.log import logger
from page.PC.disclosure.report import Report, pc_url, browser, report_url
from common.read_excel import ReadExcel
from common.get_path import GetPath

excel_path = GetPath().get_params_path('password.xlsx')
sheet = 'Sheet3'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestReport(unittest.TestCase):
    """信息纰漏页面的报告页面的操作测试用例"""
    @classmethod
    def setUpClass(cls):
        cls.syt = platform.platform()
        if cls.syt[:5] == "Linux":
            cls.display = pyvirtualdisplay.Display(visible=0, size=(5120, 2280))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = Report(cls.browser)
        cls.driver.open_url(pc_url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_pc_login()
        self.driver.open_url(report_url)
        time.sleep(1)
        self.driver.report_click()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @ddt.data(*data)
    def test_search(self, data):
        """查询不同的报告类型：日报、周报、月报、季报、年报，对应不同的数据"""
        try:
            print(data['name'])
            self.driver.search(data['product_name'], data['type_report'])
            time.sleep(2)
            text = self.driver.get_text(('xpath', '//*[@id="pane-1"]/div/div[2]/div/div[3]/table/tbody/tr/td[1]/div'))
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()