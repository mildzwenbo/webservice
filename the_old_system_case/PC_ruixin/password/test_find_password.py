"""
@author:xin
@date:2018-7-5
@brief:投资者PC端：登录页面-修改密码
"""

import platform
import time
import unittest

from pyvirtualdisplay import Display

from common.log import logger
from the_old_system_page.PC.password.find_password import ForgotPassword, browser, pc_url


class FindPassword(unittest.TestCase):
    """登录页面-修改密码页面"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 800))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = ForgotPassword(cls.driver)
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        self.browser.open_url(pc_url)

    def tearDown(self):
        time.sleep(2)

    def test_all_empty(self):
        # 不输入任何内容情况下，点击下一步按钮测试用例
        self.browser.click_next_step()
        all_error = ('class name', 'el-form-item__error')
        phone_mub = self.browser.find_elements(all_error)[0].text
        investor_type = self.browser.find_elements(all_error)[1].text
        custodian = self.browser.find_elements(all_error)[2].text
        verify = self.browser.find_elements(all_error)[3].text

        self.assertEqual(phone_mub, '请输入正确的手机号码')
        self.assertEqual(investor_type, '请选择投资者类型')
        self.assertEqual(custodian, '请选择基金管理人')
        self.assertEqual(verify, '请输入验证码')

    def test_verify_error(self):
        # 验证码输入错误测试用例
        self.browser.input_phone('15822816936')
        self.browser.select_personage_investor()
        time.sleep(1)
        self.browser.select_custodian()
        self.browser.input_verify(111)
        self.browser.click_next_step()
        error = ('class name', 'el-form-item__error')
        error_text = self.browser.find_element(error).text
        self.assertEqual(error_text, '验证码错误')

    def test_verify_correct (self):
        # 个人客户：所有文本框输入正确，点击下一步按钮跳转到下一页
        self.browser.input_phone('15822816936')
        self.browser.select_personage_investor()
        time.sleep(1)
        self.browser.select_custodian()
        self.browser.input_verify()
        self.browser.click_next_step()
        time.sleep(1)
        verify = ('class name', 'el-form-item__content')
        verify_text = self.browser.find_elements(verify)[6].text
        self.assertEqual(verify_text, '15822816936')

    def test_get_code(self):
        """获取正确的验证码"""
        self.browser.change_password('15822816936', '1')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        number = ('class name', 'el-form-item__content')
        number_text = self.browser.find_elements(number)[8].text
        self.assertEqual(number_text, '15822816936')

    def test_error_get_code(self):
        """输入错误的验证码"""
        self.browser.change_password('15822816936', '1')
        self.browser.find_elements(self.browser.text_block)[5].send_keys('aa')
        self.browser.click_next_step()
        time.sleep(1)
        error_text = self.browser.find_element(('class name', 'el-message')).text
        self.assertEqual(error_text, '验证码错误')

    def test_empty_code(self):
        """输入错误的验证码"""
        self.browser.change_password('15822816936', '1')
        time.sleep(1)
        self.browser.click_next_step()
        time.sleep(1)
        error_text = self.browser.find_element(('class name', 'el-message')).text
        self.assertEqual(error_text, '请输入验证码')

    def test_empty_password(self):
        """不输入密码，点击确定按钮"""
        self.browser.change_password('15822816936', '1')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        error = self.browser.find_elements(('class name', 'el-form-item__error'))
        error_text1 = error[0].text
        error_text2 = error[1].text
        self.assertEqual(error_text1, '新密码需同时包含字母与数字，长度8-20字符,请再次输入密码')
        self.assertEqual(error_text2, '请再次输入密码')

    def test_empty_password(self):
        """输入两次密码不相同，点击确定按钮"""
        self.browser.change_password('15822816936', '1')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        self.browser.new_password('qwe123456')
        self.browser.confirm_password('abc123')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        error = self.browser.find_element(('class name', 'el-form-item__error')).text
        self.assertEqual(error, '两次输入密码不一致!')

    def test_password_flow(self):
        """个人客户：成功修改密码的流程"""
        self.browser.change_password('15822816936', '1')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('qwe123456')
        self.browser.confirm_password('qwe123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'qwe123456')
        self.browser.find_elements(('class name', 'svg-container'))[3].click()
        self.browser.find_elements(('class name', 'el-button--primary'))[1].click()
        self.browser.open_url(pc_url)
        self.browser.change_password('15822816936', '1')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('abc123456')
        self.browser.confirm_password('abc123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'abc123456', '1')
        time.sleep(1)
        title = self.browser.find_element(('class name', 'no-redirect')).text
        self.assertEqual(title, '产品列表')

    def test_organization_password(self):
        """机构客户：成功修改密码的流程"""
        self.browser.change_password('15822816936', '2')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('qwe123456')
        self.browser.confirm_password('qwe123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'qwe123456', '2')
        self.browser.find_elements(('class name', 'svg-container'))[3].click()
        self.browser.find_elements(('class name', 'el-button--primary'))[1].click()
        self.browser.open_url(pc_url)
        self.browser.change_password('15822816936', '2')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('abc123456')
        self.browser.confirm_password('abc123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'abc123456', '2')
        time.sleep(1)
        title = self.browser.find_element(('class name', 'no-redirect')).text
        self.assertEqual(title, '产品列表')

    def test_product_password(self):
        """产品客户：成功修改密码的流程"""
        self.browser.change_password('15822816936', '3')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('qwe123456')
        self.browser.confirm_password('qwe123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'qwe123456', '3')
        self.browser.find_elements(('class name', 'svg-container'))[3].click()
        self.browser.find_elements(('class name', 'el-button--primary'))[1].click()
        self.browser.open_url(pc_url)
        self.browser.change_password('15822816936', '3')
        self.browser.input_get_code('15822816936')
        self.browser.click_next_step()
        time.sleep(1)
        self.browser.new_password('abc123456')
        self.browser.confirm_password('abc123456')
        self.browser.find_elements(('class name', 'el-button--primary'))[2].click()
        time.sleep(1)
        self.browser.lx_pc_login('15822816936', 'abc123456', '3')
        time.sleep(1)
        title = self.browser.find_element(('class name', 'no-redirect')).text
        self.assertEqual(title, '产品列表')


if __name__ == '__main__':
    unittest.main()

