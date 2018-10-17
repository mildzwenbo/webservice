"""
@author:fei
@date:2018-98-21
@brief:登记产品页面的测试用例
"""

import unittest
from pyvirtualdisplay import Display
import time
import platform
from random import randint


from page.SafeManager.product_management.unreleased_product.registration_of_products import RegistrationOfProduct, browser, manager_url, registration_of_product_url
from common.log import logger
from common.exec_mysql import ExecMysql


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
            logger.info('不输入任何信息点击保存按钮，显示的提示：%s' % result)
            self.assertEqual(result, '有必填项未填写或输入有误')
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
        name = 'product'+str(int(time.time()))
        mysql = ExecMysql()
        code = str(randint(100000, 999999))
        sql = "UPDATE add_product_name SET product_name='%s' WHERE name='test_ac_input_something';" % name
        mysql.update_mysql(sql)
        try:
            text = self.driver.input_something(name, name, code)
            logger.info('正常输入信息点击保存，显示的提示为：%s' % text)
            self.assertEqual('保存成功',text)
            sql1 = "UPDATE run_status SET status='1' WHERE name='test_ac_input_something';"
            mysql.update_mysql(sql1)
        except Exception as msg:
            logger.info(msg)
            sql2 = "UPDATE run_status SET status='0' WHERE name='test_ac_input_something';"
            mysql.update_mysql(sql2)
            raise



    def test_ad_existing_name(self):
        """输入的产品名称已经，点存在击保存"""
        try:
            mysql = ExecMysql()
            sql = "SELECT product_name FROM add_product_name WHERE name='test_ac_input_something';"
            existing_name = mysql.select_mysql(sql)[0][0]
            other_name = str(int(time.time()))
            text = self.driver.input_something(existing_name, other_name, other_name)
            logger.info('输入已经存在的产品名称点击保存，显示的提示为：%s' % text)
            self.assertEqual('产品名称已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_af_existing_code(self):
        """输入已经存在的简称，点击保存"""
        try:
            mysql = ExecMysql()
            sql = "SELECT product_name FROM add_product_name WHERE name='test_ac_input_something';"
            existing_name = mysql.select_mysql(sql)[0][0]
            name = str(int(time.time()))
            text = self.driver.input_something(name, existing_name, name)
            logger.info('输入已经存在的产品简称点击保存，显示的提示为：%s' % text)
            self.assertEqual('产品简称已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

    def test_ae_existing_name2(self):
        """输入已经存在的编码，点击保存"""
        try:
            # mysql = ExecMysql()
            # sql = "SELECT product_name FROM add_product_name WHERE name='test_ac_input_something';"
            # existing_code = mysql.select_mysql(sql)[0][0]
            name = str(int(time.time()))
            existing_code = 'produc'
            text = self.driver.input_something(name, name, existing_code)
            logger.info('输入已经存在的产品编码点击保存，显示的提示为：%s' % text)
            self.assertEqual('编码已存在', text)
        except Exception as msg:
            logger.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()
