"""
@author:
@date:2018-5-29
@brief:test基金123产品详情页面
"""
import time

from common.pc_login import pc_url, browser
from page.PC.product.product_list import ProductList
from common.get_url import GetUrl

product_info_url = GetUrl().get_pc_url()+"#/product/detail?code=ZZ0001"


class ProductInfo(ProductList):
    """产品详情页面的元素极其操作"""
    product_element_loc = ('id', 'tab-0')           #产品要素
    the_net_value_of_records_lco = ('id', 'tab-2')  #净值记录
    transaction_list_loc = ('id', 'tab-3')          #交易列表

    subscribe_button_loc = ('xpath', '//*[@id="pane-0"]/div[1]/div[1]/div[2]/div[8]/dl/dd/button')      #申购

    first_data_loc = ('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[3]/div/span')  # 开始时间
    last_data_loc = ('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[7]/div/span')  # 结束时间

    date_loc = ('class name', 'el-range-input') #净值列表和成交列表日期
    # 净值记录列表
    net_worth_search_loc = ('xpath', '//*[@id="pane-2"]/div/div[1]/div[3]/button')  #搜索按钮
    #成交列表
    business_type_loc = ('xpath', '//*[@id="pane-3"]/div/div[1]/div[4]/div/div[1]/input') #业务类型按钮
    subscribe_loc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[2]') #业务类型申购
    redemption_loc = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[3]') #业务类型赎回
    transaction_search_loc = ('xpath', '//*[@id="pane-3"]/div/div[1]/div[5]/button/span')

    def product_element_click(self):
        """点击基本要素"""
        self.click(self.product_element_loc)
        time.sleep(2)

    def the_net_value_of_records_lco_click(self):
        """点击净值记录"""
        self.click(self.the_net_value_of_records_lco)
        time.sleep(2)

    def transaction_list_click(self):
        """点击成交列表"""
        self.click(self.transaction_list_loc)
        time.sleep(2)

    def subscribe_click(self):
        """在基本要素页面点击申购"""
        time.sleep(2)
        self.click(self.subscribe_button_loc)

    def net_worth_date_click(self):
        """点击搜索中的净值日期输入框"""
        element = self.find_elements(self.date_loc)[0]
        element.click()
        time.sleep(2)

    def input_data(self):
        """输入净值列表中的日期"""
        js1 = "document.getElementsByClassName('el-range-input')[0].removeAttribute('readonly')"
        self.js_execute(js1)
        self.find_elements(('class name', 'el-range-input'))[0].send_keys('2018-06-20')
        js2 = "document.getElementsByClassName('el-range-input')[1].removeAttribute('readonly')"
        self.js_execute(js1)
        self.find_elements(('class name', 'el-range-input'))[1].send_keys('2018-06-26')
        time.sleep(1)

    def net_worth_search_click(self):
        """净值列表中的点击操作"""
        self.click(('css', '#pane-2 > div > div:nth-child(1) > div:nth-child(3) > button > span'))

    def input_transaction_date(self):
        """点击成交列表中的日期"""
        js1 = "document.getElementsByClassName('el-range-input')[2].value='2018-06-20'"
        js2 = "document.getElementsByClassName('el-range-input')[3].value='2018-06-26'"
        self.js_execute(js1)
        self.js_execute(js2)
        # self.find_elements(('class name', 'el-range-input'))[2].send_keys('2018-06-20')
        # js2 = "document.getElementsByClassName('el-range-input')[3].removeAttribute('readonly')"
        # self.js_execute(js2)
        # self.find_elements(('class name', 'el-range-input'))[1].send_keys('2018-06-26')
        time.sleep(1)

    def business_type_click(self):
        """点击成交列表中的业务类型"""
        self.click(self.business_type_loc)

    def select_subscribe(self):
        """成交列表中业务类型申购"""
        self.find_elements(('class name', 'el-select-dropdown__item'))[7].click()

    def select_redemption(self):
        """成交列表中业务类型赎回"""
        self.find_elements(('class name', 'el-select-dropdown__item'))[8].click()

    def transaction_search_click(self):
        """成交列表查询按钮"""
        self.click(self.transaction_search_loc)
        time.sleep(1)


if __name__ == '__main__':
    driver = browser()
    info = ProductInfo(driver)
    info.open_url(pc_url)
    info.yf_pc_login()
    info.open_url(product_info_url)
    info.transaction_list_click()
    time.sleep(1)
    info.input_transaction_date()
    info.business_type_click()
    time.sleep(3)
    info.select_subscribe()
    info.transaction_search_click()

    # info.transaction_list_click()
    #     # info.product_element_click()
    # info.subscribe_click()
    # info.input_data()
    # info.business_type_click()
    # info.select_redemption()
    # info.transaction_search_click()


