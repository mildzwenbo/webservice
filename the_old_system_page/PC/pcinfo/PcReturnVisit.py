from common.find_element import FindElement

import time

class ReturnVisitt(FindElement):
    '''回访单'''

    fundBuyForm_loc = ('xpath','//*[@id="fundBuyForm"]/div[1]/h3')#基金购买回访单
    number_loc = ('class name','el-radio')#选择框
    return_visit_consider_loc = ('xpath','//span[text()="考虑一下"]')#考虑一下
    return_visit_submit_loc = ('xpath','//span[text()="提交"]')#提交

    def funbuyform(self):
        text = self.find_element(self.fundBuyForm_loc).text[-7:]
        return text

    def even_number(self):
        '''点击是单选框'''
        a = [i for i in range(17) if i % 2 == 0]
        for i in a:
            element = self.find_elements(self.number_loc)[i]
            element.click()

    def odd_number(self):
        '''点击否单选框'''
        a = [i for i in range(18) if i % 2 != 0]
        for i in a:
            element = self.find_elements(self.number_loc)[i]
            element.click()

    def return_visit_consider(self):
        '''点击考虑一下按钮'''
        self.click(self.return_visit_consider_loc)

    def return_visit_submit(self):
        '''点击提交按钮'''
        self.click(self.return_visit_submit_loc)

