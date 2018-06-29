"""
@author:xin
@date:2018-5-28
@brief:身份信息页面所有元素定位及操作
"""
import time
from common.pc_login import PCLogin, pc_url, browser


class IdentityInfo(PCLogin):
    identity = ('class name', 'svg-container')#页面右上角人头图标定位
    centre = ('class name', 'el-dropdown-menu__item')#个人中心定位
    link = ('class name', 'el-button')#身份信息页面，所有链接按钮的定位

    def menu_bar(self):
        """点击右上角人头图标下的个人中心"""
        personal_center = self.find_elements(self.identity)[2]
        personal_center.click()

    def click_pwd(self):
        """点击身份信息页面，修改密码链接"""
        elements = self.find_elements(self.link)[0]
        elements.click()

    def click_phone(self):
        """点击身份信息页面，更换手机号链接"""
        elements = self.find_elements(self.link)[1]
        elements.click()

    def click_investors(self):
        """点击身份信息页面，申请转化投资者类型链接"""
        elements = self.find_elements(self.link)[2]
        elements.click()

    def click_risk(self):
        """点击身份信息页面，重新评定投资者风险等级链接"""
        elements = self.find_elements(self.link)[3]
        elements.click()

    def click_edit(self):
        """点击身份信息页面，编辑基本信息链接"""
        elements = self.find_elements(self.link)[4]
        elements.click()


if __name__ == '__main__':
    driver = browser()
    Iinfo = IdentityInfo(driver)
    Iinfo.open_url(pc_url)
    Iinfo.lx_pc_login()
    time.sleep(2)
    Iinfo.menu_bar()
    Iinfo.click_edit()
    # time.sleep(2)
    # Iinfo.click_phone()