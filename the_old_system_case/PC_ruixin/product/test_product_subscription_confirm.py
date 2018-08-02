"""
@author:fei
@date:2018-5030
@brief:申购产品最终的确认页面、填写申购金额页面测试
"""

import time
import unittest
import platform
from pyvirtualdisplay import Display

from common.log import logger
from the_old_system_page.PC.product.product_subscription_confirm import SubscriptionConfirm, browser, pc_url, subscription_confirm_url


class TestSubscriptionConfirm(unittest.TestCase):
    """申购产品最终的确认页面、填写申购金额页面测试"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.driver = browser()
        cls.browser = SubscriptionConfirm(cls.driver)
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
        self.browser.open_url(subscription_confirm_url)
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
            self.browser.confirm_button_click('20000')
            time.sleep(2)
            text = self.browser.get_text(('css', '#app > div > div.main-container > section > div > div > h1'))
            self.assertEqual('提交成功！', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()