"""
@author:fei
@date:2018-08-01
@brief:为发布产品页面所有元素的定位以及操作
"""

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl

unreleased_product_url = GetUrl().get_admin_url() + r'#/productManage/product/notline-fundproduct.html'


import time


class UnreleasedProduct(ManagerLogin):
    """为发布产品页面所有元素的定位以及操作"""
    #查询输入框，0基金名称，1基金编码
    search_loc = ('class name', 'el-input__inner')
    #查询按钮
    search_button_loc = ('class name', 'btnCheck')
    #1登记产品、2模板下载、3导入数据、4导出数据、5产品发布
    elements_loc = ('class name', 'el-button')
    #操作按钮
    operation_loc = ('class name', 'el-dropdown-link')






    def search_input_name(self):
        """
        只输入产品名称，点击搜索
        :return:
        """
        self.find_elements(self.search_loc)[0].send_keys('1')
        self.click(self.search_button_loc)

    def search_input_code(self):
        """
        只输入基金编码，点击搜索
        :return:
        """
        self.find_elements(self.search_loc)[1].send_keys('1')
        self.click(self.search_button_loc)

    def registration_of_products(self):
        """
        点击登记产品
        :return:
        """
        self.find_elements(self.elements_loc)[1].click()

    def download_template_click(self):
        """
        点击模板下载
        :return:
        """
        self.find_elements(self.elements_loc)[2].click()


    def import_data_click(self):
        """
        点击导入数据
        :return:
        """
        self.find_elements(self.elements_loc)[3].click()

    def export_data_click(self):
        """
        导出数据
        :return:
        """
        self.find_elements(self.elements_loc)[4].click()


    def product_release(self):
        """
        点击产品发布
        :return:
        """
        self.find_elements(self.elements_loc)[5].click()

    def operation_click(self):
        """列表中的操作按钮，基金名称为：自动化测试产品1"""
        self.find_elements(self.operation_loc)[3].click()


    def editor_click(self):
        """列表中的操作按钮,点击编辑，基金名称为：自动化测试产品1"""
        self.operation_click()
        time.sleep(1)
        self.find_elements(self.operation_loc)











if __name__ == '__main__':
    driver = browser()
    a = UnreleasedProduct(driver)
    a.open_url(manager_url)
    a.yf_manager_login()
    time.sleep(1)
    a.open_url(unreleased_product_url)
    time.sleep(2)
    a.operation_click()

