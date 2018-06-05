from page.PC.pcscenario import PcScenario
from page.PC.pcscenario.PcScenario import PcScenario,browser,pc_url

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyvirtualdisplay import Display
from common.log import logger
from time import sleep
import unittest
import platform


class TestScenario(unittest.TestCase):
    """申购流程"""
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

        "初始化"

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        "结束"

    def test_purchase_through(self):
        '''申购-审核通过-合同管理-回访确认-不购买'''
        try:
            self.browser.pc_login('13511055879', 'jzj198304', '1')
            self.browser.purchase_scenario(3000)
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')
            self.browser.ManageLogin('13511055879', '123456', '')
            sleep(3)
            WebDriverWait(self.driver,'By.XPATh','//*[@id="detailName"]/span')
            self.browser.audit_through()
            sleep(2)
            self.assertEqual(self.browser.manage_status(),'已通过')
            sleep(1)
            self.browser.contract_menu()
            sleep(1)
            self.assertEqual(self.browser.conract_status(),'未付款')
            self.assertEqual(self.browser.return_status(),'未回访')
            self.browser.window_scroll()
            sleep(1)
            self.browser.edit()
            sleep(1)
            self.browser.payment()
            self.assertEqual(self.browser.conract_status(),'已付款')
            sleep(1)
            self.browser.from_returm()
            sleep(1)
            self.assertEqual(self.browser.return_status(),'已发送')
            sleep(1)
            self.browser.open_url('http://inv.pb-yun.com')
            sleep(1)
            self.assertEqual(self.browser.funbuyform(),'基金购买回访单')
            self.browser.return_visit_consider()
            self.browser.return_visit_consider()
            sleep(1)
            self.browser.pc_exit()
            self.browser.open_url('http://inv.pb-yun.com')
            sleep(1)
            self.browser.odd_number()
            sleep(1)
            self.browser.return_visit_submit()
            self.browser.return_visit_submit()
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')
            self.browser.ManageLogin('13511055879', '123456', '')
            sleep(3)
            WebDriverWait(self.driver, 'By.XPATh', '//*[@id="detailName"]/span')
            sleep(3)
            self.browser.sales()
            sleep(1)
            self.browser.contract_menu()
            sleep(1)
            self.assertEqual(self.browser.return_status(),'不想买')
            self.browser.window_scroll()
            sleep(1)
            self.browser.conract_operation()
            sleep(1)
            self.browser.confirm_page_confirm_butten()
            self.assertEqual(self.browser.return_status(),'已通过')
            self.assertEqual(self.browser.conract_status(),'不购买')

        except Exception as msg:
            self.log.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()