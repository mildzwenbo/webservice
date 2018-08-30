"""
@author:fei
@date:2018-08-22
@brief:已发布产品页面的元素定位以及操作
"""

import time

from common.manager_login import ManagerLogin, browser, manager_url
from common.get_url import GetUrl
published_product_url = GetUrl().get_admin_url() + '#/productManage/product/online-fundproduct.html'
from common.exec_mysql import ExecMysql



class PublishedProductList(ManagerLogin):
    """已发布产品页面的元素定位以及操作"""
    mysql = ExecMysql()

    #所有输入框的定位， 基金名称：0， 基金编码：1，基金管理人：2， 基金经理：3
    search_input_loc = ('class name', 'el-input__inner')
    # 搜素按钮
    search_button_loc = ('class name', 'btnCheck')
    # 所有列表中的元素
    result_loc = ('class name', 'el-tooltip')

    # 导出和产品下架按钮
    export_shelves_button_loc = ('class name', 'el-button')

    #操作按钮
    operation_loc = ('class name', 'el-dropdown-link')

    #点击操作后显示的列表
    select_list_lc = ('class name', 'el-dropdown-menu__item')



    def search_name(self, name):
        """输入基金名称，点击搜素"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                try:
                    text = self.find_elements(self.result_loc)[1].text
                except Exception as msg:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                return text
            else:
                return "页面不可点击"
        else:
            return "页面不可点击"


    def search_code(self, name):
        """输入基金编码，点击搜素"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[1].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                try:
                    text = self.find_elements(self.result_loc)[1].text
                except Exception as msg:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                return text
            else:
                return "页面不可点击"
        else:
            return "页面不可点击"


    def search_admin(self, name):
        """输入基金管理人，点击搜素"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[2].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                try:
                    text = self.find_elements(self.result_loc)[1].text
                except Exception as msg:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                return text
            else:
                return "页面不可点击"
        else:
            return "页面不可点击"

    def search_manager(self, name):
        """输入基金经理，点击搜素"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[3].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                try:
                    text = self.find_elements(self.result_loc)[1].text
                except Exception as msg:
                    text = self.get_text(('class name', 'el-table__empty-text'))
                return text
            else:
                return "页面不可点击"
        else:
            return "页面不可点击"
            return False

    def export_button_click(self):
        """不填勾选任何数据，点击导出数据按钮"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.export_shelves_button_loc)[2].click()
            time.sleep(1)
            text = self.get_text(('class name', 'el-message__content'))
        else:
            text = '页面不能点击'
        return text


    def move(self):
        """移动滚动条"""
        js = "document.getElementsByClassName('is-scrolling-left')[0].scrollLeft=1000"
        self.js_execute(js)


    def operation_click(self, name):
        """点击操作按钮，自动化测试产品2"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.move()
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                text = self.find_elements(self.select_list_lc)[5].text
            else:
                text = '页面不能点击'
            return text
        else:
            return '页面不能点击'



    def editor_button_click(self, name):
        """点击操作按钮列表中的编辑，自动化测试产品2"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.move()
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.select_list_lc)[5].click()
                if self.element_click(self.find_element(('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/p/span[2]/span[3]'))):
                    text = self.find_elements(('class name', 'el-button'))[0].text
                else:
                    text = "页面不能点击"
                return text
            else:
                return '页面不能点击'
        else:
            return '页面不能点击'





    def history_button_click(self, name):
        """点击操作按钮列表中的历史净值，自动化测试产品2"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.move()
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.select_list_lc)[6].click()
                if self.element_click(self.find_element(
                        ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/p/span[2]/span[3]'))):
                    try:
                        text = self.get_text(('class name', 'el-table__empty-text'))
                    except Exception as msg:
                        text = self.find_elements(('class name', 'el-tooltip'))[0].text
                else:
                    text = "页面不能点击"
                print(text)
                return text
            else:
                return '页面不能点击'
        else:
            return '页面不能点击'



    def shelves_confirm_button_click(self, name):
        """点击操作按钮列表中的产品下架，点击确认按钮，自动化测试产品2"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.move()
                self.find_elements(self.operation_loc)[2].click()
                time.sleep(1)
                self.find_elements(self.select_list_lc)[7].click()
                time.sleep(1)
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
            else:
                text =  '页面不能点击'
            return text
        else:
            return '页面不能点击'



if __name__ == '__main__':
    driver = browser()
    p = PublishedProductList(driver)
    p.open_url(manager_url)
    p.yf_manager_login()
    time.sleep(2)
    p.open_url(published_product_url)
    p.shelves_confirm_button_click('1535596261')
