"""
@author:xin
@date:2018-5-29
@brief:身份信息-修改密码页面测试用例
"""

import platform
from pyvirtualdisplay import Display
import time
import unittest

from common.log import logger
from page.PC.IdentityInformation.ChangePasswordPage import ChangePassword, browser, pc_url


class ChangePwd(unittest.TestCase):
    """身份信息-修改密码页面测试用例"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(800, 900))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = ChangePassword(cls.driver)
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
        self.browser.pc_login('15822816936', 'abc123456')

    def tearDown(self):
        time.sleep(2)

    #@unittest.skip('pass')
    def test_input_pwd(self):
        """身份信息-修改密码流程测试用例"""
        try:

            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            self.browser.old_pwd('abc123456')
            time.sleep(1)
            self.browser.new_pwd('qwer123456')
            time.sleep(1)
            self.browser.affirm_pwd('qwer123456')
            time.sleep(1)
            self.browser.click_confirm()
            time.sleep(1)
            self.browser.pc_login('15822816936', 'qwer123456')
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            time.sleep(1)
            self.browser.old_pwd('qwer123456')
            time.sleep(1)
            self.browser.new_pwd('abc123456')
            time.sleep(1)
            self.browser.affirm_pwd('abc123456')
            time.sleep(1)
            self.browser.click_confirm()
            time.sleep(1)
            self.browser.pc_login('15822816936', 'abc123456')
            title = ('class name', 'no-redirect')
            title = self.browser.get_text(title)
            self.assertEqual('产品列表', title)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_input_null(self):
        """身份信息-修改密码页面，不输入任何内容，测试用例"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            self.browser.click_confirm()
            time.sleep(1)
            el_error = ('class name', 'el-form-item__error')
            error_message = self.browser.find_elements(el_error)
            old_pwd_error = error_message[0].text
            new_pwd_error = error_message[1].text
            affirm_pwd_error = error_message[2].text

            self.assertEqual('旧密码输入有误',old_pwd_error)
            self.assertEqual('新密码需同时包含字母与数字，长度8-20字符', new_pwd_error)
            self.assertEqual('请再次输入密码', affirm_pwd_error)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_input_inconformity(self):
        """身份信息-修改密码页面，两次输入的新密码不一致，测试用例"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            time.sleep(1)
            self.browser.old_pwd('abc123456')
            time.sleep(1)
            self.browser.new_pwd('qwer123456')
            time.sleep(1)
            self.browser.affirm_pwd('123456')
            time.sleep(1)
            self.browser.click_confirm()
            time.sleep(1)
            el_error = ('class name', 'el-form-item__error')
            error_message = self.browser.get_text(el_error)
            self.assertEqual('两次输入密码不一致!', error_message)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_input_oldpaw(self):
        """身份信息-修改密码页面，旧密码输入有误，测试用例"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_pwd()
            time.sleep(1)
            self.browser.old_pwd('qwer123456')
            time.sleep(1)
            self.browser.new_pwd('qwe123456')
            time.sleep(1)
            self.browser.affirm_pwd('qwe123456')
            time.sleep(1)
            self.browser.click_confirm()
            time.sleep(1)
            el_error = ('class name', 'el-form-item__error')
            error_message = self.browser.get_text(el_error)
            self.assertEqual('旧密码输入有误', error_message)
        except Exception as msg:
            self.log.info(str(msg))
            raise

if __name__ == '__main__':
    unittest.main()


