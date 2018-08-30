"""
@author:fei
@date:2018-08-22
@brief:未发布产品页面对产品的编辑
"""


import time

from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl
from common.exec_mysql import ExecMysql

mysql = ExecMysql()
sql = 'select url from url_list where id=3'
url = mysql.select_mysql(sql)[0][0]

editor_product_url = GetUrl().get_admin_url() + url


class EditorProduct(ManagerLogin):
    #定位到投资信息元素
    investment_information_loc = ('css', '#app > div > div.app-wrapper > div.main-container > section > div > div.form-parent > div > ul > li:nth-child(3)')
    # 基本投资方向输入框：0
    input_name_loc = ('class name', 'el-textarea__inner')
    # 保存按钮：6
    save_loc = ('class name', 'el-button--medium')

    def editor_product(self):
        """在投资信息下主要投资方向编辑信息"""
        result = self.element_click(self.find_elements(self.input_name_loc)[0])
        if result:
            self.click(self.investment_information_loc)
            investment_directionself_element = self.find_elements(self.input_name_loc)[0]
            investment_directionself_element.clear()
            investment_directionself_element.send_keys('在投资信息下主要投资方向编辑信息')
            self.find_elements(self.save_loc)[6].click()
        else:
            pass




if __name__ == '__main__':
    driver = browser()
    p = EditorProduct(driver)
    p.open_url(manager_url)
    p.yf_manager_login()
    time.sleep(2)
    p.open_url(editor_product_url)
    p.editor_product()
    # print(editor_product_url)

