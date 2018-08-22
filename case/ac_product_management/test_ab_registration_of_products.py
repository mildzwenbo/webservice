"""
@author:fei
@date:2018-98-21
@brief:登记产品页面的测试用例
"""

import unittest
from pyvirtualdisplay import Display
import time
import platform


from page.SafeManager.product_management.unreleased_product.registration_of_products import RegistrationOfProduct, browser, manager_url, registration_of_product_url
from common.log import logger


class TestRegistrationOfProducts(unittest.TestCase):

    """对登记产品页面的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == "Linux":
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = RegistrationOfProduct(cls.browser)
        cls.driver.open_url(manager_url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.yf_manager_login()
        time.sleep(1)
        self.driver.open_url(registration_of_product_url)
        time.sleep(3)
        js = "document.getElementsByClassName('sidebar-header')[0].setAttribute('style', 'display:none')"
        self.driver.js_execute(js)
        self.driver.js_scroll_top()
        time.sleep(1)


    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_aa_no_input(self):
        """不输入任何信息点击保存"""
        try:
            result = self.driver.no_input()
            self.assertTrue(result)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ab_no_input_release(self):
        """不输入任何信息，展开'其他选项'，点击保存并发布，查看报错信和错误提示数量"""
        try:
            result = self.driver.no_input_release()
            self.assertTrue(result)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ac_input_something(self):
        """填写正常的信息进行登记"""
        try:
            self.driver.input_something('自动化测试11', '自动化测试11', '自动化测试11')
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('保存成功',text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ad_existing_name(self):
        """输入的产品名称已经纯在，点击保存"""
        try:
            self.driver.input_something('自动化测试11', '自动化测试12', '自动化测试12')
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('产品名称已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_af_existing_code(self):
        """输入已经存在的简称，点击保存"""
        try:
            self.driver.input_something('自动化测试13', '自动化测试11', '自动化测试12')
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('产品简称已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ae_existing_name2(self):
        """输入已经存在的编码，点击保存"""
        try:
            self.driver.input_something('自动化测试13', '自动化测试12', '自动化测试11')
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('编码已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()
