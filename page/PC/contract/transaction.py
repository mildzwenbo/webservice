"""
@author:fei
@date:2018-7-3
@brief:申赎记录中的成交列表
"""

import time

from common.pc_login import PCLogin, browser, pc_url
from common.get_url import GetUrl

transaction_url = GetUrl().get_pc_url() + r"#/contractApply/index"


class Transaction(PCLogin):
    """申赎记录，成交列表页面所有元素的操作"""
    # 成交记录
    transaction_loc = ('id', 'tab-1')
    # 产品名称,类型，列表中的第六个，第七个
    product_name_loc = ('class name', 'el-input__inner')
    # 类型的选择,第十一个为申购，第十二个为赎回
    select_loc = ('class name', 'el-select-dropdown__item')
    # 列表中第三个为开始时间。第四个为结束时间
    date_loc = ('class name', 'el-range-input')
    # 查询按钮,第二个为查询按钮
    search_loc = ('class name', 'el-button--primary')

    def search(self, product_name, select_type):
        """
        查询
        :param product_name: 产品名称
        :param select_type: 类型的选择， 1代表：申购，2代表赎回
        :return:
        """
        self.find_elements(self.product_name_loc)[5].send_keys(product_name)
        self.find_elements(self.product_name_loc)[6].click()
        time.sleep(1)
        if select_type == '1':
            self.find_elements(self.select_loc)[10].click()
        elif select_type == '2':
            self.find_elements(self.select_loc)[11].click()
        js1 = "document.getElementsByClassName('el-range-input')[2].value = '2018-06-20'"
        js2 = "document.getElementsByClassName('el-range-input')[3].value = '2018-06-30'"
        self.js_execute(js1)
        self.js_execute(js2)
        self.find_elements(self.search_loc)[1].click()
        text = self.get_text(('xpath', '//*[@id="pane-1"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div'))
        print(text)

    def transaction_click(self):
        """
        点击成交列表
        :return:进入成交列表
        """
        self.click(self.transaction_loc)


if __name__ == '__main__':
    browser = browser()
    t = Transaction(browser)
    t.open_url(pc_url)
    t.yf_pc_login()
    t.open_url(transaction_url)
    t.transaction_click()
    time.sleep(2)
    t.search('R3', '1')
