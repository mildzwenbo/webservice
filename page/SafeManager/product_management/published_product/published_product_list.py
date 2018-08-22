"""
@author:fei
@date:2018-08-22
@brief:已发布产品页面的元素定位以及操作
"""

import time

from common.manager_login import ManagerLogin, browser, manager_url
from common.get_url import GetUrl
published_product_url = GetUrl().get_admin_url() + '#/productManage/product/online-fundproduct.html'


class PublishedProductList(ManagerLogin):
    """已发布产品页面的元素定位以及操作"""
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

    def search_name(self):
        """输入基金名称，点击搜素"""
        self.find_elements(self.search_input_loc)[0].send_keys('2')
        self.click(self.search_button_loc)
        text = self.find_elements(self.result_loc)[1].text
        if text == '自动化测试产品2':
            return True
        else:
            return False

    def search_code(self):
        """输入基金编码，点击搜素"""
        self.find_elements(self.search_input_loc)[1].send_keys('2')
        self.click(self.search_button_loc)
        text = self.find_elements(self.result_loc)[1].text
        if text == '自动化测试产品2':
            return True
        else:
            return False

    def search_admin(self):
        """输入基金管理人，点击搜素"""
        self.find_elements(self.search_input_loc)[2].send_keys('2')
        self.click(self.search_button_loc)
        text = self.find_elements(self.result_loc)[1].text
        if text == '自动化测试产品2':
            return True
        else:
            return False

    def search_manager(self):
        """输入基金经理，点击搜素"""
        self.find_elements(self.search_input_loc)[3].send_keys('2')
        self.click(self.search_button_loc)
        text = self.find_elements(self.result_loc)[1].text
        if text == '自动化测试产品2':
            return True
        else:
            return False

    def export_button_click(self):
        """不填勾选任何数据，点击导出数据按钮"""
        self.find_elements(self.export_shelves_button_loc)[2].click()
        time.sleep(1)
        text = self.get_text(('class name', 'el-message__content'))
        if text == '请选择您要下架的产品':
            return True
        else:
            return False



    def move(self):
        """移动滚动条"""
        js = "document.getElementsByClassName('is-scrolling-left')[0].scrollLeft=1000"
        self.js_execute(js)


    def operation_click(self):
        """点击操作按钮，自动化测试产品2"""
        time.sleep(2)
        self.move()
        self.find_elements(self.operation_loc)[1].click()



    def editor_button_click(self):
        """点击操作按钮列表中的编辑，自动化测试产品2"""
        self.operation_click()
        time.sleep(1)
        self.find_elements(self.select_list_lc)[15].click()
        time.sleep(2)
        text = self.find_elements(('class name', 'el-button'))[0].text
        if text == '收起':
            return True
        else:
            return False

    def history_button_click(self):
        """点击操作按钮列表中的历史净值，自动化测试产品2"""
        self.operation_click()
        time.sleep(1)
        self.find_elements(self.select_list_lc)[16].click()
        time.sleep(2)
        text = self.get_text(('class name', 'el-form-item__label'))
        if text == '选择日期':
            return True
        else:
            return False

    def shelves_button_click(self):
        """点击操作按钮列表中的产品下架，点击取消,自动化测试产品2"""
        self.operation_click()
        time.sleep(1)
        self.find_elements(self.select_list_lc)[17].click()
        self.find_elements(('class name', 'el-button--small'))[0].click()
        time.sleep(1)
        text = self.get_text(('class name', 'el-message__content'))
        if text == '已取消下架':
            return True
        else:
            return False

    def shelves_confirm_button_click(self):
        """点击操作按钮列表中的产品下架，点击确认按钮，自动化测试产品2"""
        self.operation_click()
        time.sleep(1)
        self.find_elements(self.select_list_lc)[17].click()
        self.find_elements(('class name', 'el-button--small'))[1].click()
        time.sleep(1)
        text = self.get_text(('class name', 'el-message__content'))
        if text == '下架成功!':
            return True
        else:
            return False



if __name__ == '__main__':
    driver = browser()
    p = PublishedProductList(driver)
    p.open_url(manager_url)
    p.yf_manager_login()
    time.sleep(2)
    p.open_url(published_product_url)
    p.history_button_click()
