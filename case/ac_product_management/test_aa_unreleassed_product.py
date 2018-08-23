"""
@author:fei
@date:2018-08-06
@brief:未发布产品页面所有测试用例的编写
"""

import unittest
from pyvirtualdisplay import Display
import platform
import time

from common.log import logger
from page.SafeManager.product_management.unreleased_product.unreleased_product import UnreleasedProduct, manager_url, unreleased_product_url, browser
from common.exec_mysql import ExecMysql


class TestUnreleasedProduct(unittest.TestCase):
    """发布产品页面所有测试用例的编写"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.browser = browser()
        cls.driver = UnreleasedProduct(cls.browser)
        cls.driver.open_url(manager_url)
        cls.mysql = ExecMysql()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.yf_manager_login()
        self.driver.open_url(unreleased_product_url)
        time.sleep(1)

    def tearDown(self):
        pass


    def test_a_search_input_name(self):
        """只输入产品名称点击搜索"""
        try:
            text = self.driver.search_input_name()
            self.assertEqual('自动化测试产品4', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_b_search_input_code(self):
        """只输入基金编码，点击搜索"""
        try:
            text = self.driver.search_input_code()
            self.assertEqual('自动化测试产品4', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_c_registration_of_products(self):
        """点击登记产品"""
        try:
            self.driver.registration_of_products()
            time.sleep(1)
            text = self.driver.get_text(('css', '.module-title>span'))
            self.assertEqual('基本信息', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_d_product_release(self):
        """点击产品发布"""
        try:
            self.driver.product_release()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual(text, '请选择您要发布的产品')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_e_operation_product_click(self):
        """列表中的操作按钮,查看选项，基金名称为：自动化测试产品1"""
        try:
            self.driver.operation_product_click()
            time.sleep(1)
            operation_list_loc = ('class name', 'el-dropdown-menu__item')

            text = self.driver.find_elements(operation_list_loc)[12].text
            self.assertEqual(text, '编辑')
        except Exception as msg:
            logger.info(msg)
            raise


    def test_f_editor_product_click(self):
        """列表中的操作按钮,点击编辑，基金名称为：自动化测试产品1"""
        try:
            self.driver.editor_product_click()
            text = self.driver.get_text(('css', '.module-title>span'))
            self.assertEqual('基本信息', text)
        except Exception as msg:
            logger.info(msg)
            raise


    def test_g_release_product_click(self):
        """列表中的操作按钮,点击发布，基金名称为：自动化测试产品1"""
        try:
            self.driver.release_product_click()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('发布成功!', text)
            self.mysql.update_mysql("UPDATE run_status SET status='1' WHERE name='test_g_release_product_click';")
        except Exception as msg:
            self.mysql.update_mysql("UPDATE run_status SET status='0' WHERE name='test_g_release_product_click';")
            logger.info(msg)
            raise

    def test_h_delete_product_click(self):
        """列表中的操作按钮,点击删除，基金名称为：自动化测试产品2"""
        try:
            self.driver.delete_product_click()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('删除成功!', text)
        except Exception as msg:
            logger.info(msg)
            raise



if __name__ == '__main__':
    unittest.main()