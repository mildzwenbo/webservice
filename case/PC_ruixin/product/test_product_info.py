"""
@author:
@date:2018-5-29
@brief:产品详情页面测试用例
"""

from pyvirtualdisplay import Display
import time
import platform
import unittest
import ddt


from common.log import logger
from page.PC.product.product_Info import ProductInfo, browser, product_info_url, pc_url
from common.read_excel import ReadExcel
from common.get_path import GetPath


excelpath = GetPath().get_params_path('password.xlsx')
sheet = 'Sheet2'
data = ReadExcel(excelpath, sheet).data_list()


@ddt.ddt
class TestProductInfo(unittest.TestCase):
    """对产品详情页面的所有操作"""

    @classmethod
    def setUpClass(cls):
        sty = platform.platform()
        if sty[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.driver = browser()
        cls.browser = ProductInfo(cls.driver)
        cls.log = logger
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        self.browser.yf_pc_login()
        self.browser.open_url(product_info_url)

    def tearDown(self):
        time.sleep(2)

    def test_the_net_value_of_records_lco_click(self):
        """点击净值记录列表"""
        try:
            self.browser.the_net_value_of_records_lco_click()
            text = self.browser.get_text(('xpath', '//*[@id="pane-2"]/div/div[1]/div[1]'))
            print(text)
            self.assertEqual('净值日期:', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_transaction_list_click(self):
        """点击成交记录列表"""
        try:
            self.browser.transaction_list_click()
            text = self.browser.get_text(('xpath', '//*[@id="pane-3"]/div/div[1]/div[1]/span'))
            self.assertEqual('成交日期:', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_subscribe_click(self):
        """基本要素页面点击申购"""
        try:
            self.browser.subscribe_click()
            time.sleep(1)
            text = self.browser.get_text(('css', '#app > div > div.main-container > section > div > div:nth-child(2)'
                                                 ' > h3'))
            self.assertEqual('一、基金管理人承诺', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_net_worth_search(self):
        """净值页面搜索"""
        try:
            self.browser.the_net_value_of_records_lco_click()
            time.sleep(1)
            self.browser.input_data()
            self.browser.net_worth_search_click()
            time.sleep(2)
            text = self.browser.get_text(('xpath', '//*[@id="pane-2"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div'))
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    @ddt.data(*data)
    def test_transaction_search(self, data):
        """成交列表中的搜索"""
        try:
            self.browser.transaction_list_click()
            time.sleep(1)
            self.browser.input_transaction_date()
            self.browser.business_type_click()
            if data['business'] == '1':
                self.browser.select_subscribe()
            else:
                self.browser.select_redemption()
            self.browser.transaction_search_click()
            time.sleep(2)
            text = self.browser.get_text(('xpath', '//*[@id="pane-3"]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div'))
            print(text)
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
