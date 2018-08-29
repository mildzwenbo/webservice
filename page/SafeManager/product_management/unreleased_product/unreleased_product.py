"""
@author:fei
@date:2018-08-01
@brief:未发布产品页面所有元素的定位以及操作
"""

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl
import random

unreleased_product_url = GetUrl().get_admin_url() + r'#/productManage/product/notline-fundproduct.html'
from common.exec_mysql import ExecMysql


import time


class UnreleasedProduct(ManagerLogin):
    mysql = ExecMysql()
    sql = "SELECT name FROM product_name WHERE product_name='operation_product_click';"
    search_name = mysql.select_mysql(sql)[0][0]
    """为发布产品页面所有元素的定位以及操作"""
    #查询输入框，0基金名称，1基金编码
    search_loc = ('class name', 'el-input__inner')
    #查询按钮
    search_button_loc = ('class name', 'btnCheck')
    #1登记产品、2模板下载、3导入数据、4导出数据、5产品发布
    elements_loc = ('class name', 'el-button')
    #操作按钮
    operation_loc = ('class name', 'el-dropdown-selfdefine')
    #操作按钮下的列表，9位编辑，10删除，11发布产品
    operation_list_loc = ('class name', 'el-dropdown-menu__item')






    def search_input_name(self, name):
        """
        只输入产品名称，点击搜索
        :return:
        """
        if  self.element_click(self.find_elements(self.search_loc)[0]):
            self.find_elements(self.search_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[0]):
                try:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                except Exception as mag:
                    elements = self.find_elements(('class name', 'el-tooltip'))
                    text = elements[1].text
            return text
        else:
            return '页面无法点击'


    def search_input_code(self, code):
        """
        只输入基金编码，点击搜索
        :return:
        """
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.search_loc)[1].send_keys(code)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[1]):
                try:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                except Exception as mag:
                    elements = self.find_elements(('class name', 'el-tooltip'))
                    text = elements[1].text
            return text
        else:
            return '页面无法点击'

    def registration_of_products(self):
        """
        点击登记产品
        :return:
        """
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.elements_loc)[1].click()

            if self.element_click(self.find_elements(('class name', 'el-input__inner'))[0]):

                text = self.get_text(('css', '.module-title>span'))
            else:
                text = False
            return text
        else:
            return '页面无法点击'



    def download_template_click(self):
        """
        点击模板下载
        :return:
        """
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.elements_loc)[2].click()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            return text

        else:
            return '页面无法点击'



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
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.elements_loc)[5].click()
            text = self.get_text(('class name', 'el-message__content'))
            return text
        else:
            return '页面无法点击'


    def operation_product_click(self):
        """列表中的操作按钮，基金名称为：自动化测试产品1"""


        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.search_loc)[0].send_keys(self.search_name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[1]):
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                text = self.find_elements(self.operation_list_loc)[5].text
                return text
            else:
                return '页面无法点击'
        else:
            return '页面无法点击'


    def editor_product_click(self):
        """列表中的操作按钮,点击编辑，基金名称为：自动化测试产品1"""
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.search_loc)[0].send_keys(self.search_name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[1]):
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.operation_list_loc)[5].click()
                if self.element_click(self.find_elements(('class name', 'el-input__inner'))[0]):
                    text = self.get_text(('css', '.module-title>span'))
                else:
                    text = '页面无法点击'
                return text
            else:
                return '页面无法点击'
        else:
            return '页面无法点击'


    def release_product_click(self):
        """列表中的操作按钮,点击发布，基金名称为：自动化测试产品1"""
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.search_loc)[0].send_keys(self.search_name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[1]):
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.operation_list_loc)[7].click()
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
                return text
            else:
                return '页面无法点击'
        else:
            return '页面无法点击'



    def delete_product_click(self):
        """列表中的操作按钮,点击删除，基金名称为：自动化测试产品2"""
        if self.element_click(self.find_elements(self.search_loc)[1]):
            self.find_elements(self.search_loc)[0].send_keys(self.search_name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_loc)[1]):
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.operation_list_loc)[6].click()
                self.find_elements(('class name', 'el-button--small'))[0].click()
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
                return text
            else:
                return '页面无法点击'
        else:
            return '页面无法点击'



if __name__ == '__main__':
    driver = browser()
    a = UnreleasedProduct(driver)
    a.open_url(manager_url)
    a.yf_manager_login()
    time.sleep(1)
    a.open_url(unreleased_product_url)
    text = a.delete_product_click()


