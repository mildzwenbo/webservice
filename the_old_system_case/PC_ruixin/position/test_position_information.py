"""
@author:fei
@date:2018-7-2
@brief:对持仓信息页面操作的测试用例
"""

import platform
import unittest
import time
import pyvirtualdisplay

from common.log import logger
from the_old_system_page.PC.position import ThePositionInformation, position_url, pc_url, browser


class TestThePositionInformation(unittest.TestCase):
    """对持仓信息页面操作的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.platform()
        if cls.syt[:5] == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = ThePositionInformation(cls.browser)
        cls.driver.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt[:5] == "Linux":
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_pc_login()
        self.driver.open_url(position_url)
        time.sleep(2)

    def tearDown(self):
        time.sleep(1)

    def test_search(self):
        """
        持仓信息中，输入产品名称“资舟投资基金R3”点击查询，和列表中的产品名称做对比
        :return:
        """
        try:
            self.driver.search('资舟投资基金R3')
            text_element = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div')
            text = self.driver.get_text(text_element)
            self.assertEqual('资舟投资基金R3', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_look_over(self):
        """
        第一条数据点击操作，点击查看，进入到查看页面， 以“基本信息”作为对比
        :return:
        """
        try:
            self.driver.look_over()
            text_element = ('xpath', '//*[@id="pane-0"]/div[1]/div[2]/h3')
            text = self.driver.get_text(text_element)
            self.assertEqual('基本信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_subscribe(self):
        """
        第一条数据点击操作，点击申购，进入到查看页面， 以“风险揭示书”作为对比
        :return:
        """
        try:
            self.driver.subscribe()
            text_element = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div[1]/h3')
            text = self.driver.get_text(text_element)
            self.assertEqual("风险揭示书", text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_redemption(self):
        """
        第一条数据点击操作，点击申购，进入到查看页面， 以“风险揭示书”作为对比
        :return:
        """
        try:
            self.driver.redemption()
            text_element = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/span')
            text = self.driver.get_text(text_element)
            self.assertEqual("赎回申请", text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()