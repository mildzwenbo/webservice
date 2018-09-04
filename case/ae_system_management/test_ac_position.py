"""
@author:fei
@date:2018-09-03
@brief:对职务页面的测试用例
"""


from pyvirtualdisplay import Display
import platform
import unittest
import time

from common.log import logger
from common.exec_mysql import ExecMysql
from page.SafeManager.system_management.position.position_management import PositionManagement, browser, manager_url, position_management_url

status = ExecMysql().select_mysql("select status from run_status where id=4")[0][0]



class TestPositionManagement(unittest.TestCase):
    """对职务页面的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == "Linux":
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = PositionManagement(cls.browser)
        cls.driver.open_url(manager_url)
        cls.mysql = ExecMysql()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.yf_manager_login()
        if self.driver.element_click(self.driver.find_element(('id', 'institutions'))):
            self.driver.open_url(position_management_url)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_aa_add_button_click(self):
        """点击新增职务按钮"""
        try:
            result = self.driver.add_button_click()
            logger.info('职务管理页面点击添加按钮，显示的元素：%s' % result)
            self.assertEqual(result, '新增职务')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ab_no_input_name_add_department(self):
        """不输入职务名称，点击保存"""
        try:
            result = self.driver.no_input_name_add_position()
            logger.info('职务管理页面点击添加按钮，不输入任何信息，点击保存，显示的提示信息为：%s' % result)
            self.assertEqual(result, '必填项')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ac_add_position(self):
        """新增职务"""
        try:
            name = 'position'+str(int(time.time()))
            result = self.driver.add_position(name)
            logger.info("职务管理页面点击添加按钮，输入职务名称，点击保存，显示的提示信息为：%s" % result)
            if result == "新增成功":
                sql = "UPDATE add_product_name SET product_name='%s' WHERE id=3" % name
                sql1 = "update run_status set status='1' where id=3"
                self.mysql.update_mysql(sql)
                self.mysql.update_mysql(sql1)
            self.assertEqual(result, '新增成功')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ad_exist_name_add(self):
        """添加已经存在的职务名字"""
        try:
            sql = "select name from search_name where id=5"
            name = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.add_position(name)
            logger.info("职务管理页面点击添加按钮，输入已经存在职务名称，点击保存，显示的提示信息为：%s" % result)
            self.assertEqual(result, '职务已存在')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ae_search_department(self):
        """在搜索中输入职务名称，点击搜索"""
        try:
            sql = "select name from search_name where id=5"
            name = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.search_position(name)
            logger.info('在搜索中输入mame,点击搜索，显示的结果为：%s' % result)
            self.assertIn(result, name)
        except Exception as msg:
            logger.info(msg)
            raise


    def test_af_editor_department_click(self):
        """列表中点击编辑按钮"""
        try:
            sql = "select name from search_name where id=5"
            name = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.editor_position_click(name)
            logger.info('列表中点击编辑按钮,显示的提示：%s' % result)
            self.assertEqual(result, '编辑职务')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ag_editor_department(self):
        """编辑职务"""
        try:
            sql = "select name from search_name where id=5"
            name = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.editor_position(name)
            logger.info('编辑职务,点击保存后的提示：%s' % result)
            self.assertEqual(result, '编辑成功')
        except Exception as msg:
            logger.info(msg)
            raise

    @unittest.skipUnless(status, '添加职务失败')
    def test_ah_delete_department(self):
        """删除职务"""
        try:
            sql = "select product_name from add_product_name where id=3"
            name = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.delete_position(name)
            logger.info('删除产品后的提示：%s' % result)
            self.assertEqual(result, '删除成功')
        except Exception as msg:
            logger.info(msg)
            raise


if __name__ == '__main__':
    unittest.main()
