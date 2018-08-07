"""
@author:fei
@date:2018-7-2
@brief:信息纰漏下报告页面
"""
import time

from common.pc_login import PCLogin, browser, pc_url
from common.get_url import GetUrl

report_url = GetUrl().pc_url + r'#/informationDisclosure/index'


class Report(PCLogin):
    """信息纰漏下的报告页面进行的操作"""
    #产品名称、报告类型
    inputs_loc = ('class name', 'el-input__inner')
    #开始时间和结束时间
    dates_loc = ('class name', 'el-range-input')
    #查询按钮
    report_search_loc = ('class name', 'el-button--primary')
    # 报告按钮
    report_loc = ('id', 'tab-1')

    def search(self, text, type_value):
        """
        对查询进行操作
        :return:
        """
        name_input_element = self.find_elements(self.inputs_loc)[4]
        name_input_element.send_keys(text)

        remove_readonly = 'document.getElementsByClassName("el-input__inner")[5].removeAttribute("readonly")'
        self.js_execute(remove_readonly)
        time.sleep(1)
        if type_value == '1':
            type_report = 'document.getElementsByClassName("el-input__inner")[5].value="日报"'
        self.js_execute(js=type_report)
        time.sleep(1)
        js1 = "document.getElementsByClassName('el-range-input')[2].value = '2018-06-10'"
        js2 = "document.getElementsByClassName('el-range-input')[3].value = '2018-06-27'"
        self.js_execute(js1)
        self.js_execute(js2)
        search_element = self.find_elements(self.report_search_loc)[1]
        search_element.click()

    def report_click(self):
        """
        净值页面，点击进入报告页面
        :return:
        """
        self.click(self.report_loc)


if __name__ == '__main__':
    browser = browser()
    r = Report(browser)
    r.open_url(pc_url)
    r.yf_pc_login()
    r.open_url(report_url)
    time.sleep(1)
    r.report_click()
    time.sleep(1)
    r.search(text="Rx", type_value="1")

