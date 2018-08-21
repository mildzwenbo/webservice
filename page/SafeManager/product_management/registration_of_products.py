"""
@author:fei
@date:2018-08-20
@brief:登记产品页面的测试用例
"""


from common.manager_login import manager_url, ManagerLogin, browser
from common.get_url import GetUrl


import time

registration_of_product_url = GetUrl().get_admin_url() + r'#/product/ProductAdd'


class RegistrationOfProduct(ManagerLogin):

    #所有输入框的class name
    input_name_loc = ('class name', 'el-input__inner')

    #保存:6 保存并且发布按钮:7
    save_loc = ('class name', 'el-button--medium')

    #所有的下拉框选项
    select_elements_loc = ('class name', 'el-select-dropdown__item')

    #单选选选项
    mulitple_loc = ('class name', 'el-checkbox__inner')


    def no_input(self):
        """
        不填写任何信息点击保存按钮
        :return:
        """
        time.sleep(2)
        self.find_elements(self.save_loc)[6].click()
        time.sleep(1)
        text = self.get_text(('class name', 'el-message--error'))
        if text == '有必填项未填写或输入有误':
            return True
        else:
            return False

    def no_input_release(self):
        """
        勾选所有其他选项，查看必填项共37个必填项，其余没有些
        :return:
        """
        time.sleep(2)
        self.find_elements(('class name', 'el-radio__inner'))[7].click()
        self.js_scroll_end(0, 800)
        self.find_elements(('class name', 'el-checkbox__inner'))[6].click()
        self.find_elements(('class name', 'el-radio__inner'))[32].click()
        self.find_elements(('class name', 'el-radio__inner'))[35].click()
        self.find_elements(('class name', 'el-radio__inner'))[36].click()
        self.js_scroll_end(0, 100)
        self.find_elements(('class name', 'el-radio__inner'))[38].click()
        self.find_elements(('class name', 'el-radio__inner'))[42].click()
        self.find_elements(('class name', 'el-radio__inner'))[44].click()
        self.js_scroll_end(0, 2000)
        self.find_elements(('class name', 'el-radio__inner'))[48].click()
        self.find_elements(('class name', 'el-checkbox__inner'))[14].click()
        self.find_elements(('class name', 'el-radio__inner'))[51].click()
        self.find_elements(('class name', 'el-checkbox__inner'))[19].click()
        self.find_elements(('class name', 'el-radio__inner'))[55].click()
        time.sleep(2)
        self.find_elements(self.save_loc)[7].click()
        time.sleep(1)
        text = self.get_text(('class name', 'el-message--error'))

        number = len(self.find_elements(('class name', 'el-form-item__error')))
        if text == '有必填项未填写或输入有误' and number == 37:
            return True
        else:
            return False


    def input_something(self, name,name2, code):
        """
        输入信息
        :return:
        """
        #产品名称
        self.find_elements(self.input_name_loc)[0].send_keys(name)
        # 产品简称
        self.find_elements(self.input_name_loc)[1].send_keys(name2)
        #产品编码
        self.find_elements(self.input_name_loc)[2].send_keys(code)
        #基金类型
        self.find_elements(self.input_name_loc)[3].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[29].click()
        #产品类型
        self.find_elements(self.input_name_loc)[4].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[43].click()
        #组织形式
        self.find_elements(self.input_name_loc)[6].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[43].click()
        #成立日期
        time.sleep(1)
        self.find_elements(self.input_name_loc)[8].click()
        time.sleep(1)
        self.click(('class name', 'today'))
        # 到期日期
        self.find_elements(self.mulitple_loc)[0].click()
        # 管理类型
        self.find_elements(self.input_name_loc)[11].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[44].click()
        #基金状态
        self.find_elements(self.input_name_loc)[12].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[44].click()
        #份额类型
        self.find_elements(self.input_name_loc)[13].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[42].click()
        #基金成立规模
        self.find_elements(self.input_name_loc)[16].send_keys('22')
        self.js_scroll_end(0, 500)
        # 基金管理人
        self.find_elements(self.input_name_loc)[19].send_keys('自动化测试11')
        # 基金经理
        self.find_elements(self.input_name_loc)[20].send_keys('自动化测试11')
        # 基金运作方式
        self.find_elements(self.input_name_loc)[21].click()
        time.sleep(1)
        self.find_elements(self.select_elements_loc)[44].click()
        #基金风险等级
        self.find_elements(self.input_name_loc)[22].click()
        self.find_elements(self.select_elements_loc)[42].click()
        # 主要投资方向
        self.find_elements(('class name', 'el-textarea__inner'))[0].send_keys('自动化测试11')
        self.find_elements(self.save_loc)[6].click()






if __name__ == '__main__':
    driver = browser()
    r = RegistrationOfProduct(driver)
    r.open_url(manager_url)
    r.yf_manager_login()
    time.sleep(1)
    r.open_url(registration_of_product_url)
    time.sleep(2)
    r.input_something()