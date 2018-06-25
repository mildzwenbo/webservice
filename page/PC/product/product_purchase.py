from common.find_element import FindElement


import time


class ProductPurchase(FindElement):

    '''产品列表页面元素'''
    name_loc = ('class name', 'user-name')  # 登录名称定位
    viwe_loc = ('class name', 'el-button--medium')  # 产品列表查看定位

    '''基本元素页面元素'''
    info_loc = ('xpath', '//span[text()="产品详情"]')  # 产品详情
    purchase1_loc = ('xpath', '//span[text()="申购"]')  # 基本要素页面申购按钮

    '''风险揭示书页面'''
    book_loc = ('class name', 'no-redirect')  # 风险揭示书定位
    check_box_loc = ('class name', 'el-checkbox__inner')  # 勾选框定位
    confirm_loc = ('class name', 'is-plain')  # 确认按钮定位

    '''申购页面'''
    apply_loc = ('class name', 'no-redirect')  # 申购页面申购申请元素定位
    purchase_confirm_loc = ('class name', 'el-checkbox__inner')  # 申购页面勾选框
    purchase_amount_loc = ('class name', 'el-input__inner')  # 申购金额输入框
    purchase_button_loc = ('class name', 'is-plain')  # 申购页面提交按钮


    def viwe_button(self):
        '''点击产品列表页面-查看按钮'''
        viwe_button = self.find_elements(self.viwe_loc)[2]
        viwe_button.click()

    def detaile_test(self,asstassertEqual):
        '''获取基本详情页面-产品详情，并断言'''
        details_text = self.find_element(self.info_loc).text
        asstassertEqual(details_text, '产品详情')

    def purchase_button(self):
        '''点击基本详情页面-申购按钮'''
        self.click(self.purchase1_loc)

    def disclosure_book(self,asstassertEqual):
        '''获取风险揭示书页面-风险揭示数，并断言'''
        disclosure_book_text = self.find_element(self.book_loc).text
        asstassertEqual(disclosure_book_text, '风险揭示书')


    def check_box_button(self):
        '''定位勾选框--选中勾选框'''
        self.js_scroll_end(0, 1200)
        target = self.find_elements(self.check_box_loc)
        target[0].click()
        target[1].click()
        target[2].click()
        target[3].click()
        target[4].click()
        target[5].click()
        target[6].click()
        target[7].click()
        self.js_scroll_end(0, 2000)
        target[8].click()
        target[9].click()
        target[10].click()
        target[11].click()
        target[12].click()
        time.sleep(1)

    def disclosure_book_confirm(self):
        '''点击风险揭示数页面确认按钮'''
        disclosure_book = self.find_elements(self.confirm_loc)[1]
        disclosure_book.click()

    def apply_text(self,asstassertEqual):
        '''获取申购页面-申请元素，并断言'''
        apply_text = self.find_element(self.apply_loc).text
        asstassertEqual(apply_text, '申购')


    def purchase_confirm(self,amount):
        '''申购页面勾选框'''
        self.js_scroll_end(0, 1300)
        self.click(self.purchase_confirm_loc)
        time.sleep(1)

        '''申购页面输入金额'''
        self.send_keys(self.purchase_amount_loc, amount)
        time.sleep(1)

        '''点击提交按钮'''
        self.find_elements(self.purchase_button_loc)[1].click()
        time.sleep(1)


    '''提交页面'''
    successful_loc = ('xpath', '//span[text()="返回产品列表"]')  # 提交页面返回产品列表

    def successful(self,asstassertEqual):
        '''提交页面提交成功定位'''
        text = self.find_element(self.successful_loc).text
        asstassertEqual(text,'返回产品列表')

if __name__ == '__main__':
    driver = browser()
    po = ProductPurchase(driver)
    po.open_url('http://inv.pb-yun.com')
    po.pc_login('15822816936', 'abc123456', '1')
    time.sleep(2)
    po.viwe_button()