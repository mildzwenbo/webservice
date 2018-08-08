"""
@author:liuxin
@date:2018-8-6
@brief:数据维护-所有产品页面元素定位
"""

from page.SafeManager.data_maintenance.product import Product, browser, manager_url
import time


class Calendar(Product):
    operate_button = ('class name', 'el-button--medium')  # 页面所有按钮定位
    left_but = ('class name', 'prev-month')  # 日历中向左的按钮
    right_but = ('class name', 'next-month')  # 日历中向右的按钮
    years = ('class name', 'el-input__inner')  # 年份和月份文本框定位
    August = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[8]/span')  # 日历中八月份的选择
    August_8 = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[4]')  # 八日定位
    import_excl = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div[3]/div/div/button')  # 导入估值表按钮定位
    delete_excel = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div[1]/div[6]')  # 删除估值表按钮定位
    crumbs = ('class name', 'goHover')  # 可点击的面包屑导航链接定位
    button = ('class name', 'el-button--default')  # 弹框里的确定、取消按钮定位

    def click_log(self):
        """点击数据日历页面，操作日志按钮"""
        time.sleep(1)
        self.find_elements(self.operate_button)[0].click()

    def click_import_data(self):
        """点击数据日历页面，导入数据按钮"""
        time.sleep(1)
        self.find_elements(self.operate_button)[1].click()

    def click_return_data(self):
        """点击数据日历页面，返回列表按钮"""
        time.sleep(1)
        self.find_elements(self.operate_button)[2].click()

    def select_date(self):
        """选择日期：2018-8-8"""
        time.sleep(1)
        self.find_elements(self.years)[1].click()
        time.sleep(1)
        self.click(self.August)
        time.sleep(1)
        self.click(self.August_8)

    # def upload_file(self):
    #     """上传附件"""
    #     self.select_date()
    #     self.click(self.import_excl)
    #     time.sleep(1)
    #     SendKeys.SendKeys('D:\\baidu.py')  # 发送文件地址
    #     SendKeys.SendKeys("{ENTER}")  # 发送回车键

    def click_delete_excel(self):
        """点击删除估值表按钮"""
        self.select_date()
        time.sleep(1)
        self.click(self.delete_excel)

    def sure_button(self):
        """点击删除估值表按钮显示的弹框里，确定按钮"""
        self.find_elements(self.button)[1].click()

    def cancel_button(self):
        """点击删除估值表按钮显示的弹框里，取消按钮"""
        self.find_elements(self.button)[0].click()


if __name__ == '__main__':
    driver = browser()
    p = Calendar(driver)
    p.open_url(manager_url)
    p.lx_manager_login()
    p.click_bar()
    p.click_date()
    p.click_close()