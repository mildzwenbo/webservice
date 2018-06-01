"""
@author:fei
@date:2018-5-28
@brief:风险不匹配警示函页面
"""

from common.PC_login import PCLogin, browser, pc_url
from common.get_url import GetUrl
import time


agreement_url = GetUrl().get_pc_url() + r'#/product/agreement'


class Agreement(PCLogin):

    check_loc = ('css', '#app > div > div.main-container > section > div > div:nth-child(2) >'
                        ' p:nth-child(4) > label > span > span')            #勾选按钮

    button_loc = ('class name', 'is-plain')                                 #确认或取消按钮

    def check_click(self):
        """勾选"""
        self.click(self.check_loc)

    def affirm_click(self):
        """取消按钮"""
        affirm_element = self.find_elements(self.button_loc)[0]
        affirm_element.click()

    def confirm_click(self):
        """确认按钮"""
        confirm_element = self.find_elements(self.button_loc)[1]
        confirm_element.click()


if __name__ == '__main__':
    driver = browser()
    a = Agreement(driver)
    a.open_url(pc_url)
    a.pc_login('15822816936', 'abc123456', '1')
    a.open_url(agreement_url)
    time.sleep(1)
    a.check_click()
    # a.affirm_click()
    a.confirm_click()