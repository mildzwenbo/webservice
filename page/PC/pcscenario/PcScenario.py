from common.PC_login import PCLogin,browser
from common.get_url import GetUrl

import time
import datetime
import unittest


pc_url = GetUrl().get_pc_url()


class PcScenario(PCLogin):

    '''流程页面'''

    '''产品列表页面元素'''
    name_loc = ('class name','user-name')#登录名称定位
    viwe_loc = ('class name','el-button--medium')#产品列表查看定位

    def login_name(self):
        '''获取登录名称'''
        text = self.find_element(self.name_loc).text
        return text

    def viwe_button(self):
        '''点击查看按钮方法'''
        element = self.find_elements(self.viwe_loc)[2]
        element.click()

    '''基本元素页面元素'''
    info_loc = ('class name','el-breadcrumb__inner')#产品详情
    purchase1_loc = ('xpath','//span[text()="申购"]')#基本要素页面申购按钮

    def info_text(self):
        '''获取基本要素页面产品详情'''
        element = self.find_elements(self.info_loc)[2]
        text = element.text
        return text

    def purchase_button1(self):
        '''点击基本要素页面申购按钮'''
        self.click(self.purchase1_loc)


    '''风险揭示书页面'''
    book_loc = ('class name','no-redirect')#风险揭示书定位
    check_box_loc = ('class name','el-checkbox__inner')#勾选框定位
    confirm_loc = ('class name','is-plain')#确认按钮定位

    def disclosure_book(self):
        '''获取风险揭示书'''
        text = self.find_element(self.book_loc).text
        return text

    def check_box_confirm_butten(self):
        '''定位勾选框-点击确认按钮'''
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
        '''点击确认按钮'''
        element = self.find_elements(self.confirm_loc)[1]
        element.click()

    '''申购页面'''
    apply_loc = ('class name','no-redirect') #申购页面申购申请元素定位
    purchase_confirm_loc = ('class name','el-checkbox__inner')#申购页面勾选框
    purchase_amount_loc = ('class name','el-input__inner')#申购金额输入框
    purchase_button_loc = ('class name','is-plain')#申购页面提交按钮

    def apply(self):
        '''申购页面申购申请元素'''
        text = self.find_element(self.apply_loc).text
        return text

    def purchase_button_jump(self,amount):
        '''申购页面点击勾选框-输入金额-点击确认按钮'''
        '''申购页面勾选框'''
        self.js_scroll_end(0, 1300)
        self.click(self.purchase_confirm_loc)
        time.sleep(1)
        '''申购页面输入金额'''
        self.send_keys(self.purchase_amount_loc, amount)
        time.sleep(1)
        '''点击提交按钮'''
        element = self.find_elements(self.purchase_button_loc)[1]
        element.click()

    def purchase_scenario(self,jump):
        '''申购流程'''
        time.sleep(2)
        self.viwe_button()
        time.sleep(1)
        self.purchase_button1()
        time.sleep(1)
        self.check_box_confirm_butten()
        time.sleep(1)
        self.purchase_button_jump(jump)
        time.sleep(1)

    '''提交页面'''
    successful_loc = ('xpath','//*[@id="app"]/div/div[2]/ul/div[2]/span[3]/span/span')    #提交页面操作成功信息

    def successful(self):
        '''提交页面提交成功定位'''
        text = self.find_element(self.successful_loc).text
        return text

    '''查看申赎记录'''
    menu_loc = ('class name', 'el-menu-item')  # 申赎记录菜单
    breadcrumb_loc = ('class name','no-redirect') #申赎记录
    cell_loc = ('class name', 'cell')  # 列表页面字段下数据

    def menu(self):
        '''点击申赎记录菜单'''
        element = self.find_elements(self.menu_loc)[3]
        element.click()

    def breadcrumb(self):
        '''获取面包屑'''
        text = self.find_element(self.breadcrumb_loc).text
        return text

    def apply_time(self):
        '''获取列表时间信息'''
        element = self.find_elements(self.cell_loc)[7]
        text = element.text
        return text[:10]

    def current_time(self):
        '''获取当前时间'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[:10]
        return time1

    def status(self):
        '''获取列表状态信息'''
        text = self.find_elements(self.cell_loc)[12].text
        return text


    '''管理端登录页面'''
    username_loc = ('id', 'login-name')  # 用户名称定位
    passwd_loc = ('id', 'login-password')  # 密码定位
    verification_loc = ('id', 'verifyCode')  # 验证码定位
    submit_loc = ('id', 'login-btn')  # 登录按钮定位
    longin_username_loc = ('id', 'username')

    # def username(self,username):
    #     '''用户名字段输入用户名'''
    #     self.send_keys(self.username_loc,username)
    #
    # def passwd(self,passwd):
    #     '''密码字段输入密码'''
    #     self.send_keys(self.passwd_loc,passwd)
    #
    # def verifi(self,verifi):
    #     '''验证码字段输入验证码'''
    #     self.send_keys(self.verification_loc,verifi)
    #
    # def sbm(self):
    #     '''点击登录按钮'''
    #     self.click(self.submit_loc)

    def type_username(self):
        '''获取登录页面用户名'''
        text = self.find_element(self.longin_username_loc).text
        return text

    def ManageLogin(self,username,passwd,verifi):
        '''用户名字段输入用户名'''
        self.send_keys(self.username_loc,username)
        time.sleep(1)
        self.send_keys(self.passwd_loc, passwd)
        time.sleep(1)
        self.send_keys(self.verification_loc, verifi)
        time.sleep(1)
        self.click(self.submit_loc)
        time.sleep(1)

    '''销售管理-预约申请列表页面'''
    menu_sales_loc = ('xpath','//span[text()="销售管理"]')#销售管理菜单
    '''列表'''
    status1_loc = ('xpath', '//*[@class="layui-table"]/tbody/tr[1]/td[7]/div')  # 状态
    operation_button_loc = ('class name','layui-btn')#操作按钮
    drop_down_loc = ('xpath','//*[@id="selectIDPop"]/div/div/i')#审核页面下拉选项
    select_loc = ('name','modules')
    rejected_loc = ('xpath','//*[@id="selectIDPop"]/div/dl/dd[2]')#驳回按钮
    determine_loc = ('class name','layui-layer-btn0')#确定按钮
    a = ('class name','main-left')
    def sales(self):
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)
    #
    # def top(self):
    #     '''菜单滚动条'''
    #     js = "document.getElementsByClassName('main-left')[0].scrollTop=10000"
    #     self.driver.execute_script(js)
    #
    # def appointment(self):
    #     '''点击预约申请菜单'''
    #     self.driver.find_element_by_link_text("预约申请").click()

    def click_menu(self):
        '''菜单操作'''
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)
        time.sleep(1)
        '''菜单滚动条'''
        js = "document.getElementsByClassName('main-left')[0].scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(1)
        '''点击预约申请菜单'''
        self.driver.find_element_by_link_text("预约申请").click()

    def manage_status(self):
        '''状态'''
        text = self.find_element(self.status1_loc).text
        return text
    '''滚动条'''
    def scroll(self):
        self.js_scroll_end(0, 1000)

    def scroll_lift(self):
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def window_scroll(self):
        '''窗口操作'''
        '''滚动条向下到底'''
        self.js_scroll_end(0, 1000)
        time.sleep(1)
        '''内置滚动条向右'''
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def operation_button(self):
        '''点击操作按钮'''
        self.find_elements(self.operation_button_loc)[1].click()

    def audit_button(self):
        '''点击审核按钮'''
        js = "document.getElementById('purchase-edit').click()"
        self.js_execute(js)

    def drop_down(self):
        '''点击审核下拉'''
        self.click(self.drop_down_loc)

    def rejected(self):
        '''点击驳回按钮'''
        self.click(self.rejected_loc)

    def determine(self):
        '''点击确定按钮'''
        self.click(self.determine_loc)


    def audit_rejected(self):
        '''审核驳回'''
        self.operation_button()
        time.sleep(1)
        self.audit_button()
        time.sleep(1)
        self.drop_down()
        time.sleep(1)
        self.rejected()
        time.sleep(1)
        self.determine()

    def audit_through(self):
        '''审核通过'''
        self.click_menu()
        time.sleep(1)
        self.window_scroll()
        time.sleep(1)
        self.operation_button()
        time.sleep(1)
        self.audit_button()
        time.sleep(1)
        self.determine()

    '''合同管理'''
    contract_operation_loc = ('xpath','//*[@class="layui-table"]/tbody/tr[1]/td[9]/div/a')#操作按钮
    conract_states_loc = ('xpath','//*[@class="layui-table"]/tbody/tr[1]/td[6]/div')#合同状态
    return_states_loc = ('xpath','//*[@class="layui-table"]/tbody/tr[1]/td[7]/div')#回访状态
    contract_no_loc = ('id','contractNo')#合同编码
    time_input_loc = ('id','netValueDate')#时间输入框
    agent_loc = ('id','agent')#经办人输入框
    serviceCharge_loc = ('id','serviceCharge')#手续费
    calmnessPeriod_loc = ('id','calmnessPeriod')#冷静期
    contract_save_loc = ('id','contract-save')#保存按钮



    def contract_menu(self):
        '''点击合同管理菜单'''
        self.driver.find_element_by_link_text('合同管理').click()

    def conract_operation(self):
        '''点击操作按钮'''
        self.click(self.contract_operation_loc)

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
        self.js_scroll_end(0,0)

    def conract_no(self):
        '''合同编码输入'''
        now_time = datetime.datetime.now()
        self.send_keys(self.contract_no_loc,'HT%s' %now_time)

    def time_input(self):
        '''时间输入框'''
        js = "document.getElementById('netValueDate').removeAttribute('readonly')"
        self.driver.execute_script(js)
        self.send_keys(self.time_input_loc,'2018-04-18')

    def serviceCharge(self):
        '''手续费'''
        self.send_keys(self.serviceCharge_loc,'1')


    def agent(self):
        '''经办人输入框'''
        self.send_keys(self.agent_loc,'刘鑫')


    def calmnessPeriod(self):
        '''冷静期输入框'''
        self.send_keys(self.calmnessPeriod_loc,'0')

    def contract_save(self):
        '''点击保存按钮'''
        self.click(self.contract_save_loc)

    def edit(self):
        '''进入页面进行编辑'''
        self.conract_operation()
        time.sleep(1)
        self.conract_edit()
        time.sleep(1)
        self.scroll_on()
        self.conract_no()
        self.time_input()
        self.serviceCharge()
        self.agent()
        self.calmnessPeriod()
        self.contract_save()

    '''确认已付款'''

    paymentTime_loc = ('id','paymentTime')#付款时间
    payment_current_loc =('xpath','//span[text()="现在"]')
    layui_layer_btn0_loc = ('class name','layui-layer-btn0')#确认按钮

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

    def payment(self):
        '''确认付款'''
        self.window_scroll()
        time.sleep(1)
        self.conract_operation()
        time.sleep(1)
        self.contract_payment()
        time.sleep(1)
        self.paymentTime()
        time.sleep(1)
        self.payment_current()
        time.sleep(1)
        self.layui_layer_btn0()


    '''发送回访单'''
    returm_determine_loc = ('class name','layui-layer-btn0')

    def contract_returm(self):
        '''点击发送回访单按钮'''
        js = "document.getElementById('send-tick').click()"
        self.js_execute(js)
    def returm_determine(self):
        '''点击弹出回访单页面确认按钮'''
        self.click(self.returm_determine_loc)

    def from_returm(self):
        '''发送回访单'''
        self.window_scroll()
        time.sleep(1)
        self.conract_operation()
        time.sleep(1)
        self.contract_returm()
        time.sleep(1)
        self.returm_determine()

    '''PC端回访单'''
    fundBuyForm_loc = ('xpath','//*[@id="fundBuyForm"]/div[1]/h3')
    number_loc = ('class name','el-radio')
    return_visit_consider_loc = ('xpath','//span[text()="考虑一下"]')
    return_visit_submit_loc = ('xpath','//span[text()="提交"]')

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

    def even_submit(self):
        '''点击是提交'''
        self.even_number()
        time.sleep(1)
        self.return_visit_submit()
        self.return_visit_submit()

    def odd_sbumit(self):
        '''点击否提交'''
        self.odd_number()
        time.sleep(1)
        self.return_visit_submit()
        self.return_visit_submit()


    '''产品类表退出'''
    product_drop_down_loc = ('class name','el-icon-caret-bottom')
    product_exit_loc = ('xpath','//span[text()="退出"]')

    def product_drop_down(self):
        '''点击下拉'''
        self.click(self.product_drop_down_loc)

    def product_eixt(self):
        '''点击退出按钮'''
        self.click(self.product_exit_loc)

    def pc_exit(self):
        '''PC端退出'''
        self.product_drop_down()
        time.sleep(1)
        self.product_eixt()

    '''回访确认'''
    visit_confirm_button_loc = ('class name','layui-layer-btn0')#确认回访页面确认按钮
    visit_rejected_loc = ('xpath','//div[text()="驳回"]')#确认回访页面驳回单选框

    def visit_rejected(self):
        self.click(self.visit_rejected_loc)

    def confirm_page_confirm_butten(self):
        '''点击回访确认按钮，跳转回访确认页面，点击确认按钮'''
        js = "document.getElementById('make-sure').click()"
        self.js_execute(js)
        time.sleep(1)
        '''点击确认按钮'''
        self.click(self.visit_confirm_button_loc)

    '''合同页面 进行合同编辑，发送回访单'''
    def contract_eidt_returm_buy(self):
        '''合同-编辑-回访'''
        self.contract_menu()
        time.sleep(1)
        self.edit()
        time.sleep(1)
        self.payment()
        time.sleep(1)
        self.from_returm()

    '''合同页面，进行客户回访单不想买，管理员进行拒绝'''
    def contract_returm_refused(self):
        '''合同-回访单拒绝'''
        self.sales()
        time.sleep(1)
        self.contract_menu()
        time.sleep(1)
        self.conract_operation()
        time.sleep(1)
        js = "document.getElementById('make-sure').click()"
        self.js_execute(js)
        time.sleep(1)
        self.js_scroll_end(0,1000)
        time.sleep(1)
        self.visit_rejected()
        time.sleep(1)
        self.click(self.visit_confirm_button_loc)

    def contract_returm_through(self):
        '''合同-回访单通过'''
        self.sales()
        time.sleep(1)
        self.contract_menu()
        time.sleep(1)
        self.conract_operation()
        time.sleep(1)
        self.confirm_page_confirm_butten()


















if __name__ == '__main__':
    driver = browser()
    po = PcScenario(driver)
    po.open_url('http://boss.pb-yun.com')
    po.ManageLogin('13511055879', '123456', '')
    time.sleep(1)
    po.sales()
    time.sleep(1)
    po.contract_menu()
    time.sleep(1)
    po.window_scroll()
    time.sleep(1)
    po.conract_operation()



    # text = po.funbuyform()
    # print(text)
    # po.even_number()
    # po.return_visit_submit()
    # po.return_visit_submit()
    # po.return_visit_consider()
    # po.return_visit_consider()



    # po.ManageLogin('13511055879','123456','')
    # po.sales()
    # time.sleep(2)
    # po.contract_menu()
    # time.sleep(1)
    # po.window_scroll()

    # time.sleep(1)
    # po.conract_operation()
    # time.sleep(1)
    # po.contract_returm()
    # time.sleep(1)
    # po.returm_determine()

    # po.edit()
    # time.sleep(1)
    # po.payment()

    # po.conract_operation()
    # time.sleep(1)
    # po.contract_payment()
    # time.sleep(1)
    # po.paymentTime()
    # time.sleep(1)
    # po.payment_current()
    # time.sleep(1)
    # po.layui_layer_btn0()
    #合同状态


    # po.confirm_payment()
    # po.layui_layer_btn0()


    # time.sleep(1)



    # time.sleep(1)
    # text = po.type_username()
    # print(text)
    # time.sleep(1)
    # po.click_menu()
    # time.sleep(1)
    # text1 = po.manage_status()
    # print(text1)
    # time.sleep(1)
    # po.window_scroll()
    # time.sleep(1)
    # po.operation_button()
    # time.sleep(1)
    # po.audit_button()
    # time.sleep(1)
    # po.drop_down()
    # po.rejected()
    # time.sleep(1)
    # po.determine()












    # po.pc_login('13511055879','jzj198304','1')
    # text = po.login_name()
    # print(text)
    # time.sleep(1)
    # po.viwe_button()
    # text1 = po.info_text()
    # print(text1)
    # time.sleep(2)
    # po.purchase_button1()
    # text2 = po.disclosure_book()
    # print(text2)
    # time.sleep(1)
    # po.check_box()
    # time.sleep(1)
    # po.confirm_butten()
    # time.sleep(1)
    # text3 = po.apply()
    # print(text3)
    # po.purchase_confirm()
    # time.sleep(1)
    # po.purchase_amount('3000')
    # po.purchase_button2()
    # time.sleep(1)
    # po.menu()
    # time.sleep(1)
    # text5 = po.breadcrumb()
    # text4 = po.apply_time()
    # text6 = po.status()
    # print(text5)
    # print(text4)
    # print(text6)
    # print(123456)


    # po.sales()
    # time.sleep(2)
    # po.contract_menu()
    # po.window_scroll()
    # po.edit()
    # po.window_scroll()
    # po.conract_operation()
    # po.contract_payment()
    # po.paymentTime()
    # po.confirm_payment()
    # po.layui_layer_btn0()











