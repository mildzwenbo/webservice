"""
@author:fei
@date:2018-7-2
@brief:纰漏信息历史净值页面
"""
import time

from common.pc_login import PCLogin, pc_url, browser
from common.get_url import GetUrl

disclosure_url = GetUrl().pc_url + r'#/informationDisclosure/index'


class NetValueOfHistory(PCLogin):
    #历史净值按钮
    net_value_of_history_loc = ('id', 'tab-0')
    #报告按钮
    report_loc = ('id', 'tab-1')
    #产品名称输入框
    product_name_loc = ('class name', 'el-input__inner')
    #日期输入框
    date_loc = ('class name', 'el-range-input')
    #查询按钮
    search_loc = ('class name', 'el-button')

    def net_value_product_name_input(self, text):
        """
        历史净值页面，产品名称输入
        :return:
        """
        input_elements = self.find_elements(self.product_name_loc)
        input_elements[0].send_keys(text)

    def net_value_date_input(self):
        """
        历史净值页面，对日期的输入
        :return:
        """
        js1 = "document.getElementsByClassName('el-range-input')[0].value = '2018-06-10'"
        js2 = "document.getElementsByClassName('el-range-input')[1].value = '2018-06-17'"
        self.js_execute(js1)
        self.js_execute(js2)

    def net_value_search_click(self):
        """
        在净值页面点击搜索按钮
        :return:
        """
        search = self.find_elements(self.search_loc)[0]
        search.click()

    def report_click(self):
        """
        净值页面，点击进入报告页面
        :return:
        """
        self.click(self.report_loc)

    def net_value_click(self):
        """
        点击进入到净值页面
        :return:
        """
        self.click(self.net_value_of_history_loc)


if __name__ == '__main__':
    driver = browser()
    net = NetValueOfHistory(driver)
    net.open_url(pc_url)
    net.yf_pc_login()
    net.open_url(disclosure_url)
    time.sleep(2)
    net.net_value_product_name_input('P4')
    net.net_value_date_input()
    time.sleep(1)
    net.net_value_search_click()
    net.report_click()
    time.sleep(2)
    net.net_value_click()

