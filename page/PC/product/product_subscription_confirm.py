"""
@author:fei
@date:2018-5-30
@brief:申购产品最终的确认页面、填写申购金额页面
"""
import time

from common.pc_login import PCLogin, browser, pc_url
from common.get_url import GetUrl

subscription_confirm_url = GetUrl().get_pc_url()+'#/product/subscribe?fundId=1948&fundName=test基金123&manager=江珊&' \
                                                 'netValue=1.2094&cumulativeNetValue=1.2094&netValueDt=2018-04-26&' \
                                                 'currentYearValue=-0.0165%25&startIndexValue=-0.0165%25&' \
                                                 'fundCreateDate=2017-04-13&briefName=test&productCode=test001&' \
                                                 'fundType=QFII&fundStatus=正在运作&investType=股票类基金&' \
                                                 'investTypeOther=&organizationType=契约型&organizationTypeOther=&' \
                                                 'fundEndDate=2020-04-30&manageType=受托管理&shareType=结构化产品&' \
                                                 'currency=人民币&valuationFrequency=存续期内不估值&' \
                                                 'valuationFrequencyOther=&lever=12&fundManager=吴雪&' \
                                                 'fundOperType=开放式&fundRiskRank=R1&investStrategy=&' \
                                                 'investStrategyOther=123123123&mainInvestOrientation=投资方向123&' \
                                                 'warningLine=1.00&stopLine=0.99&hasCustodian=Yes&outsourcing=&' \
                                                 'outsourcingFeeType=FIXRATE&outsourcingFeePercent=10&buyFee=10&' \
                                                 'purchaseFee=10&redeemFee=10&manageFee=0&custodianHasGuarantee=Yes&' \
                                                 'serviceCharge=0&targetScale=10000.000000&realScale=0.000500&' \
                                                 'investTarget=说明问题123&openDateType=&openDateDes=&latelyOpenDate=&' \
                                                 'totalAssets=5668.951365'


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