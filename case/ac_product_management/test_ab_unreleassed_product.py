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

mysql = ExecMysql()
sql = "SELECT status FROM run_status WHERE name='test_ac_input_something'"
status = int(mysql.select_mysql(sql)[0][0])


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
        self.driver.yf_manager_login()
        self.driver.open_url(unreleased_product_url)
        time.sleep(1)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_a_search_input_name(self):
        """只输入产品名称点击搜索"""
        try:
            name = '产品' + str(int(time.time()))
            logger.info('搜索目标：%s' % name)
            text = self.driver.search_input_name(name)
            logger.info("结果：%s" % text)
            if text == '无数据':
                pass
            else:
                self.assertIn(name, text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_b_search_input_code(self):
        """只输入基金编码，点击搜索"""
        try:
            code = '产品' + str(int(time.time()))
            logger.info('搜索的基金编码为：%s' % code)
            text = self.driver.search_input_code(code)
            logger.info('返回的结果为:%s' % text)
            if text == '无数据':
                pass
            else:
                self.assertEqual(code, text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_c_registration_of_products(self):
        """点击登记产品"""
        try:
            text = self.driver.registration_of_products()
            logger.info('点击登记产品后返回的结果：%s' % text)
            self.assertEqual(text, '基本信息')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_d_product_release(self):
        """点击产品发布"""
        try:
            text = self.driver.product_release()
            logger.info('没有选择产品点击发布产品后返回的错误提示：%s' % text)
            self.assertEqual(text, '请选择您要发布的产品')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_e_operation_product_click(self):
        """列表中的操作按钮,查看选项，基金名称为：自动化测试产品1"""
        try:
            text = self.driver.operation_product_click()
            logger.info('点击操作按钮，显示的列表第一个为：%s' % text)
            self.assertEqual(text, '编辑')
        except Exception as msg:
            logger.info(msg)
            raise


    def test_f_editor_product_click(self):
        """列表中的操作按钮,点击编辑，基金名称为：自动化测试产品1"""
        try:
            text = self.driver.editor_product_click()
            logger.info('点击操作按钮，点击编辑按钮，显示的结果为：%s' %text)
            self.assertEqual('基本信息', text)
        except Exception as msg:
            logger.info(msg)
            raise


    def test_h_release_product_clcik(self):
        """列表中的操作按钮,点击发布，基金名称为：自动化测试产品1"""
        try:
            text = self.driver.release_product_click()
            logger.info("点击操作按钮，点击发布按钮，显示的提示为：%s" % text)
            self.assertEqual('发布成功!', text)
            try:
                self.mysql.update_mysql("UPDATE run_status SET status='1' WHERE name='test_g_release_product_clcik';")
            except ExecMysql as msg:
                self.mysql.update_mysql("UPDATE run_status SET status='1' WHERE name='test_g_release_product_clcik';")
        except Exception as msg:
            self.mysql.update_mysql("UPDATE run_status SET status='0' WHERE name='test_g_release_product_clcik';")
            logger.info(msg)
            raise

    @unittest.skipUnless(status, '未发布产品列表中产品未发布成功的case没有执行成功，则不执行此case')
    def test_g_delete_product_click(self):
        """列表中的操作按钮,点击删除，基金名称为：自动化测试产品2"""
        try:
            text = self.driver.delete_product_click()
            logger.info('点击操作，点击删除按钮，取确定后，显示的提示为：%s' % text)
            self.assertEqual('删除成功!', text)
        except Exception as msg:
            logger.info(msg)
            raise



if __name__ == '__main__':
    unittest.main()
