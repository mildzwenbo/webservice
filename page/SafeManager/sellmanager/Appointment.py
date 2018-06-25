from common.find_element import FindElement
from common.PC_login import PCLogin,browser
from page.SafeManager.ManageLogin import ManageLoginPage

import time

class Appointment(FindElement):

    '''销售管理-预约申请列表页面'''

    menu_sales_loc = ('xpath', '//span[text()="销售管理"]')  # 销售管理菜单
    '''列表'''
    status1_loc = ('xpath', '//*[@class="layui-table"]/tbody/tr[1]/td[7]/div')  # 状态
    operation_button_loc = ('class name', 'layui-btn')  # 操作按钮
    drop_down_loc = ('xpath', '//*[@id="selectIDPop"]/div/div/i')  # 审核页面下拉选项
    select_loc = ('name', 'modules')
    rejected_loc = ('xpath', '//*[@id="selectIDPop"]/div/dl/dd[2]')  # 驳回按钮
    determine_loc = ('class name', 'layui-layer-btn0')  # 确定按钮
    a = ('class name', 'main-left')

    def sales(self):
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)

    def click_menu(self):
        '''菜单操作'''
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)
        time.sleep(1)
        # '''菜单滚动条'''
        # js = "document.getElementsByClassName('main-left')[0].scrollTop=10000"
        # self.driver.execute_script(js)
        # time.sleep(1)
        '''点击预约申请菜单'''
        self.driver.find_element_by_link_text("预约申请").click()

    def manage_status(self):
        '''状态'''
        text = self.find_element(self.status1_loc).text
        return text

    '''滚动条'''

    def scroll(self):
        self.js_scroll_end(0, 1000)

    def scroll_lift(self):
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def window_scroll(self):
        '''窗口操作'''
        '''滚动条向下到底'''
        self.js_scroll_end(0, 1000)
        time.sleep(1)
        '''内置滚动条向右'''
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def operation_button(self):
        '''点击操作按钮'''
        self.find_elements(self.operation_button_loc)[1].click()

    def audit_button(self):
        '''点击审核按钮'''
        js = "document.getElementById('purchase-edit').click()"
        self.js_execute(js)

    def drop_down(self):
        '''点击审核下拉'''
        self.click(self.drop_down_loc)

    def rejected(self):
        '''点击驳回按钮'''
        self.click(self.rejected_loc)

    def determine(self):
        '''点击确定按钮'''
        self.click(self.determine_loc)


if __name__ == '__main__':
    driver = browser()
    po = PCLogin(driver)
    po.open_url('http://boss.pb-yun.com/')
    po2 = ManageLoginPage(driver)
    po2.ManageLogin('13511055879','123456','')
    time.sleep(4)
    po1 = Appointment(driver)
    po1.click_menu()
    time.sleep(1)
    po1.window_scroll()
    time.sleep(1)
    po1.operation_button()
    time.sleep(1)
    po1.audit_button()
    time.sleep(1)
    po1.drop_down()
    time.sleep(1)
    po1.rejected()





