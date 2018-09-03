"""
@author:liuxin
@ad_date:2018-8-24
@brief:系统管理-角色管理页面测试用例
"""

import unittest
import platform
from pyvirtualdisplay import Display
import time

from selenium.webdriver.common.keys import Keys
from page.SafeManager.system.role import RoleManage, browser, manager_url
from common.log import logger


class AllProducts(unittest.TestCase):
    """对系统管理-角色管理页面所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(5120, 2880))
            cls.display.start()
        cls.browser = browser()
        cls.driver = RoleManage(cls.browser)
        cls.driver.open_url(manager_url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.lx_manager_login()
        self.driver.role_bar()

    def tearDown(self):
        time.sleep(1)

    def test_aa_select(self):
        """查询功能测试用例"""
        try:
            self.driver.select_role('主管')
            mub = self.driver.query_number()
            self.assertEqual(mub, '1')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_ab_empty_role(self):
        """新增角色弹框，不输入内容，点击确定按钮"""
        try:
            self.driver.add_button()
            self.driver.new_confirm()
            error = self.driver.find_element(('class name', 'el-form-item__error')).text
            self.assertEqual(error, '必填项，不能为空')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_ac_add_role(self):
        """新增角色成功"""
        try:
            self.driver.add_button()
            self.driver.input_role('自动化测试')
            self.driver.new_confirm()
            time.sleep(1)
            error = self.driver.find_element(('class name', 'el-message--success')).text
            self.assertEqual(error, '添加成功')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_ad_jurisdiction(self):
        """点击权限设置按钮"""
        try:
            time.sleep(1)
            self.driver.jurisdiction_set()
            time.sleep(1)
            error = self.driver.find_elements(('class name', 'el-dialog__title'))[1].text
            self.assertEqual(error, '编辑权限')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_ae_edit(self):
        """点击编辑按钮"""
        try:
            self.driver.edit_set()
            input_value = self.driver.find_elements(self.driver.role_name)[3]
            input_value.send_keys(Keys.CONTROL, 'a')
            self.driver.input_role('测试001')
            self.driver.new_confirm()
            time.sleep(1)
            error = self.driver.find_element(('class name', 'el-message--success')).text
            self.assertEqual(error, '编辑成功')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_af_delete_cancel(self):
        """点击删除按钮，显示弹框，点击取消按钮"""
        try:
            self.driver.delete_set()
            self.driver.hint_cancel()
            time.sleep(1)
            error = self.driver.find_element(('class name', 'el-message--info')).text
            self.assertEqual(error, '已取消删除')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_ag_delete_loser(self):
        """删除已关联用户的角色-失败"""
        try:
            self.driver.delete_set()
            self.driver.hint_confirm()
            time.sleep(1)
            error = self.driver.find_element(('class name', 'el-message--warning')).text
            self.assertEqual(error, '该角色已关联用户，不可删除')
        except Exception as msg:
            logger.info(str(msg))
            raise

    def test_af_delete_succeed(self):
        """删除已关联用户的角色-成功"""
        try:
            self.driver.select_role('测试001')
            time.sleep(1)
            self.driver.find_element(('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div/a[3]')).click()
            self.driver.hint_confirm()
            time.sleep(1)
            error = self.driver.find_element(('class name', 'el-message--success')).text
            self.assertEqual(error, '删除成功')
        except Exception as msg:
            logger.info(str(msg))
            raise




if __name__ == '__main__':
    unittest.main()

