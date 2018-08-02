"""
@author:fei
@date:2018-5-30
@brief:申购风险揭示书页面元素，及操作
"""
import time

from the_old_system_page.PC.product.product_list import ProductList, pc_url, browser
from common.get_url import GetUrl

risk_disclosure_url = GetUrl().get_pc_url()+'#/product/riskDisclosure?fundCode=ZZ0001&fundRiskRank='


class RiskDisclosure(ProductList):
    """申购过程中的风险揭示书"""

    list_confirm_button_loc = ('class name', 'el-checkbox__inner')  #列表中所有的确认按钮
    confirm_cancel_button_loc = ('class name', 'el-button')         #取消或确认按钮

    def list_confirm_button_click(self):
        """点击列表中所有的确认按钮"""
        self.js_scroll_end(0, 1200)
        elements = self.find_elements(self.list_confirm_button_loc)
        for i in range(5):
            elements[i].click()
        self.js_scroll_end(0, 2000)
        for i in range(5, 13):
            elements[i].click()

    def cancel_button_click(self):
        """点击取消按钮"""
        self.js_scroll_end(0, 2000)
        self.find_elements(self.confirm_cancel_button_loc)[0].click()

    def confirm_button_click(self):
        """点击确定按钮"""
        self.list_confirm_button_click()
        time.sleep(1)
        self.find_elements(self.confirm_cancel_button_loc)[1].click()


if __name__ == '__main__':
    driver = browser()
    r = RiskDisclosure(driver)
    r.open_url(pc_url)
    r.pc_login('15822816936', 'abc123456', '1')
    r.open_url(risk_disclosure_url)
    time.sleep(2)
    # r.list_confirm_button_click()
    # r.confirm_button_click()
    r.cancel_button_click()


