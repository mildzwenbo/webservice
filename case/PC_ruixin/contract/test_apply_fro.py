"""
@author:fei
@date:2018-7-3
@brief:申赎记录下申请列表中的测试用例
"""

import unittest
import platform
import pyvirtualdisplay
import ddt
import time

from common.log import logger
from common.read_excel import ReadExcel
from page.PC.contract.apply_fro import ApplyFor, browser, pc_url, apply_url
from common.get_path import GetPath

excel_path = GetPath().get_params_path('contract.xlsx')
sheet = 'Sheet1'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestApplyFor(unittest.TestCase):
    """申赎记录下申请列表中的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.sty = platform.platform()
        if cls.sty[:5] == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = ApplyFor(cls.browser)
        cls.driver.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.sty[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_pc_login()
        self.driver.open_url(apply_url)
        time.sleep(1)

    @ddt.data(*data)
    def test_search(self, data):
        """搜索功能的测试， 搜索不同的类型的R3产品，和产品名称做对比"""
        try:
            print(data['name'])
            self.driver.search('R3', data['select_type'])
            element = ('xpath', '//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            text = self.driver.get_text(element)
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_transaction_click(self):
        """进入到成交列表和以份额确认日字段做对比"""
        try:
            self.driver.transaction_click()
            time.sleep(2)
            text = self.driver.get_text(('xpath', '//*[@id="pane-1"]/div/div[1]/form/div[3]/label'))
            self.assertEqual("份额确认日：", text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_apply_fro(self):
        """进入到申请列表以申请日期字段对比"""
        try:
            self.driver.transaction_click()
            self.driver.apply_fro_lick()
            time.sleep(2)
            text = self.driver.get_text(('xpath', '//*[@id="pane-0"]/div/div[1]/form/div[3]/label'))
            self.assertEqual("申请日期：", text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

