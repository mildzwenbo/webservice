"""
@author：fei
@date：2018-09-03
@brief：对用户管理页面的测试用例
"""


import unittest
import platform
from pyvirtualdisplay import Display
import time
import random


from common.log import logger
from common.exec_mysql import ExecMysql
from page.SafeManager.system_management.user_management.user_managerment import UserManagement, browser, manager_url, user_management_url


class TestUserManagement(unittest.TestCase):
    """对用户管理页面的测试用例"""

    def get_status(self):
        sql = 'select status from run_status where id=5'
        status = ExecMysql().select_mysql('select status from run_status where id=5')[0][0]
        return status

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == "Linux":
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = UserManagement(cls.browser)
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
            self.driver.open_url(user_management_url)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_aa_add_button_click(self):
        """点击新增用户按钮"""
        try:
            result = self.driver.add_button_click()
            logger.info('点击新增用户按钮，返回的结果为：%s' % result)
            self.assertEqual(result, '新增用户')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ab_no_input_name_add_user(self):
        """不输入任何信息，点击保存"""
        try:
            result = self.driver.no_input_name_add_user()
            logger.info('不输入任何信息，点击保存,返回的结果为：%s' % result)
            self.assertEqual(result, '必填项')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ac_add_user(self):
        """新增用户"""
        try:
            id = 'ID' + str(int(time.time()))
            name = 'username' + str(int(time.time()))
            phone  = '139'+str(random.randint(10000000, 999999999))
            email = str(random.randint(10000000, 999999999)) + "@pb-station.com"
            result = self.driver.add_user(id, name, phone, email)
            logger.info('新增用户，返回的结果为：%s' % result)
            if result == '新增成功':
                id_sql = "update add_product_name set product_name='%s' where id=4" % id
                phone_sql = "update add_product_name set product_name='%s' where id=5" % phone
                email_sql = "update add_product_name set product_name='%s' where id=6" % email
                name_sql = "update add_product_name set product_name='%s' where id=7" % name
                run_status = "update run_status set status='1' where id=5"
                self.mysql.update_mysql(id_sql)
                self.mysql.update_mysql(phone_sql)
                self.mysql.update_mysql(email_sql)
                self.mysql.update_mysql(name_sql)
                self.mysql.update_mysql(run_status)
            self.assertEqual(result, '新增成功')
        except Exception as msg:
            run_status = "update run_status set status='0' where id=5"
            self.mysql.update_mysql(run_status)
            logger.info(msg)
            raise

    @unittest.skipUnless(int(ExecMysql().select_mysql('select status from run_status where id=5')[0][0]), '添加用户的case执行失败')
    def test_ad_user_exist_id(self):
        """添加已经存在的ID"""
        try:
            id = self.mysql.select_mysql("select product_name from add_product_name where id=4")
            name = 'username' + str(int(time.time()))
            phone = '139' + str(random.randint(10000000, 999999999))
            email = str(random.randint(10000000, 999999999)) + "@pb-station.com"
            result = self.driver.add_user(id, name, phone, email)
            logger.info('添加已经存在的ID,返回的结果为：%s' % result)
            self.assertEqual(result, '用户ID已存在')
        except Exception as msg:
            logger.info(msg)
            raise

    @unittest.skipUnless(int(ExecMysql().select_mysql('select status from run_status where id=5')[0][0]), '添加用户的case执行失败')
    def test_ae_user_exist_telephone(self):
        """添加已经存在的电话号"""
        try:
            id = 'ID' + str(int(time.time()))
            name = 'username' + str(int(time.time()))
            phone = self.mysql.select_mysql("select product_name from add_product_name where id=5")
            email = str(random.randint(10000000, 999999999)) + "@pb-station.com"
            result = self.driver.add_user(id, name, phone, email)
            logger.info('添加已经存在的ID,返回的结果为：%s' % result)
            self.assertEqual(result, '手机号已存在')
        except Exception as msg:
            logger.info(msg)
            raise

    @unittest.skipUnless(int(ExecMysql().select_mysql('select status from run_status where id=5')[0][0]),
                         '添加用户的case执行失败')
    def test_af_user_exist_email(self):
        """添加已经存在的电话号"""
        try:
            id = 'ID' + str(int(time.time()))
            name = 'username' + str(int(time.time()))
            phone = '139' + str(random.randint(10000000, 999999999))
            email = self.mysql.select_mysql("select product_name from add_product_name where id=6")
            result = self.driver.add_user(id, name, phone, email)
            logger.info('添加已经存在的ID,返回的结果为：%s' % result)
            self.assertEqual(result, '邮箱已存在')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ag_search_user(self):
        """在搜索中输入mame,点击搜索"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.search_user(username)
            logger.info('在搜索中输入mame,点击搜索,返回的结果为：%s' % result)
            self.assertIn(username, result)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ah_click_product(self):
        """点击操作列表中的产品"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.click_product(username)
            logger.info('点击操作列表中的产品,返回的结果为：%s' % result)
            self.assertEqual(result, '产品分配')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ai_allocation_user(self):
        """在产品分配中分配产品"""
        try:
            sql = "select name from search_name where id=6"
            sql1 = "select name from search_name where id=7"
            username = self.mysql.select_mysql(sql)[0][0]
            name = self.mysql.select_mysql(sql1)[0][0]
            result = self.driver.allocation_user(username, name)
            logger.info('在产品分配中分配产品,返回的结果为：%s' % result)
            if result == "暂无数据":
                run_status = "update run_status set status='1' where id=6"
                self.mysql.update_mysql(run_status)
            self.assertEqual(result, '暂无数据')
        except Exception as msg:
            run_status = "update run_status set status='0' where id=6"
            self.mysql.update_mysql(run_status)
            logger.info(msg)
            raise

    @unittest.skipUnless(int(ExecMysql().select_mysql('select status from run_status where id=6')[0][0]),'分配产品的测试用例执行失败')
    def test_aj_remove_product(self):
        """移除分配的产品"""
        try:
            sql = "select name from search_name where id=6"
            sql1 = "select name from search_name where id=7"
            username = self.mysql.select_mysql(sql)[0][0]
            name = self.mysql.select_mysql(sql1)[0][0]
            result = self.driver.remove_product(username, name)
            logger.info('在产品分配中移除产品,返回的结果为：%s' % result)
            self.assertEqual(result, '暂无数据')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ak_reset_password_click(self):
        """点击重置密码按钮"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.reset_password_click(username)
            logger.info('点击重置密码,返回的结果为:%s' % result)
            self.assertEqual(result, "修改密码")
        except Exception as msg:
            logger.info(msg)
            raise

    def test_al_reset_password(self):
        """重置密码"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.reset_password(username)
            logger.info('重置密码,返回的结果为:%s' % result)
            self.assertEqual(result, "修改成功")
        except Exception as msg:
            logger.info(msg)
            raise

    def test_am_permission_to_view_click(self):
        """点击查看权限按钮"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.permission_to_view_click(username)
            logger.info('查看权限密码,返回的结果为:%s' % result)
            self.assertEqual(result, '权限查看')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_an_editor_user_click(self):
        """点击编辑按钮"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.editor_user_click(username)
            logger.info('点击编辑按钮,返回的结果为:%s' % result)
            self.assertEqual(result, '编辑用户')
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ao_editor_user(self):
        """编辑用户"""
        try:
            sql = "select name from search_name where id=6"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.editor_user(username)
            logger.info('编辑用户,返回的结果为:%s' % result)
            self.assertEqual(result, '编辑成功')
        except Exception as msg:
            logger.info(msg)
            raise

    @unittest.skipUnless(int(ExecMysql().select_mysql('select status from run_status where id=5')[0][0]),'添加用户的case执行失败')
    def test_ap_delete_user(self):
        """删除用户"""
        try:
            sql = "select product_name from add_product_name where id=7"
            username = self.mysql.select_mysql(sql)[0][0]
            result = self.driver.delete_user(username)
            logger.info('删除用户后得到的提示为：%s' % result)
            self.assertEqual(result, '删除成功')
        except Exception as msg:
            logger.info(msg)
            raise


if __name__ == '__main__':
    unittest.main()

