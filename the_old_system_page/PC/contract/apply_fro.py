"""
@author：fei
@date：2018-7-3
@brief：申赎记录下的申请列表
"""

from common.pc_login import PCLogin, pc_url, browser
from common.get_url import GetUrl
import time

apply_url = GetUrl().get_pc_url() + r'#/contractApply/index'


class ApplyFor(PCLogin):
    """申赎记录下申请列表中所有元素的操作"""
    # 产品名称和类型，第一个为产品名称，第二个为类型
    inputs_loc = ('class name', 'el-input__inner')
    # 类型的选择，第十一个为申购，第十二个为赎回
    select_loc = ('class name', 'el-select-dropdown__item')
    # 列表中第一个为开始时间。第二个为结束时间
    date_loc = ('class name', 'el-range-input')
    # 查询按钮,第一个为查询按钮
    search_loc = ('class name', 'el-button--primary')
    # 成交列表
    transaction_loc = ('id', 'tab-1')
    # 申请列表
    apply_fro_loc = ('id', 'tab-0')

    def search(self, product_name, select_type):
        """
        查询
        :param product_name: 产品名称
        :param select_type: 类型的选择， 1代表：申购，2代表赎回
        :return:
        """
        self.find_elements(self.inputs_loc)[0].send_keys(product_name)
        self.find_elements(self.inputs_loc)[1].click()
        time.sleep(1)
        if select_type == '1':
            self.find_elements(self.select_loc)[10].click()
        elif select_type == "2":
            self.find_elements(self.select_loc)[11].click()
        js1 = "document.getElementsByClassName('el-range-input')[0].value = '2018-06-27 00:00:00'"
        js2 = "document.getElementsByClassName('el-range-input')[1].value = '2018-06-30 00:00:00'"
        self.js_execute(js1)
        self.js_execute(js2)
        time.sleep(1)
        self.find_elements(self.search_loc)[0].click()
        element = ('xpath', '//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
        text = self.get_text(element)
        print(text)

    def transaction_click(self):
        """
        点击成交列表
        :return:进入成交列表
        """
        self.click(self.transaction_loc)

    def apply_fro_lick(self):
        """
        点击申请页面
        :return: 进入到申请列表
        """
        self.click(self.apply_fro_loc)


if __name__ == '__main__':
    browser = browser()
    a = ApplyFor(browser)
    a.open_url(pc_url)
    a.yf_pc_login()
    a.open_url(apply_url)
    time.sleep(1)
    a.search('R3', '1')

