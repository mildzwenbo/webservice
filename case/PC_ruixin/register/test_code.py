"""
@author:fei
@date:2017-7-5
@brief:注册过程中输入验证码操作
"""


import pyvirtualdisplay
import platform
import unittest
import time
import ddt

from common.log import logger
from common.read_excel import ReadExcel
from common.get_path import GetPath
from page.PC.register.code import Code, pc_url, register_confirm_url, browser

excel_path = GetPath().get_params_path('register.xlsx')
sheet = "Sheet3"
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestCode(unittest.TestCase):
    """对验证码的操作"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.browser = browser()
        cls.driver = Code(cls.browser)
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
    def test_Code(self, data):
        """对验证码的测试"""
        try:
            print(data['instructions'])
            self.driver.code_input(data['name'], data['phone'], data['select'])
            time.sleep(1)
            if data['select'] != '2':
                text = self.driver.find_elements((data['type'], data['selector']))[0].text
            else:
                text = self.driver.find_elements((data['type'], data['selector']))[12].text
            self.assertEqual(data['result'], text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()


