"""
@author:fei
@date:2018-5-26
@brief:登录页面等测试用例
"""

import platform
from pyvirtualdisplay import Display
import time
import unittest
import ddt

from common.log import logger
from page.PC.IdentityInformation.EditInfoPage import EditInfo, browser, pc_url
from common.get_path import GetPath
from common.read_excel import ReadExcel


excel_path = GetPath().get_params_path('change_information.xlsx')
sheet = 'Sheet1'
data = ReadExcel(excel_path, sheet).data_list()


@ddt.ddt
class TestEditInfo(unittest.TestCase):
    """登录页面等测试用例"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 800))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = EditInfo(cls.driver)
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
        self.browser.lx_pc_login()

    def tearDown(self):
        time.sleep(2)

    #@unittest.skip('pass')
    def test_clean_all(self):
        """清空必填项后点击保存按钮，测试用例"""
        try:
            self.browser.menu_bar()
            time.sleep(1)
            self.browser.click_edit()
            self.browser.clear_name()
            self.browser.clear_certificate()
            time.sleep(1)
            self.browser.click_save()

            el_error1 = ('class name', 'el-form-item__error')
            el_error2 = ('class name', 'tips-SFZ')
            name_error = self.browser.find_element(el_error1).text
            certificate_error = self.browser.find_element(el_error2).text

            self.assertEqual('必填项，不能为空', name_error)
            self.assertEqual('必填项，不能为空', certificate_error)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def edit(self, name, certificate, number, emil, phone, postcode):
        self.browser.menu_bar()
        time.sleep(1)
        self.browser.click_edit()
        self.browser.clear_name()
        self.browser.import_name(name)
        #选择性别
        gender = self.browser.find_elements(self.browser.gender)[0]
        aria_checked = gender.get_attribute('aria-checked')
        if aria_checked == 'true':
            self.browser.click_woman()
        else:
            self.browser.click_man()
        self.browser.select_birthday('1993-01-01')
        # 选择证件类型
        content = self.browser.find_elements(self.browser.message_input)[2]
        value = content.get_attribute('value')
        if value == certificate:
            if value == '身份证':
                self.browser.select_birthday('1993-01-01')
                self.browser.select_Taiwan() #点击台湾居民来往内地通行证
                time.sleep(1)
                self.browser.input_emil(emil)
            elif value == '护照':
                self.browser.select_birthday('1992-06-12')
                self.browser.select_identity_card()#点击身份证
                time.sleep(1)
                self.browser.certificate_mub(number)
            elif value == '港澳居民来往内地通行证':
                self.browser.select_passport()#点击护照
                time.sleep(1)
                self.browser.input_postcode(postcode)
            elif value == '台湾居民来往内地通行证':
                self.browser.select_HK()#点击港澳居民来往内地通行证
                time.sleep(1)
                self.browser.input_phone(phone)
        time.sleep(1)
        self.browser.click_save()



    @ddt.data(*data)
    def test_edit_information(self, data):
        try:
            self.edit(data['name'], data['certificate'], data['number'], data['emil'], data['phone'], data['postcode'])
            time.sleep(2)
            el_error = (data['type'], data['selector'])
            text = self.browser.get_text(el_error)
            self.assertEqual(data['result'], text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

