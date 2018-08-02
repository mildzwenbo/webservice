"""
@author:
@date:
@brief:产品列表更高风险等级产品页的测试
"""

import platform
from pyvirtualdisplay import Display
import time
import unittest

from common.log import logger
from the_old_system_page.PC import Agreement, browser, agreement_url, pc_url


class TestAgreement(unittest.TestCase):
    """产品列表更高风险等级产品页的测试"""

    @classmethod
    def setUpClass(cls):
        sty = platform.platform()
        if sty[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.driver = browser()
        cls.log = logger
        cls.browser = Agreement(cls.driver)
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        sty = platform.platform()
        if sty[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        self.browser.yf_pc_login()
        self.browser.open_url(agreement_url)

    def tearDown(self):
        time.sleep(2)

    def test_affirm_click(self):
        """点击取消按钮"""
        try:
            self.browser.affirm_click()
            time.sleep(1)
            text = self.browser.find_elements(('class name', 'el-button--medium'))[1].text
            self.assertEqual('查看更高风险等级的产品', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_confirm_click(self):
        """点击确认按钮"""
        try:
            self.browser.check_click()
            self.browser.confirm_click()
            time.sleep(1)
            text = self.browser.find_elements(('class name', 'el-breadcrumb__inner'))[1].text
            self.assertEqual('更高等级产品列表', text)

        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
