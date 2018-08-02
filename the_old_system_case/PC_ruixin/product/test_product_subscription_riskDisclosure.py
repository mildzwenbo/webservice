"""
@author:fei
@date:2018-5-30
@brief:申购过程中的分享揭示书的测试
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time

from common.log import logger
from the_old_system_page.PC.product.product_subscription_riskDisclosure import RiskDisclosure, risk_disclosure_url, browser, pc_url


class TestRiskDisclosure(unittest.TestCase):
    """申购过程中的分享揭示书的测试"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.driver = browser()
        cls.browser = RiskDisclosure(cls.driver)
        cls.browser.open_url(pc_url)
        cls.log = logger

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
        self.browser.open_url(risk_disclosure_url)
        time.sleep(1)

    def tearDown(self):
        pass

    def test_cancel_button_click(self):
        """点击取消按钮"""
        try:
            self.browser.cancel_button_click()
            time.sleep(1)
            text = self.browser.get_text(('class name', 'no-redirect'))
            self.assertEqual('产品列表', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_confirm_button_click(self):
        """点击确定按钮"""
        try:
            self.browser.confirm_button_click()
            time.sleep(1)
            text = self.browser.get_text(('css', '#app > div > div.main-container > '
                                                 'section > div > div:nth-child(2) > h4'))
            self.assertEqual('申购申请', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
