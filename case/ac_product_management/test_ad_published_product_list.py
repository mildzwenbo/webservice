"""
@author:fei
@date:2018-08-22
@brief:对已发布产品列表的测试
"""


from pyvirtualdisplay import Display
import time
import unittest
import platform


from page.SafeManager.product_management.published_product.published_product_list import PublishedProductList, browser, manager_url, published_product_url
from common.log import logger
from common.exec_mysql import ExecMysql


mysql = ExecMysql()
select_sql = "SELECT status FROM run_status WHERE name='test_g_release_product_click';"
status = int(mysql.select_mysql(select_sql)[0][0])

class TestPublishedProductList(unittest.TestCase):
    """对已发布产列表所有的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = PublishedProductList(cls.browser)
        cls.driver.open_url(manager_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.yf_manager_login()
        time.sleep(1)
        self.driver.open_url(published_product_url)
        time.sleep(2)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def name(self):
        mysql = ExecMysql()
        sql = "select name from search_name where product_name='search_name'"
        name = mysql.select_mysql(sql)[0][0]
        return name

    def name1(self):
        mysql = ExecMysql()
        sql = "select name from search_name where product_name='operation_product_click'"
        name = mysql.select_mysql(sql)[0][0]
        return name


    def test_a_search_name(self):
        """输入基金名称，点击搜素"""
        try:
            name = self.name()
            result = self.driver.search_name(name)
            logger.info("输入基金名称查询的结果为:%s" % result)
            self.assertIn(result, 'product1535605704')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_b_search_code(self):
        """输入基金编码，点击搜素"""
        try:
            name = self.name()
            result = self.driver.search_code(name)
            logger.info("输入基金编码查询的结果为:%s" % result)
            self.assertIn(result, 'product1535605704')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_c_search_admin(self):
        """输入基金管理人，点击搜素"""
        try:
            name = self.name()
            result = self.driver.search_admin(name)
            logger.info("输入基金管理人查询的结果为:%s" % result)
            self.assertIn(result, 'product1535605704')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_d_search_manager(self):
        """输入基金经理，点击搜素"""
        try:
            name = self.name()
            result = self.driver.search_manager(name)
            logger.info("输入基金经理查询的结果为:%s" % result)
            self.assertIn(result, 'product1535605704')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_e_export_button_click(self):
        """不填勾选任何数据，点击导出数据按钮"""
        try:
            result = self.driver.export_button_click()
            logger.info('不填勾选任何数据，点击导出数据按钮,显示的提示为：%s' % result)
            self.assertEqual(result, '请选择您要下架的产品')
        except Exception as msg:
            logger.info(msg)
            raise


    def test_h_history_button_click(self):
        """点击操作按钮列表中的历史净值"""
        try:
            name = self.name()
            result = self.driver.history_button_click(name)
            if result == '无数据':
                pass
            else:
                self.assertEqual(result, name)
        except Exception as msg:
            logger.info(msg)
            raise



    def test_f_operation_click(self):
        """点击列表中的操作按钮"""
        try:
            name = self.name()
            result = self.driver.operation_click(name)
            logger.info('点击操作按钮后显示的数据为：%s' % result)
            self.assertEqual(result, '编辑')
        except Exception as msg:
            logger.info(msg)
            raise



    def test_g_editor_button_click(self):
        """点击操作按钮列表中的编辑"""
        try:
            name = self.name()
            result = self.driver.editor_button_click(name)
            logger.info('点击操作按钮列表中的编辑，显示的数据为：%s' % result)
            self.assertEqual(result, '收起')
        except Exception as msg:
            logger.info(msg)
            raise



    @unittest.skipUnless(status, '该产品没有发布成功')
    def test_i_shelves_confirm_button_click(self):
        """点击操作按钮列表中的产品下架，点击确认按钮，自动化测试产品2"""
        try:
            name = self.name1()
            result = self.driver.shelves_confirm_button_click(name)
            logger.info('点击操作按钮列表中的,点击删除后确定，显示的提示：%s' % result)
            self.assertTrue(result)
        except Exception as msg:
            logger.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()
