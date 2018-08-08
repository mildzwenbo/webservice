
"""
@author:liuxin
@ad_date:2018-8-8
@brief:数据维护-操作日志页面元素定位
"""

from page.SafeManager.data_maintenance.product import Product, browser, manager_url
import time
import os


class OperationLog(Product):
    all_input = ('class name', 'el-input__inner')  # 操作日志页面，所有文本框元素定位
    query_button = ('class name', 'btnCheck')  # 查询按钮定位
    result = ('class name', 'el-select-dropdown__item')  # 上传结果下拉框定位
    download = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/a')  # 附件名称链接定位
    loser = ('xpath', '//*[@id="app"]/div/div[2]/div[2]/section/div/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[7]/div/a')  # 结果为失败的链接定位


    def click_log_bar(self):
        """点击主导航栏：数据维护-操作日志"""
        self.find_elements(self.data)[2].click()
        time.sleep(1)
        self.find_elements(self.all_product)[5].click()

    def upload_heir(self, value):
        """查询：上传人输入内容"""
        self.find_elements(self.all_input)[0].send_keys(value)

    def upload_time(self, value):
        """查询：选择上传时间"""
        query_time = self.find_elements(self.all_input)[1]
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
        self.js_execute(js)
        query_time.send_keys(value)

    def succeed_result(self):
        """查询：上传结果-成功结果"""
        time.sleep(1)
        self.find_elements(self.all_input)[2].click()
        time.sleep(1)
        self.find_elements(self.result)[4].click()

    def loser_result(self):
        """查询：上传结果-失败结果"""
        time.sleep(1)
        self.find_elements(self.all_input)[2].click()
        time.sleep(1)
        self.find_elements(self.result)[5].click()

    def all_result(self):
        """查询：上传结果-失败结果"""
        time.sleep(1)
        self.find_elements(self.all_input)[2].click()
        time.sleep(1)
        self.find_elements(self.result)[3].click()

    def click_file(self):
        """点击附件链接"""
        time.sleep(1)
        self.click(self.download)

    def click_loser(self):
        """点击结果下失败的链接"""
        time.sleep(1)
        self.click(self.loser)

    def click_query_button(self):
        """点击结果下失败的链接"""
        self.click(self.query_button)

    def delete_file(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                OperationLog(c_path)
            else:
                os.remove(c_path)



if __name__ == '__main__':
    driver = browser()
    p = OperationLog(driver)
    p.open_url(manager_url)
    p.lx_manager_login()
    p.click_log_bar()
    p.click_loser()

