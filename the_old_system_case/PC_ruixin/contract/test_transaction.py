"""
@author:fei
@date:2018-7-3
@brief:申购记录下成交列表所有操作的测试用例
"""

import time
import platform
import ddt
import unittest
import pyvirtualdisplay

from common.get_path import GetPath
from common.log import logger
from the_old_system_page.PC.contract.transaction import Transaction, pc_url, browser, transaction_url
from common.read_excel import ReadExcel

excel_path = GetPath().get_params_path('contract.xlsx')
sheet = 'Sheet1'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestTransaction(unittest.TestCase):
    """申购记录下成交列表所有操作的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.platform()
        if cls.syt[:5] == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(5120, 2280))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = Transaction(cls.browser)
        cls.driver.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_pc_login()
        self.driver.open_url(transaction_url)
        time.sleep(1)
        self.driver.transaction_click()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @ddt.data(*data)
    def test_search(self, data):
        """"查询不同的类型：申购、赎回 对应不同的数据"""
        try:
            print(data['name'])
            self.driver.search('R3', data['select_type'])
            time.sleep(2)
            text = self.driver.get_text(('xpath', '//*[@id="pane-1"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div'))
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
