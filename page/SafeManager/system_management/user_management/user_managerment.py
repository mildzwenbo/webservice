"""
@author:fei
@date:2018-09-03
@brief:对用户页面所有元素的操作以及定位
"""

import time

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl

user_management_url = GetUrl().get_admin_url() + r'#/systemManage/system/system-staff-module.html'

class UserManagement(ManagerLogin):
    """对用户页面所有元素的操作以及定位"""

    # 部分搜索输入框：0
    search_input_loc = ('class name', 'el-input__inner')

    # 搜索按钮
    search_button_loc = ('class name', 'btnCheck')

    #新增用户:0、模板下载:1、导入按钮:2
    elements_loc = ('class name', 'el-button--warning')

    # 列表中的操作按钮
    list_loc = ('class name', 'el-tooltip')


    def search_user(self, username):
        """
        在搜索中输入mame,点击搜索
        :param name:要输入的名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.search_input_loc)[0].send_keys(username)
            self.click(self.search_button_loc)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                text = self.find_elements(self.list_loc)[1].text
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'

    def add_button_click(self):
        """
        点击新增用户按钮
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.find_elements(self.elements_loc)[0].click()
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                text = self.get_text(('class name', 'el-dialog__title'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'

    def no_input_name_add_user(self):
        """
        不输入任何信息，点击保存
        :return:错误提示字段
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.add_button_click()
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                # self.find_elements(self.search_input_loc)[3].send_keys(name)
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                errors_num = len(self.find_elements(('class name', 'el-form-item__error')))
                print('错误提示的个数为：%d' % errors_num)
                text = self.find_elements(('class name', 'el-form-item__error'))[0].text
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'


    def add_user(self, id,name, phone, email):
        """
        新增职务
        :param name:新增用户的名称
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.add_button_click()
            if self.element_click(self.find_elements(self.search_input_loc)[3]):
                #用户ID
                self.find_elements(self.search_input_loc)[3].send_keys(id)
                #姓名
                self.find_elements(self.search_input_loc)[4].send_keys(name)
                # 手机号
                self.find_elements(self.search_input_loc)[5].send_keys(phone)
                # 初始密码
                self.find_elements(self.search_input_loc)[6].send_keys('123456')
                js = "document.getElementsByClassName('dialogDiv')[0].scrollTop=300"
                self.js_execute(js)
                # 确认密码
                self.find_elements(self.search_input_loc)[7].send_keys('123456')
                # 点击部门名称
                self.find_elements(('class name', 'el-cascader__label'))[0].click()
                time.sleep(1)
                self.find_elements(('class name', 'el-cascader-menu__item'))[0].click()
                self.find_elements(self.search_input_loc)[7].click()
                time.sleep(1)
                #职务名称
                self.find_elements(('class name', 'el-cascader__label'))[1].click()
                time.sleep(2)
                self.find_elements(('class name', 'el-cascader-menu__item'))[4].click()
                self.find_elements(self.search_input_loc)[7].click()
                time.sleep(1)
                # 角色
                self.find_elements(self.search_input_loc)[10].click()
                time.sleep(1)
                self.find_elements(('class name', 'el-select-dropdown__item'))[4].click()
                self.find_elements(self.search_input_loc)[7].click()
                # 电子邮箱
                self.find_elements(self.search_input_loc)[11].send_keys(email)
                self.find_elements(self.search_input_loc)[7].click()
                time.sleep(1)
                self.click(('class name', 'el-button--primary'))
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'


    def click_product(self, username):
        """点击操作列表中的产品"""
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '产品'))
                if self.element_click(self.find_elements(('class name', 'el-input__inner'))[3]):
                    text = self.find_elements(('class name', 'el-dialog__title'))[3].text
                else:
                    text = '不能点击'
                return text
        else:
            return '不能点击'

    def allocation_user(self, username, name):
        """
        在产品分配中分配产品
        :param username:选择的用户
        :param name:要分配的产品
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '产品'))
                if self.element_click(self.find_elements(('class name', 'el-input__inner'))[3]):
                    #搜索产品名称
                    time.sleep(1)
                    self.find_element(('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div[7]/div/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div/div/input')).send_keys(name)
                    self.click(('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div[7]/div/div/div[2]/div/div[2]/div/div[1]/form/button/span'))
                    if self.element_click(self.find_elements(('class name', 'el-dialog__title'))[3]):
                        # 选择产品点击分配
                        self.find_elements(('class name', 'el-checkbox__inner'))[1].click()
                        time.sleep(2)
                        self.find_elements(('class name', 'el-button--medium'))[8].click()

                        if self.element_click(self.find_elements(('class name', 'el-dialog__title'))[3]):
                            # 查看显示的结果
                            text = self.get_text(('class name', 'el-table__empty-text'))
                        else:
                            text = '不能点击'
                        return text
        else:
            return '不能点击'


    def remove_product(self, username, name):
        """
        移除产品
        :param username:
        :param name:
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '产品'))
                if self.element_click(self.find_elements(('class name', 'el-input__inner'))[3]):
                    self.click(('class name', 'dialogTableTwo'))
                    if self.element_click(self.find_elements(('class name', 'el-input__inner'))[3]):
                        # 搜索产品名称
                        time.sleep(1)
                        self.find_element(('xpath',
                                           '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div[7]/div/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div/div/input')).send_keys(
                            name)
                        self.click(('xpath',
                                    '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div[7]/div/div/div[2]/div/div[2]/div/div[1]/form/button/span'))
                        if self.element_click(self.find_elements(('class name', 'el-dialog__title'))[3]):
                            # 选择产品点击分配
                            self.find_elements(('class name', 'el-checkbox__inner'))[1].click()
                            time.sleep(2)
                            self.find_elements(('class name', 'el-button--medium'))[8].click()

                            if self.element_click(self.find_elements(('class name', 'el-dialog__title'))[3]):
                                # 查看显示的结果
                                text = self.get_text(('class name', 'el-table__empty-text'))
                            else:
                                text = '不能点击'
                            return text
        else:
            return '不能点击'

    def reset_password_click(self, username):
        """
        点击重置密码
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '重设密码'))
                time.sleep(1)
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    text = self.find_elements(('class name', 'el-dialog__title'))[1].text
                else:
                    text = '不能点击'

                return text
        else:
            return '不能点击'

    def reset_password(self, username):
        """
        点击重置密码
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '重设密码'))
                time.sleep(1)
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    self.find_elements(self.search_input_loc)[3].send_keys('111111')
                    self.find_elements(self.search_input_loc)[4].send_keys('111111')
                    self.click(('class name', 'el-button--primary'))
                    time.sleep(1)
                    text = self.get_text(('class name', 'el-message__content'))
                else:
                    text = '不能点击'
                return text
        else:
            return '不能点击'


    def permission_to_view_click(self, username):
        """
        点击查看权限按钮
        :param name:
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '权限查看'))
                if self.element_click(self.find_elements(('class name', 'el-tree-node__label'))[0]):
                    text = self.find_elements(('class name', 'el-dialog__title'))[2].text
                else:
                    text = '不能点击'
                return text
        else:
            return '不能点击'

    def editor_user_click(self, username):
        """
        点击编辑按钮
        :param username:
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '编辑'))
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    text = self.find_elements(('class name', 'el-dialog__title'))[0].text
                else:
                    text = '不能点击'
                return text
        else:
            return '不能点击'

    def editor_user(self, username):
        """
        编辑用户
        :param username:
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '编辑'))
                if self.element_click(self.find_elements(self.search_input_loc)[3]):
                    self.find_elements(self.search_input_loc)[3].clear()
                    self.find_elements(self.search_input_loc)[3].send_keys('aaa')
                    self.click(('class name', 'el-button--primary'))
                    time.sleep(1)
                    text = self.get_text(('class name', 'el-message__content'))
                else:
                    text = '不能点击'
                return text
        else:
            return '不能点击'


    def delete_user(self, username):
        """
        删除用户
        :param username:
        :return:
        """
        if self.element_click(self.find_elements(self.search_input_loc)[0]):
            self.search_user(username)
            if self.element_click(self.find_elements(self.search_input_loc)[0]):
                self.click(('link text', '删除'))
                self.find_elements(('class name', 'el-button--primary'))[1].click()
                time.sleep(1)
                text = self.get_text(('class name', 'el-message__content'))
            else:
                text = '不能点击'
            return text
        else:
            return '不能点击'







if __name__ == '__main__':
    driver = browser()
    user = UserManagement(driver)
    user.open_url(manager_url)
    user.yf_manager_login()
    time.sleep(3)
    user.open_url(user_management_url)
    # user.no_input_name_add_user()
    user.add_user('username153', '17888888888', 'dfdlsdjf@qq.com')