from common.pc_login import PCLogin,browser
from page.SafeManager.ManageLogin import ManageLoginPage
from page.PC.product.product_purchase import ProductPurchase
from page.PC.purchaserecord.purchase_record import PurchaseRrecord
from page.SafeManager.sellmanager.Appointment import Appointment
from page.SafeManager.sellmanager.ContractManager import ContractManager
from page.PC.pcinfo.PcReturnVisit import ReturnVisitt
from common.get_url import GetUrl


import time


pc_url = GetUrl().get_pc_url()


class PcScenario(PCLogin,ManageLoginPage,ProductPurchase,PurchaseRrecord,Appointment,ContractManager,ReturnVisitt):

    '''流程所有page'''

    '''pc端产品列表查看-申购-提交'''
    def purodut_scenarion(self, asstassertEqual, amount, ):
        '''PC管理端申购--提交页面'''
        self.viwe_button()                                          #点击产品列表页面查看按钮
        time.sleep(1)
        self.detaile_test(asstassertEqual)                          #获取产品详情页面【产品详情】并断言
        time.sleep(1)
        self.purchase_button()                                      #点击产品详情页面申购按钮
        time.sleep(1)
        self.disclosure_book(asstassertEqual)                       #获取风险揭示书页【风险揭示书】并断言
        time.sleep(1)
        self.check_box_button()                                     #点击风险揭示书页面复选框
        time.sleep(1)
        self.disclosure_book_confirm()                              #点击风险揭示书页面确认按钮
        time.sleep(1)
        self.apply_text(asstassertEqual)                            #获取申购页面【申购】并断言
        time.sleep(1)
        self.purchase_confirm(amount)                               #申购页面点击确认项、输入金额、点击确认按钮
        time.sleep(1)
        self.successful(asstassertEqual)                            #提交页面获取【提交成功】并断言

    '''申赎记录列表页面'''
    def purchase_record(self,asstassertEqual,status):
        '''申赎记录页面-查看是否增加数据'''
        self.menu()                                                  #点击申赎记录菜单
        time.sleep(1)
        asstassertEqual(self.breadcrumb(),'申赎记录')               #获取页面【申赎记录】并断言
        time.sleep(1)
        asstassertEqual(self.status(),status)                        #获取列表页面数据状态并断言

    '''销售管理-预约申请页面'''
    def appointment_apply(self,asstassertEqual):
        '''销售管理-预约申请页面审核'''
        self.click_menu()                                             #点击销售管理-预约申请菜单
        time.sleep(1)
        self.window_scroll()                                          #窗口向下向右移动
        time.sleep(1)
        asstassertEqual(self.manage_status(),'未审核')               #获取数据状态并进行断言
        time.sleep(1)
        self.operation_button()                                       #点击列表操作按钮
        time.sleep(1)
        self.audit_button()                                           #点击审核按钮跳转审核页面
        time.sleep(1)

    def audit_rejected(self):
        '''销售管理-预约申请列表页面审核-驳回'''
        self.drop_down()                                               #点击审核下拉
        time.sleep(1)
        self.rejected()                                                #选取驳回
        time.sleep(1)
        self.determine()                                               #点击确定

    '''销售管理--合同管理'''
    def sell_contract(self):
        '''点击菜单销售管理-合同管理'''
        self.sales()
        time.sleep(1)
        self.contract_menu()

    def contract_operation(self,asstassertEqual,contract_status,return_status):

        '''合同管理页面：进入管理菜单-点击操作按钮'''
        self.contract_menu()                                           #点击合同管理菜单，进入列表页面
        time.sleep(1)
        self.window_scroll()                                           #列表页面滚动条移动
        time.sleep(1)
        asstassertEqual(self.conract_status(),contract_status)         #获取列表页面合同状态并断言
        asstassertEqual(self.return_status(),return_status)            #获取列表回访状态并断言
        time.sleep(1)
        self.conract_operation()                                       #点击列表页面操作按钮
        time.sleep(1)

    def conract_edit_button(self,time1,cost,name,calm_time):

        '''合同管理页面-合同编辑'''
        self.conract_edit()                                            #点击列表页面编辑按钮
        time.sleep(1)
        self.scroll_on()                                               #页面滚动至最上面
        time.sleep(1)
        self.conract_no()                                              #输入合同编码
        time.sleep(1)
        self.time_input(time1)                                          #时间输入
        time.sleep(1)
        self.serviceCharge(cost)                                        #输入金额
        time.sleep(1)
        self.agent(name)                                                #输入经办人
        time.sleep(1)
        self.calmnessPeriod(calm_time)                                  #冷静期
        time.sleep(1)
        self.contract_save()                                            #点击确定按钮

    def conract_payment(self):
        '''确认付款'''
        self.window_scroll()
        time.sleep(1)
        self.conract_operation()                                        #点击操作按钮
        time.sleep(1)
        self.contract_payment()                                         #点击确认付款按钮
        time.sleep(1)
        self.paymentTime()                                              #输入付款时间
        time.sleep(1)
        self.payment_current()                                          #点击现在按钮
        time.sleep(1)
        self.layui_layer_btn0()                                         #点击确认按钮
        time.sleep(4)

    def from_returm(self):
        '''发送回访单'''
        self.window_scroll()                                            #移动窗口
        time.sleep(1)
        self.conract_operation()                                        #点击操作按钮
        time.sleep(1)
        self.contract_returm()                                          #点击发动回访单按钮
        time.sleep(1)
        self.returm_determine()                                         #点击回访单页面确认按钮


    '''PC端回访单'''

    def even_submit(self):
        '''点击是提交'''
        self.even_number()                                              #选取是
        time.sleep(1)
        self.return_visit_submit()                                      #点击回访单页面提交按钮

    def odd_sbumit(self):
        '''点击否提交'''
        self.odd_number()                                               #选取否
        time.sleep(1)
        self.return_visit_submit()                                      #点击回访单页面提交按钮







if __name__ == '__main__':
    driver = browser()
    po = PcScenario(driver)
    po.open_url('http://boss.pb-yun.com/')
    po.pc_login('13511055879', '123456', '')
    time.sleep(4)
    po.sales()
    time.sleep(1)
    po.contract_operation()
    time.sleep(1)
















