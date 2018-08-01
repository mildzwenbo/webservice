"""
@author：fei
@date:2018-7-6
@brief:对注册过程中的填写基本信息页面的操作
"""

import platform
import pyvirtualdisplay
import time
import unittest

from the_old_system_page.PC.register.personage_basic_info import PersonageBasicInfo, pc_url, browser, register_confirm_url
from common.log import logger


class TestPersonageBasicInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = pyvirtualdisplay.Display(size=(1280, 900), visible=0)
            cls.display.start()
        cls.browser = browser()
        cls.log = logger
        cls.driver = PersonageBasicInfo(cls.browser)
        cls.driver.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.open_url(register_confirm_url)
        self.driver.pwd_input('abc123456', 'abc123456')
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    def test_basic_next_step_click(self):
        """什么都不填写，点击下一步"""
        try:
            self.driver.basic_next_step_click()
            time.sleep(1)
            # text = self.driver.find_elements(('class name', 'el-message__content"'))[0].text
            text = self.driver.get_text(('class name', 'el-message__content'))
            time.sleep(1)
            self.assertEqual(text, '有填写错误，请检测')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_basic_inputs(self):
        """只选择了证件类型，没有填写证件号"""
        try:
            self.driver.basic_inputs()
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'tips-SFZ'))[0].text
            self.assertEqual(text, '必填项，不能为空')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_basic_identity(self):
        """选择了身份证，输入不正确的格式"""
        try:
            self.driver.basic_identity()
            time.sleep(1)
            text = self.driver.find_elements(('class name', 'tips-SFZ'))[0].text
            self.assertEqual(text, '身份证格式错误，请重新输入')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_basic_correct_info(self):
        """正确的填写到下一个页面"""
        try:
            self.driver.basic_correct_info()
            time.sleep(1)
            text = self.driver.get_text(('css', '#signUpIndex > div > h1'))
            self.assertEqual(text, '完善基本信息与风险等级评定')
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
