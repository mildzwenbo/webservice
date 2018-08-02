"""
@author:fei
@date:2018-7-5
@brief:注册也买最后对密码的测试用例
"""


import pyvirtualdisplay
import ddt
import unittest
import platform
import time


from the_old_system_page.PC.register.input_pwd import InputPwd, pc_url, register_confirm_url, browser
from common.get_path import GetPath
from common.read_excel import ReadExcel
from common.log import logger

excel_path = GetPath().get_params_path('register.xlsx')
sheet = 'Sheet4'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestInputPwd(unittest.TestCase):
    """注册页面密码输入测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = InputPwd(cls.browser)
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
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @ddt.data(*data)
    def test_pwd_input(self, data):
        try:
            print(data['instructions'])
            self.driver.pwd_input(data['pwd1'], data['pwd2'])
            time.sleep(1)
            if data['select'] == '1' or data['select'] == 2:
                result_error1 = self.driver.find_elements((data['type1'], data['selector1']))[0].text
                result_error2 = self.driver.find_elements((data['type2'], data['selector2']))[1].text
                self.assertEqual(data['result1'], result_error1)
                self.assertEqual(data['result2'], result_error2)
            elif data['select'] == '3':
                result = self.driver.get_text((data['type1'], data['selector1']))
                self.assertEqual(result, data['result1'])

        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()