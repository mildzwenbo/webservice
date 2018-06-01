from common.PC_login import PCLogin,browser
from common.get_url import GetUrl


import time
import datetime

pc_url = GetUrl().get_pc_url()


class PcScenario(PCLogin):

    '''流程页面'''
    '''产品列表页面元素'''
    name_loc = ('xpath','//*[@id="app"]/div/div[2]/ul/div[3]/div/div')#登录名称定位
    viwe_loc = ('xpath',' //*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/table/tbody/tr[1]/td[9]/div/button')#产品列表查看定位
    '''基本元素页面元素'''
    info_loc = ('xpath','//*[@id="pane-0"]/div[1]/div[2]/h3')#基本要素页面基本信息定位
    purchase1_loc = ('xpath','//*[@id="pane-0"]/div[1]/div[1]/div[2]/div[8]/dl/dd/button/span')#基本要素页面申购按钮
    '''风险揭示书页面'''
    book_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[1]/h3')#风险揭示书定位
    check_box_loc = ('class name','el-checkbox__inner')#勾选框定位
    confirm_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[5]/div/button[2]')#确认按钮定位
    '''申购页面'''
    apply_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[2]/h4') #申购页面申购申请元素定位
    purchase_confirm_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[8]/p/label/span/span')#申购页面勾选框
    purchase_amount_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[9]/form/div/div/div/input')#申购金额输入框
    purchase_button_loc = ('xpath','//*[@id="app"]/div/div[2]/section/div/div[10]/div/button[2]/span')#申购页面提交按钮
    '''提交页面'''
    successful_loc = ('xpath','//*[@id="app"]/div/div[2]/ul/div[2]/span[3]/span/span')    #提交页面操作成功信息



    '''产品列表页面'''
    def login_name(self):
        '''获取登录名称'''
        text = self.find_element(self.name_loc).text
        return text

    def viwe_button(self):
        '''点击查看按钮方法'''
        self.click(self.viwe_loc)

    '''基本要素页面'''

    def info_text(self):
        '''获取基本要素页面基本信息'''
        text = self.find_element(self.info_loc).text
        return text
    def purchase_button1(self):
        '''点击基本要素页面申购按钮'''
        self.click(self.purchase1_loc)


    '''风险揭示书页面'''

    def disclosure_book(self):
        '''获取风险揭示书'''
        text = self.find_element(self.book_loc).text
        return text

    def check_box(self):
        '''定位勾选框'''
        self.js_scroll_end(0, 1300)
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

    def confirm_butten(self):
        '''点击确认按钮'''
        self.click(self.confirm_loc)

    def book_jump(self):
        '''风险揭示书页面勾选点击提交按钮'''
        self.check_box()
        time.sleep(1)
        self.confirm_butten()


    '''申购页面'''
    def apply(self):
        '''申购页面申购申请元素'''
        text = self.find_element(self.apply_loc).text
        return text

    def purchase_confirm(self):
        '''申购页面勾选框'''
        self.js_scroll_end(0, 1300)
        self.click(self.purchase_confirm_loc)

    def purchase_amount(self,amount):
        '''申购页面输入金额'''
        self.send_keys(self.purchase_amount_loc,amount)

    def purchase_button2(self):
        '''点击提交按钮'''
        self.click(self.purchase_button_loc)

    def purchase_button_jump(self,amount):
        self.purchase_confirm()
        time.sleep(1)
        self.purchase_amount(amount)
        time.sleep(1)
        self.purchase_button2()

    def purchase_scenario(self,jump):
        '''申购流程'''
        time.sleep(2)
        self.viwe_button()
        time.sleep(1)
        self.purchase_button1()
        time.sleep(1)
        self.book_jump()
        time.sleep(1)
        self.purchase_button_jump(jump)
        time.sleep(1)



        '''提交页面'''
    def successful(self):
        '''提交页面提交成功定位'''
        text = self.find_element(self.successful_loc).text
        return text

    '''查看申赎记录'''
    menu_loc = ('xpath', '//*[@id="app"]/div/div[1]/ul/div/a[4]/li')  # 申赎记录菜单
    apply_time_loc = ('xpath', '//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div')  # 列表页面申请时间字段
    status_loc = ('xpath', '//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div')  # 列表状态字段

    def menu(self):
        '''点击申赎记录菜单'''
        self.click(self.menu_loc)

    def apply_time(self):
        '''获取列表时间信息'''
        text = self.find_element(self.apply_time_loc).text
        return text[:10]

    def current_time(self):
        '''获取当前时间'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[:10]
        return time1

    def status(self):
        '''获取列表状态信息'''
        text = self.find_element(self.status_loc).text
        return text

    def time_status(self):
        submit = []
        time = self.apply_time()
        submit.append(time)
        statu = self.status()
        submit.append(statu)
        return submit

    def current_time_status(self):
        submit1 = []
        time1 = self.current_time()
        submit1.append(time1)
        statu2 = '未审核'
        submit1.append(statu2)
        return submit1

    '''管理端登录页面'''
    username_loc = ('id', 'login-name')  # 用户名称定位
    passwd_loc = ('id', 'login-password')  # 密码定位
    verification_loc = ('xpath', '//*[@id="verifyCode"]')  # 验证码定位
    submit_loc = ('xpath', '//*[@id="login-btn"]')  # 登录按钮定位
    longin_username_loc = ('xpath', '//*[@id="username"]')

    def username(self,username):
        '''用户名字段输入用户名'''
        self.send_keys(self.username_loc,username)

    def passwd(self,passwd):
        '''密码字段输入密码'''
        self.send_keys(self.passwd_loc,passwd)

    def verifi(self,verifi):
        '''验证码字段输入验证码'''
        self.send_keys(self.verification_loc,verifi)

    def sbm(self):
        '''点击登录按钮'''
        self.click(self.submit_loc)

    def type_username(self):
        '''获取登录页面用户名'''
        text = self.find_element(self.longin_username_loc).text
        return text

    def ManageLogin(self,usernam,passwd,verifi):
        self.username(usernam)
        time.sleep(1)
        self.passwd(passwd)
        time.sleep(1)
        self.verifi(verifi)
        time.sleep(1)
        self.sbm()
        time.sleep(4)

    '''销售管理-预约申请列表页面'''
    '''菜单'''
    menu_sales_loc = ('xpath', '/html/body/div[1]/div[2]/div[1]/ul/li[9]/div/span')  # 菜单销售管理
    menu_appointment_loc = ('xpath', '/html/body/div[1]/div[2]/div[1]/ul/li[9]/ul/li[4]/a')  # 菜单预约申请
    '''列表'''
    apply1_time_loc = ('xpath', '//*[@id="main-right"]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[5]/div')  # 申请时间
    status1_loc = ('xpath', '//*[@id="main-right"]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/div')  # 状态
    operation_button_loc = ('xpath','//*[@id="main-right"]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[10]/div/a')#操作按钮
    drop_down_loc = ('xpath','//*[@id="selectIDPop"]/div/div/i')

    rejected_loc = ('xpath','//*[@id="selectIDPop"]/div/dl/dd[2]')#驳回按钮
    determine_loc = ('class name','layui-layer-btn0')#确定按钮
    a = ('class name','main-left')
    def sales(self):
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)

    def top(self):
        '''菜单滚动条'''
        js = "document.getElementsByClassName('main-left')[0].scrollTop=10000"
        self.driver.execute_script(js)

    def appointment(self):
        '''点击预约申请菜单'''
        self.click(self.menu_appointment_loc)

    def click_menu(self):
        self.sales()
        time.sleep(1)
        self.top()
        time.sleep(1)
        self.appointment()

    def manage_status(self):
        '''状态'''
        text = self.find_element(self.status1_loc).text
        return text
    '''滚动条'''
    def scroll(self):
        self.js_scroll_end(0, 800)

    def scroll_lift(self):
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.driver.execute_script(js)

    def window_scroll(self):
        '''窗口操作'''
        self.scroll()
        time.sleep(1)
        self.scroll_lift()

    def operation_button(self):
        '''点击操作按钮'''
        self.click(self.operation_button_loc)

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
        self.sales()
        time.sleep(1)
        self.top()
        time.sleep(2)
        self.appointment()
        time.sleep(1)
        self.window_scroll()
        time.sleep(1)
        self.operation_button()
        time.sleep(1)
        self.audit_button()
        time.sleep(1)
        self.determine()

    '''合同管理'''
    contract_menu_loc = ('xpath','/html/body/div[1]/div[2]/div[1]/ul/li[9]/ul/li[1]/a')#合同管理菜单
    contract_operation_loc = ('xpath','//*[@id="main-right"]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/a')#操作按钮
    conract_status_loc = ('xpath','//*[@id="main-right"]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[6]/div')#合同状态
    return_states_loc = ('xpath','//*[@id="main-right"]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div')#回访状态
    contract_no_loc = ('id','contractNo')#合同编码
    time_input_loc = ('id','netValueDate')#时间输入框
    agent_loc = ('id','agent')#经办人输入框
    serviceCharge_loc = ('id','serviceCharge')#手续费
    calmnessPeriod_loc = ('id','calmnessPeriod')#冷静期
    contract_save_loc = ('id','contract-save')#保存按钮



    def contract_menu(self):
        '''点击合同管理菜单'''
        self.click(self.contract_menu_loc)

    def conract_operation(self):
        '''点击操作按钮'''
        self.click(self.contract_operation_loc)

    def conract_states(self):
        '''数据状态'''
        text = self.find_element(self.conract_status_loc).text
        return text

    def return_states(self):
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
    confirm_payment_loc = ('xpath','//*[@id="layui-layer100008"]/div[1]')
    layui_layer_btn0_loc = ('class name','layui-layer-btn0')#确认按钮

    def contract_payment(self):
        '''点击确认已付款按钮'''
        js = "document.getElementById('contract-payment').click()"
        self.js_execute(js)

    def paymentTime(self):
        '''输入付款时间'''
        js = "document.getElementById('paymentTime').removeAttribute('readonly')"
        driver.execute_script(js)
        self.send_keys(self.paymentTime_loc, '2018-05-30')

    def confirm_payment(self):
        '''点击确认已付款'''
        self.click(self.confirm_payment_loc)


    def layui_layer_btn0(self):
        '''点击确认按钮'''
        self.click(self.layui_layer_btn0_loc)



if __name__ == '__main__':

    driver = browser()
    po = PcScenario(driver)
    po.open_url('http://boss.pb-yun.com/')
    po.ManageLogin('13511055879','123456','')
    po.sales()
    time.sleep(2)
    po.contract_menu()
    po.window_scroll()
    po.edit()
    po.window_scroll()
    po.conract_operation()
    po.contract_payment()
    po.paymentTime()
    po.confirm_payment()
    po.layui_layer_btn0()











