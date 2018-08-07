"""
@author:liuxin
@date:2018-8-2
@brief:数据维护-所有产品页面元素定位
"""

from common.manager_login import ManagerLogin, browser, manager_url
import time


class Product(ManagerLogin):
    data = ('class name', 'el-submenu__title')    # 主导航栏“数据维护”元素定位
    all_product = ('class name', 'el-menu-item')  # 主导航栏“数据维护-所有产品、操作日志”元素定位
    fund_query = ('class name', 'el-input__inner')  # 所有产品页面，查询功能文本框定位
    query_button = ('class name', 'el-button')  # 查询按钮定位
    data_chaining = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/a')  # 数据维护按钮定位
    number = ('class name', 'el-pagination__total')  # 查询结果的个数定位
    no_number = ('class name', 'el-table__empty-text')  # 无数据文本定位
    # fund_name = ('css', '.el-table_1_column_2')  # 列表中“基金名称”定位

    def click_bar(self):
        """点击主导航栏：数据维护-所有产品"""
        self.find_elements(self.data)[2].click()
        self.find_elements(self.all_product)[4].click()

    def query_name(self, value):
        """查询：基金名称字段输入查询内容"""
        time.sleep(1)
        self.find_elements(self.fund_query)[0].send_keys(value)

    def query_code(self, value):
        """查询：基金编码字段输入查询内容"""
        time.sleep(1)
        self.find_elements(self.fund_query)[1].send_keys(value)

    def click_query(self):
        """点击查询按钮"""
        time.sleep(1)
        self.click(self.query_button)

    def query_number(self):
        """获取页面有多少条数据"""
        value = self.find_element(self.number).text
        nub = value[2:-2]
        return nub

    # def fund_name_value(self):
    #     time.sleep(4)
    #     fund_name_text = self.find_elements(self.fund_name)[1]
    #     print(fund_name_text)

    def null_number(self):
        """查询数据为空"""
        value = self.find_element(self.no_number).text
        return value

    def click_date(self):
        """点击操作>数据维护连接"""
        time.sleep(1)
        self.click(self.data_chaining)


if __name__ == '__main__':
    driver = browser()
    p = Product(driver)
    p.open_url(manager_url)
    p.lx_manager_login()
    p.click_bar()
    p.query_name("222")
    # p.click_query()
    time.sleep(1)
    p.click_query()
    time.sleep(1)
    p.null_number()

