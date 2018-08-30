"""
@author:fei
@date:2018-08-23
@brief:已发布产品历史净值页面的元素定位以及操作
"""

import time

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl
from common.exec_mysql import ExecMysql
from common.log import logger

mysql = ExecMysql()
sql = "select url from url_list where id=1"
url = mysql.select_mysql(sql)[0][0]

history_list_url = GetUrl().get_admin_url() + url

class HistoryList(ManagerLogin):
    """已发布产品历史净值页面的元素定位以及操作"""

    #时间输入框，开始时间：0，结束时间：1
    select_date_loc = ('class name', 'el-input__inner')
    #查询按钮
    search_loc = ('class name', 'btnCheck')


    def date_search(self):
        """输入开始和结束的时间，点击搜索按钮"""

        if self.element_click(self.find_elements(('class name', 'cell'))[0]):
            self.find_elements(self.select_date_loc)[0].click()
            time.sleep(1)
            self.click(('class name', 'today'))
            time.sleep(1)
            self.click(self.search_loc)
            time.sleep(1)
            text = self.get_text(('class name', 'el-table__empty-text'))
            print(text)
            return text
        else:
            return "页面不能点击"

if __name__ == '__main__':
    driver = browser()
    s = HistoryList(driver)
    s.open_url(manager_url)
    s.yf_manager_login()
    time.sleep(1)
    s.open_url(history_list_url)
    print(history_list_url)





