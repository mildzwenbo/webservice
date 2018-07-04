"""
@author:fei
@date:2018-7-4
@brief:个人和机构注册信息的填写的测试用例
"""

import time
import pyvirtualdisplay
import platform
import unittest
import ddt


from common.log import logger
from page.PC.register.registration_information import RegistrationInformation, browser,pc_url, register_confirm_url
from common.get_path import GetPath
from common.read_excel import ReadExcel

excel_path = GetPath().get_params_path('register.xlsx')
sheet = 'Sheet1'
sheet1 = "Sheet2"
data = ReadExcel(excel_path, sheet).data_list()

institutions_data = ReadExcel(excel_path, sheet1).data_list()


@ddt.ddt
class TestRegistrationInfo(unittest.TestCase):
    """对注册过程中的基本信息输入的测试用"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = pyvirtualdisplay.Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.browser = browser()
        cls.driver = RegistrationInformation(cls.browser)
        cls.driver.open_url(pc_url)
        cls.log = logger

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

    def test_info_personal_do_not_enter(self):
        """个人用户注册不输入任何基本信息，点击下一步，与显示提示做对比"""
        try:
            self.driver.info_personal_not_enter()
            time.sleep(1)
            name_error = self.driver.find_elements(('class name', 'el-form-item__error'))[0].text
            phone_error = self.driver.find_elements(('class name', 'el-form-item__error'))[1].text
            validation_error = self.driver.find_elements(('class name', 'el-form-item__error'))[2].text
            self.assertEqual(name_error, '请输入客户名称')
            self.assertEqual(phone_error, '请输入正确的手机号码')
            self.assertEqual(validation_error, '请输入验证码')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    @ddt.data(*data)
    def test_info_personal_input_info(self, data):
        """个人用户，输入已经注册过的手机号和未注册的手机号进行注册"""
        try:
            print(data['instructions'])
            self.driver.info_personal_input_info(data['name'], data['phone'])
            time.sleep(2)
            if data['phone'] == '17600661017':
                text = self.driver.find_elements((data['select_type'], data['selector']))[0].text
                self.assertEqual(text, data['result'])
            elif data['phone'] == '13944096337':
                text = self.driver.find_elements((data['select_type'], data['selector']))[6].text
                self.assertEqual(text, data['result'])
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_info_institutions_not_enter(self):
        """机构用户不填写任何信息点击下一步"""
        try:
            self.driver.info_institutions_not_enter()
            time.sleep(1)
            institutions_name = self.driver.find_elements(('class name', 'el-form-item__error'))[0].text
            name_error = self.driver.find_elements(('class name', 'el-form-item__error'))[1].text
            phone_error = self.driver.find_elements(('class name', 'el-form-item__error'))[2].text
            validation_error = self.driver.find_elements(('class name', 'el-form-item__error'))[3].text
            self.assertEqual(institutions_name, '请输入机构名称')
            self.assertEqual(name_error, '请输入经办人姓名')
            self.assertEqual(phone_error, '请输入正确的手机号码')
            self.assertEqual(validation_error, '请输入验证码')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    @ddt.data(*institutions_data)
    def test_info_institutions_input_info(self, institutions_data):
        """机构用户输入已经注册的机构名称和未注册的机构名称进入注册"""
        try:
            print(institutions_data['instructions'])
            time.sleep(1)
            self.driver.info_institutions_input_info(institutions_data['institutions_name'], institutions_data['name'], institutions_data['phone'])
            time.sleep(3)
            if institutions_data['phone'] == '17600661017':
                text = self.driver.find_elements((institutions_data['type'], institutions_data['selector']))[0].text
                self.assertEqual(text, institutions_data['result'])
            elif institutions_data['phone'] == '13944096337':
                text = self.driver.find_elements((institutions_data['type'], institutions_data['selector']))[0].text
                self.assertEqual(text, institutions_data['result'])
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()


