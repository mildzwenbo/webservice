from common.find_element import FindElement

import time

class PurchaseRrecord(FindElement):
    '''申赎记录列表页面'''
    menu_loc = ('class name', 'el-menu-item')  # 申赎记录菜单
    breadcrumb_loc = ('class name', 'no-redirect')  # 申赎记录
    cell_loc = ('class name', 'cell')  # 列表页面字段下数据

    def menu(self):
        '''点击申赎记录菜单'''
        element = self.find_elements(self.menu_loc)[3]
        element.click()

    def breadcrumb(self):
        '''获取面包屑'''
        text = self.find_element(self.breadcrumb_loc).text
        return text

    def apply_time(self):
        '''获取列表时间信息'''
        element = self.find_elements(self.cell_loc)[7]
        text = element.text
        return text[:10]

    def current_time(self):
        '''获取当前时间'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[:10]
        return time1

    def status(self):
        '''获取列表状态信息'''
        text = self.find_elements(self.cell_loc)[12].text
        return text