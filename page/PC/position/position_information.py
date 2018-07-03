"""
@author: fei
@date:2018-7-2
@brief:持仓信息页面
"""
import time

from common.pc_login import PCLogin, pc_url, browser
from common.get_url import GetUrl

position_url = GetUrl().get_pc_url() + r'#/positioninfo/index'


class ThePositionInformation(PCLogin):
    """持仓信息页面"""
    #产品名称输入框, 列表中第一个
    names_loc = ('class name', 'el-input__inner')
    #查询按钮
    search_loc = ('class name', 'el-button--medium')
    #第一个记录中的操作按钮, 列表中的第二个
    operation_loc = ('class name', 'el-button--primary')
    #操作列表中的数据，第一个为查询，第二个为申购，第三个为赎回
    operation_list_loc = ('class name', 'el-dropdown-menu__item')

    def search(self, text):
        """
        查询操作
        :param text:
        :return:
        """
        name = self.find_elements(self.names_loc)[0]
        name.send_keys(text)
        self.click(self.search_loc)

    def look_over(self):
        """列表中第一条数据，点击操作按钮，点击查看"""
        operation_element = self.find_elements(self.operation_loc)[1]
        operation_element.click()
        time.sleep(2)
        self.find_elements(self.operation_list_loc)[0].click()

    def subscribe(self):
        """列表中第一条数据，点击操作按钮，点击申购"""
        operation_element = self.find_elements(self.operation_loc)[1]
        operation_element.click()
        time.sleep(2)
        self.find_elements(self.operation_list_loc)[1].click()

    def redemption(self):
        """列表中第一条数据，点击操作按钮，点击查看"""
        operation_element = self.find_elements(self.operation_loc)[1]
        operation_element.click()
        time.sleep(1)
        self.find_elements(self.operation_list_loc)[2].click()
        time.sleep(1)


if __name__ == '__main__':
    browser = browser()
    position = ThePositionInformation(browser)
    position.open_url(pc_url)
    position.yf_pc_login()
    position.open_url(position_url)
    time.sleep(2)
    position.look_over()
    position.delete_all_cookies()
    position.refresh()


