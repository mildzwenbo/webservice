"""
@author:fei
@date:2018-08-31
@brief:系统管理中的部门管理所有元素的操作
"""

import time

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl


depart_management_url = GetUrl().get_admin_url() + '#/systemManage/system/system-department-module.html'


class DepartmentManagement(ManagerLogin):
    """对部门管理页面所有元素的操作"""

    #部分搜索输入框：0
    search_input_loc = ('class name', 'el-input__inner')

    #搜索按钮
    search_button_loc = ('class name', 'btnCheck')

    #新增部门按钮
    add_department_loc = ('class name', 'floatRight')

    #列表中的操作按钮
    list_loc = ('class name', 'el-tooltip')


    def search_department(self, name):
        """
        在搜索中输入mame,点击搜索
        :param name:要输入的名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                text = self.find_elements(self.list_loc)[0].text
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'


    def add_button_click(self):
        """
        点击新增部门按钮
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.click(self.add_department_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                text = self.get_text(('class name', 'el-dialog__title'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'


    def no_input_name_add_department(self):
        """
        不输入部门名称，点击保存
        :param name: 新增部门的名称
        :return:错误提示字段
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.click(self.add_department_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                # self.find_elements(self.search_input_loc)[3].send_keys(name)
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-form-item__error'))
            else:
                text = '不能点击'
            print(text)
            return text
        else:
            return '不能点击'

    def add_department(self, name):
        """
        新增职务
        :param name:新增职务的名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.click(self.add_department_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                self.find_elements(self.search_input_loc)[3].send_keys(name)
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'


    def editor_department_click(self, name):
        """
        点击编辑按钮
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '编辑'))
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    text = self.get_text(('class name', 'el-dialog__title'))
                else:
                    text = '不能点击'
                print(text)
                return text
            else:
                return '不能点击'
        else:
            return '不能点击'

    def editor_department(self, name):
        """
        编辑部门
        :param name: 产品名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '编辑'))
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    self.click(('class name', 'el-button--primary'))
                    time.sleep(1)
                    text = self.get_text(('class name', 'el-message__content'))
                else:
                    text = '不能点击'
                return text
            else:
                return '不能点击'
        else:
            return '不能点击'

    def delete_department(self, name):
        """
        删除部门
        :param name: 要删除部门的名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(name)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '删除'))
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'





if __name__ == '__main__':
    driver = browser()
    d = DepartmentManagement(driver)
    d.open_url(manager_url)
    d.yf_manager_login()
    time.sleep(2)
    d.open_url(depart_management_url)
    d.delete_department('eeeee')





