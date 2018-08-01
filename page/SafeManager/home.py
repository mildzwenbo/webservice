"""
@author:fei
@date:2018-7-31
@brief:首页的多有元素的以及其操作
"""

from common.manager_login import ManagerLogin, browser, manager_url
from common.get_url import GetUrl
import time


class Home(ManagerLogin):
    #产品管理快捷入口
    product_management_loc = ('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.main_header > ul > li.main-bgitem > a > span')
    #数据维护入口
    data_management_loc = ('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.main_header > ul > li.main-bgitem2 > a')
    #系统管理入口
    system_management_loc = ('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.main_header > ul > li.main-bgitem3 > a > span')



    def product_management_click(self):
        """
        点击快捷入口的产品管理
        :return:
        """
        self.click(self.product_management_loc)

    def data_management_click(self):
        """
        点击快捷入口数据管理
        :return:
        """
        self.click(self.data_management_loc)

    def system_management_click(self):
        """
        点击快捷入口系统管理
        :return:
        """
        self.click(self.system_management_loc)




if __name__ == '__main__':
    driver = browser()
    home = Home(driver)
    home.open_url(manager_url)
    home.yf_manager_login()
    home.data_management_click()



