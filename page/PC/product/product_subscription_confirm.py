"""
@author:fei
@date:2018-5-30
@brief:申购产品最终的确认页面、填写申购金额页面
"""
import time

from common.pc_login import PCLogin, browser, pc_url
from common.get_url import GetUrl

subscription_confirm_url = GetUrl().get_pc_url()+'#/product/subscribe?fundId=2015&fundName=' \
                                                 '%E8%B5%84%E8%88%9F%E6%8A%95%E8%B5%84%E5%9F%BA%E9%87%91R3&manager=' \
                                                 'test2&netValue=1.0576&cumulativeNetValue=1.0576&netValueDt=2018-06-26' \
                                                 '&currentYearValue=0%25&startIndexValue=-0.03%25&' \
                                                 'fundCreateDate=2018-06-19&briefName=%E8%B5%84%E8%88%9F%E6%8A%95%E8%B5' \
                                                 '%84%E5%9F%BA%E9%87%91R3&productCode=ZZ0001&fundType=%E9%93%B6%E8%A1%8' \
                                                 'C%E7%90%86%E8%B4%A2%E4%BA%A7%E5%93%81&fundStatus=%E6%AD%A3%E5%9C%A8%' \
                                                 'E8%BF%90%E4%BD%9C&investType=%E6%9C%9F%E8%B4%A7%E5%8F%8A%E5%85%B6' \
                                                 '%E4%BB%96%E8%A1%8D%E7%94%9F%E5%93%81%E7%B1%BB%E5%9F%BA%E9%87%91&inv' \
                                                 'estTypeOther=&organizationType=%E5%A5%91%E7%BA%A6%E5%9E%8B&organizati' \
                                                 'onTypeOther=&fundEndDate=9999-12-31&manageType=%E5%8F%97%E6%89%98%E7%' \
                                                 'AE%A1%E7%90%86&shareType=%E4%BC%9E%E5%9E%8B%E5%9F%BA%E9%87%91&currenc' \
                                                 'y=%E4%BA%BA%E6%B0%91%E5%B8%81&valuationFrequency=%E5%AD%98%E7%BB%AD%' \
                                                 'E6%9C%9F%E5%86%85%E4%B8%8D%E4%BC%B0%E5%80%BC&valuationFrequencyOther=' \
                                                 '&lever=0&fundManager=test2&fundOperType=%E5%BC%80%E6%94%BE%E5%BC%8F&' \
                                                 'fundRiskRank=R3&investStrategy=&investStrategyOther=&mainInvestOrient' \
                                                 'ation=test2&warningLine=&stopLine=&hasCustodian=No&outsourcing=&outso' \
                                                 'urcingFeeType=&outsourcingFeePercent=0&buyFee=0&purchaseFee=0&redeem' \
                                                 'Fee=0&manageFee=0&custodianHasGuarantee=&serviceCharge=0&targetScal' \
                                                 'e=100,000.00&realScale=9.99&investTarget=test2&openDateType=&openDate' \
                                                 'es=&latelyOpenDate=&totalAssets=2,632.30'


class SubscriptionConfirm(PCLogin):
    """申购产品的最终页面中的元素和操作方法"""

    check_loc = ('class name', 'el-checkbox__inner') #勾选按钮
    money_loc = ('class name', 'el-input__inner')#金额
    confirm_cancel_button_loc = ('class name', 'el-button')         #取消或确认按钮

    def check_click(self):
        """勾选"""
        self.js_scroll_end(0, 4000)
        self.click(self.check_loc)

    def cancel_button_click(self):
        """点击取消按钮"""
        self.js_scroll_end(0, 4000)
        self.find_elements(self.confirm_cancel_button_loc)[0].click()

    def confirm_button_click(self, number):
        """点击确定按钮"""
        self.check_click()
        self.input_money(number)
        self.find_elements(self.confirm_cancel_button_loc)[1].click()

    def input_money(self, number):
        """输入金额"""
        self.js_scroll_end(0, 2000)
        self.send_keys(self.money_loc, number)

if __name__ == '__main__':
    driver = browser()
    c = SubscriptionConfirm(driver)
    c.open_url(pc_url)
    c.pc_login('15822816936', 'abc123456', '1')
    c.open_url(subscription_confirm_url)
    # c.check_click()
    # c.input_money('20000')
    # c.cancel_button_click()
    c.confirm_button_click('23333')