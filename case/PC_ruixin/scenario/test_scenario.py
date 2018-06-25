from page.PC.pcscenario import PcScenario
from page.PC.pcscenario.PcScenario import PcScenario,browser,pc_url
from common.log import logger

from selenium.webdriver.support.wait import WebDriverWait
from pyvirtualdisplay import Display
from time import sleep
import unittest
import platform


class TestScenario(unittest.TestCase):
    """申购-审核流程"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = PcScenario(cls.driver)
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        "初始化"

    def tearDown(self):
        sleep(2)
        "结束"

    def test_purchase_rejected(self):
        '''申购-审核驳回流程'''
        try:
            self.browser.pc_login('15822816936', 'abc123456', '1')                # 登录
            sleep(1)
            self.browser.purodut_scenarion(self.assertEqual, 2000)                  # PC申购--提交成功
            sleep(1)
            self.browser.purchase_record(self.assertEqual,'未审核')                 # 进入申赎记录页面获取数据状态断言
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')                      # 进入管理端
            sleep(1)
            self.browser.ManageLogin('13511055879', '123456', '')                 # 管理端输入账号密码
            sleep(3)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span') # 显示等待
            sleep(1)
            self.browser.appointment_apply(self.assertEqual)                        # 进入销售管理-预约申请页面-获取数据状态-断言
            sleep(1)
            self.browser.audit_rejected()                                           #审核驳回
            sleep(1)
            self.assertEqual(self.browser.manage_status(),'已驳回')                #获取列表状态并断言
            sleep(1)
            self.browser.open_url('http://inv.pb-yun.com')                        #进入PC端申赎列表查看数据状态并断言
            sleep(1)
            self.browser.purchase_record(self.assertEqual, '已驳回')               #进入申赎记录列表页面查看数据状态并断言

        except Exception as msg:
            self.log.info(msg)
            raise


    def test_purchase_through(self):
        '''申购-审核-通过-合同管理编辑-确认付款-回访单确认-想买'''
        try:
            self.browser.open_url('http://inv.pb-yun.com')
            sleep(1)
            self.browser.pc_login('15822816936', 'abc123456', '1')                # 登录
            sleep(1)
            self.browser.purodut_scenarion(self.assertEqual, 2000)                  # PC申购--提交成功
            sleep(1)
            self.browser.purchase_record(self.assertEqual,'未审核')                 # 进入申赎记录页面获取数据状态断言
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')                      # 进入管理端
            sleep(1)
            self.browser.ManageLogin('13511055879', '123456', '')                 # 管理端输入账号密码
            sleep(3)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span') # 显示等待
            sleep(1)
            self.browser.appointment_apply(self.assertEqual)                        # 进入销售管理-预约申请页面-获取数据状态-断言
            sleep(1)
            self.browser.determine()                                                #审核通过
            sleep(1)
            self.assertEqual(self.browser.manage_status(),'已通过')                #进入列表页面进行断言
            sleep(1)
            self.browser.contract_operation(self.assertEqual,'未付款','未回访')    #进入合同管理列表页面，数据状态断言，点击操作按钮
            sleep(1)
            self.browser.conract_edit_button('2018-04-26',1,'刘鑫','0')           #输入时间、手续费、经办人、冷静期保存
            sleep(1)
            self.browser.conract_payment()                                          #确认已付款页面点击进行确认
            sleep(1)
            self.assertEqual(self.browser.conract_status(),'已付款')               #数据状态断言-已付款
            self.browser.from_returm()                                              #回访单页面进行确认按钮
            sleep(1)
            self.assertEqual(self.browser.return_status(),'已发送')                #数据状态断言-已发送
            sleep(1)
            self.browser.open_url('http://inv.pb-yun.com')                        #登录投资者PC端
            sleep(1)
            self.browser.even_submit()                                              #PC回访单点击是提交
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')                      # 进入管理端
            sleep(1)
            self.browser.ManageLogin('13511055879', '123456', '')                 # 管理端输入账号密码
            sleep(1)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span') # 显示等待
            sleep(1)
            self.browser.sell_contract()                                            #点击销售管理-合同管理菜单
            sleep(1)
            self.assertEqual(self.browser.return_status(),'想买')                  #列表数据状态断言-想买


        except Exception as msg:
            self.log.info(msg)
            raise

    def test_purchase_visitrejected(self):
        '''申购-审核-通过-合同管理编辑-确认付款-回访单确认-想买'''
        try:
            self.browser.open_url('http://inv.pb-yun.com')
            sleep(1)
            self.browser.pc_login('15822816936', 'abc123456', '1')                # 登录
            sleep(1)
            self.browser.purodut_scenarion(self.assertEqual, 2000)                  # PC申购--提交成功
            sleep(1)
            self.browser.purchase_record(self.assertEqual,'未审核')                 # 进入申赎记录页面获取数据状态断言
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')                      # 进入管理端
            sleep(1)
            self.browser.ManageLogin('13511055879', '123456', '')                 # 管理端输入账号密码
            sleep(3)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span') # 显示等待
            sleep(1)
            self.browser.appointment_apply(self.assertEqual)                        # 进入销售管理-预约申请页面-获取数据状态-断言
            sleep(1)
            self.browser.determine()                                                #审核通过
            sleep(1)
            self.assertEqual(self.browser.manage_status(),'已通过')                #进入列表页面进行断言
            sleep(1)
            self.browser.contract_operation(self.assertEqual,'未付款','未回访')    #进入合同管理列表页面，数据状态断言，点击操作按钮
            sleep(1)
            self.browser.conract_edit_button('2018-04-26',1,'刘鑫','0')           #输入时间、手续费、经办人、冷静期保存
            sleep(1)
            self.browser.conract_payment()                                          #确认已付款页面点击进行确认
            sleep(1)
            self.browser.from_returm()                                              #回访单页面进行确认按钮
            sleep(1)
            self.assertEqual(self.browser.conract_status(),'已付款')               #数据状态断言-已付款
            sleep(1)
            self.browser.open_url('http://inv.pb-yun.com')                        #登录投资者PC端
            sleep(1)
            self.browser.odd_number()                                               #PC回访单点击否提交
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')                      # 进入管理端
            sleep(1)
            self.browser.ManageLogin('13511055879', '123456', '')                  # 管理端输入账号密码
            sleep(1)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span')  # 显示等待
            sleep(1)
            self.browser.sell_contract()                                             # 点击销售管理-合同管理菜单
            sleep(1)
            self.assertEqual(self.browser.return_status(), '不想买')                 # 列表数据状态断言-不想买

        except Exception as msg:
            self.log.info(msg)
            raise



if __name__ == "__main__":
    unittest.main()






