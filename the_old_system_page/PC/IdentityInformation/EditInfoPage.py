"""
@author:xin
@date:2018-5-30
@brief:身份信息-编辑基本信息页面所有元素定位
"""
import time
from the_old_system_page.PC.IdentityInformation import IdentityInfo, pc_url, browser
from selenium.webdriver.common.keys import Keys


class EditInfo(IdentityInfo):
    message_input = ('class name', 'el-input__inner') #身份信息页面-编辑基本信息页面，所有文本框定位
    gender = ('class name', 'el-radio')#身份信息-编辑基本信息页面，性别按钮定位
    certificate = ('class name', 'el-select-dropdown__item')#身份信息-编辑基本信息页面,证件类型定位
    save = ('class name','el-button--medium')#身份信息-编辑基本信息页面,保存按钮定位
    upload_papers = ('id', '1')

    def clear_name(self):
        """清空客户名称文本框内容"""
        name_value = self.find_elements(self.message_input)[0]
        name_value.click()
        name_value.send_keys(Keys.CONTROL, 'a')
        name_value.send_keys(Keys.BACK_SPACE)

    def import_name(self, value):
        """客户名称文本框输入内容"""
        name_value = self.find_elements(self.message_input)[0]
        name_value.send_keys(value)

    def clear_certificate(self):
        """清空证件号码文本框内容"""
        certificate_value = self.find_elements(self.message_input)[3]
        certificate_value.click()
        certificate_value.send_keys(Keys.CONTROL, 'a')
        certificate_value.send_keys(Keys.BACK_SPACE)

    def import_certificate(self, value):
        """证件号码文本框输入内容"""
        certificate_value = self.find_elements(self.message_input)[3]
        certificate_value.send_keys(value)

    def click_man(self):
        """点击性别男"""
        gender_man = self.find_elements(self.gender)[0]
        gender_man.click()

    def click_woman(self):
        """点击性别女"""
        gender_woman = self.find_elements(self.gender)[1]
        gender_woman.click()

    def select_birthday(self, day):
        """点击生日日期"""
        birthday = self.find_elements(self.message_input)[1]
        js1 = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
        self.js_execute(js1)
        birthday.send_keys(Keys.CONTROL, 'a')
        birthday.send_keys(day)
        birthday.send_keys(Keys.TAB)
        time.sleep(2)

    def select_identity_card(self):
        """选择证件类型：身份证"""
        identity_card_text = self.find_elements(self.message_input)[2]  # 文本框定位
        identity_card_text.click()
        time.sleep(1)
        identity_card = self.find_elements(self.certificate)[0]  # 身份证
        identity_card.click()

    def select_passport(self):
        """选择证件类型：护照"""
        identity_card_text = self.find_elements(self.message_input)[2]  # 文本框定位
        identity_card_text.click()
        time.sleep(1)
        passport = self.find_elements(self.certificate)[1]  # 护照
        passport.click()

    def select_HK(self):
        """选择证件类型：港澳居民来往内地通行证"""
        identity_card_text = self.find_elements(self.message_input)[2]  # 文本框定位
        identity_card_text.click()
        time.sleep(1)
        HK = self.find_elements(self.certificate)[2]  # 港澳居民来往内地通行证
        HK.click()

    def select_Taiwan(self):
        """选择证件类型：台湾居民来往大陆通行证"""
        identity_card_text = self.find_elements(self.message_input)[2]  # 文本框定位
        identity_card_text.click()
        time.sleep(1)
        Taiwan = self.find_elements(self.certificate)[3]  # 台湾居民来往大陆通行证
        Taiwan.click()

    def certificate_mub(self, value):
        """输入证件号码"""
        identity_card_text = self.find_elements(self.message_input)[3]  # 文本框定位
        time.sleep(1)
        identity_card_text.click()
        identity_card_text.send_keys(Keys.CONTROL, 'a')
        #identity_card_text.send_keys(Keys.BACK_SPACE)
        identity_card_text.send_keys(value)
        time.sleep(1)
        identity_card_text.send_keys(Keys.TAB)

    def input_emil(self, value):
        """输入邮箱内容"""
        emil_value = self.find_elements(self.message_input)[4]
        emil_value.click()
        emil_value.send_keys(Keys.CONTROL, 'a')
        emil_value.send_keys(value)

    def input_phone(self, value):
        """输入固定电话号码"""
        phone_value = self.find_elements(self.message_input)[5]
        phone_value.click()
        phone_value.send_keys(Keys.CONTROL, 'a')
        phone_value.send_keys(value)

    def input_company(self, value):
        """输入公司信息"""
        company_value = self.find_elements(self.message_input)[6]
        company_value.click()
        company_value.send_keys(Keys.CONTROL, 'a')
        company_value.send_keys(value)

    def input_duty(self, value):
        """输入职务信息"""
        duty_value = self.find_elements(self.message_input)[7]
        duty_value.click()
        duty_value.send_keys(Keys.CONTROL, 'a')
        duty_value.send_keys(value)

    def input_site(self, value):
        """输入地址信息"""
        site_value = self.find_elements(self.message_input)[8]
        site_value.click()
        site_value.send_keys(Keys.CONTROL, 'a')
        site_value.send_keys(value)

    def input_postcode(self, value):
        """输入邮政编码"""
        postcode_value = self.find_elements(self.message_input)[9]
        postcode_value.click()
        postcode_value.send_keys(Keys.CONTROL, 'a')
        postcode_value.send_keys(value)

    def upload(self):
        self.js_scroll_end(0, 500)
        self.click(self.upload_papers)


    def click_save(self):
        """点击确定按钮"""
        self.click(self.save)


if __name__ == '__main__':
    driver = browser()
    ei = EditInfo(driver)
    ei.open_url(pc_url)
    ei.lx_pc_login()
    ei.menu_bar()
    time.sleep(1)
    ei.click_edit()
    ei.certificate_mub('41142519720828083X')
    ei.click_save()
    time.sleep(2)

    # ei.select_birthday('2019-09-09')
    # ei.upload()
    # ei.select_Taiwan()
    # time.sleep(1)
    #ei.input_emil('自动化测试')
    #time.sleep(1)
    #ei.input_emil('ssss')
    # time.sleep(1)
    # ei.input_phone('ssss')
    # time.sleep(1)
    # ei.input_company('ssss')
    # time.sleep(1)
    # ei.input_duty('ssss')
    # time.sleep(1)
    # ei.input_site('ssss')
    # time.sleep(1)
    # ei.input_postcode('ssss')

