from common.find_element import FindElement
from common.pc_login import PCLogin,browser
from the_old_system_page.SafeManager.ManageLogin import ManageLoginPage
from the_old_system_page.SafeManager.sellmanager.Appointment import Appointment


import time,datetime

class ContractManager(FindElement):
    '''合同管理页面'''

    '''合同管理'''
    contract_operation_loc = ('xpath', '//*[@class="layui-table"]/tbody/tr[1]/td[9]/div/a')  # 操作按钮
    conract_states_loc = ('xpath', '//*[@class="layui-table"]/tbody/tr[1]/td[6]/div')  # 合同状态
    return_states_loc = ('xpath', '//*[@class="layui-table"]/tbody/tr[1]/td[7]/div')  # 回访状态
    contract_no_loc = ('id', 'contractNo')  # 合同编码
    time_input_loc = ('id', 'netValueDate')  # 时间输入框
    agent_loc = ('id', 'agent')  # 经办人输入框
    serviceCharge_loc = ('id', 'serviceCharge')  # 手续费
    calmnessPeriod_loc = ('id', 'calmnessPeriod')  # 冷静期
    contract_save_loc = ('id', 'contract-save')  # 保存按钮

    def contract_menu(self):
        '''点击合同管理菜单'''
        self.driver.find_element_by_link_text('合同管理').click()

    def conract_operation(self):
        '''点击操作按钮'''
        self.click(self.contract_operation_loc)

    def window_scroll(self):
        '''窗口操作'''
        '''滚动条向下到底'''
        self.js_scroll_end(0, 1000)
        time.sleep(1)
        '''内置滚动条向右'''
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def conract_status(self):
        '''数据状态'''
        text = self.find_element(self.conract_states_loc).text
        return text

    def return_status(self):
        '''回访状态'''
        text = self.find_element(self.return_states_loc).text
        return text

    def conract_edit(self):
        '''点击编辑按钮'''
        js = "document.getElementById('contract-edit').click()"
        self.js_execute(js)

    def scroll_on(self):
        '''滚动最上面'''
        self.js_scroll_end(0, 0)

    def conract_no(self):
        '''合同编码输入'''
        t = time.time()
        now_time = datetime.datetime.now()
        self.send_keys(self.contract_no_loc, 'HT%s' % int(t))

    def time_input(self,time1):
        '''时间输入框'''
        js = "document.getElementById('netValueDate').removeAttribute('readonly')"
        self.driver.execute_script(js)
        self.send_keys(self.time_input_loc,time1)

    def serviceCharge(self,cost):
        '''手续费'''
        self.send_keys(self.serviceCharge_loc, cost)

    def agent(self,name):
        '''经办人输入框'''
        self.send_keys(self.agent_loc, name)

    def calmnessPeriod(self,time2):
        '''冷静期输入框'''
        self.send_keys(self.calmnessPeriod_loc, time2)

    def contract_save(self):
        '''点击保存按钮'''
        self.click(self.contract_save_loc)


    '''确认已付款'''

    contract_payment_loc = ('id','contract-payment')
    paymentTime_loc = ('id', 'paymentTime')  # 付款时间
    payment_current_loc = ('xpath', '//span[text()="确定"]')
    layui_layer_btn0_loc = ('class name', 'layui-layer-btn0')  # 确认按钮

    def contract_payment_button(self):
        self.click(self.contract_payment_loc)

    def contract_payment(self):
        '''点击确认已付款按钮'''
        js = "document.getElementById('contract-payment').click()"
        self.js_execute(js)

    def paymentTime(self):
        '''点击输入付款时间'''
        self.click(self.paymentTime_loc)

    def payment_current(self):
        '''点击现在按钮'''
        self.click(self.payment_current_loc)

    def layui_layer_btn0(self):
        '''点击确认按钮'''
        self.click(self.layui_layer_btn0_loc)

    '''冷静期页面'''
    calm_date_loc = ('xpath','//*[@id="layui-layer100012"]/div[3]/a[2]')

    def clam_date(self):
        self.click(self.calm_date_loc)


    '''发送回访单'''
    returm_determine_loc = ('class name', 'layui-layer-btn0')  # 回访单页面确认按钮

    def contract_returm(self):
        '''点击发送回访单按钮'''
        js = "document.getElementById('send-tick').click()"
        self.js_execute(js)

    def returm_determine(self):
        '''点击弹出回访单页面确认按钮'''
        self.click(self.returm_determine_loc)


if __name__ == '__main__':
    driver = browser()
    po = PCLogin(driver)
    po.open_url('http://boss.pb-test.com/')
    po2 = ManageLoginPage(driver)
    po2.ManageLogin('17600000000', '123456', '')
    po1 = ContractManager(driver)
    po3 =Appointment(driver)
    time.sleep(4)
    po3.sales()
    po1.contract_menu()
    time.sleep(1)
    po1.window_scroll()
    time.sleep(1)
    status1 = po1.conract_status()
    status2 = po1.return_status()
    time.sleep(1)
    po1.conract_operation()
    po1.conract_edit()  # 点击列表页面编辑按钮
    time.sleep(1)
    po1.scroll_on()  # 页面滚动至最上面
    time.sleep(1)
    po1.conract_no()  # 输入合同编码
    time.sleep(1)
    po1.time_input('2018-01-01')  # 时间输入
    time.sleep(1)
    po1.serviceCharge(2000)  # 输入金额
    time.sleep(1)
    po1.agent('刘鑫')  # 输入经办人
    time.sleep(1)
    po1.calmnessPeriod(0)
    time.sleep(1)
    po1.contract_save()
    time.sleep(1)
    po1.window_scroll()
    po1.conract_operation()
    time.sleep(1)
    po1.contract_payment()  # 点击确认付款按钮
    time.sleep(1)
    po1.paymentTime()  # 输入付款时间
    time.sleep(1)
    po1.payment_current()  # 点击现在按钮
    time.sleep(1)
    po1.layui_layer_btn0()  # 点击确认按钮
    time.sleep(4)
