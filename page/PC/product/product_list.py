"""
@author:
@date:
@brief: 缺省消息提醒按钮的定位， 点击消息的方法
"""

from common.PC_login import PCLogin, browser, pc_url
import time


class ProductList(PCLogin):

    home_loc = ('link text', 'Home')                            #Home按钮
    username_loc = ('css', '#app > div > div.main-container > ul > div.right-menu > a:nth-child(2) > span > svg')                        #用户名
    search_input_loc = ('class name', 'el-input__inner')        #输入框
    search_loc = ('class name', 'el-button--medium')            #点击输入按钮、更高风险等级按钮，
                                                                # 列表中产品操作栏中的查看按钮

    quit_loc = ('class name', 'svg-container')              #退出按钮

    def home_click(self):
        """点击Home按钮"""
        self.click(self.home_loc)

    def username_click(self):
        """点击用户名"""
        self.click(self.username_loc)

    def input_search(self, text):
        """搜索输入框中输入"""
        elements = self.find_elements(self.search_input_loc)[1]
        elements.send_keys(text)

    def search_click(self):
        """点击查询按钮"""
        elements = self.find_elements(self.search_loc)[0]
        elements.click()

    def risk_level_click(self):
        """"""
        elements = self.find_elements(self.search_loc)[1]
        elements.click()

    def product_search_click(self):
        """点击列表中第一个产品操作中的查询按钮"""
        elements = self.find_elements(self.search_loc)[2]
        elements.click()

    def personal_information_click(self):
        """点击个人中心"""
        self.find_elements(self.quit_loc)[0].click()

    def quit_click(self):
        """点击退出按钮"""
        self.find_elements(self.quit_loc)[2].click()



if __name__ == '__main__':
    driver = browser()
    h = ProductList(driver)
    h.open_url(pc_url)
    h.pc_login('15822816936', 'abc123456', '1')
    h.input_search('测试')
    time.sleep(1)
    h.search_click()


