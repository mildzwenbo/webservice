from page.PC.pcscenario import PcScenario
from page.PC.pcscenario.PcScenario import PcScenario,browser,pc_url


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
        '''申购-审核通过-合同管理流程'''
        try:
            self.browser.pc_login('13511055879', 'jzj198304', '1')
            self.browser.purchase_scenario(3000)
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')
            self.browser.ManageLogin('13511055879', '123456', '')
            sleep(1)
            self.browser.audit_through()
            sleep(2)
            # self.assertEqual(self.browser.manage_status(),'已通过')
            sleep(1)
            self.browser.contract_menu()
            sleep(1)
            self.assertEqual(self.browser.conract_states(),'未付款')
            self.assertEqual(self.browser.return_states(),'未回访')
            self.browser.window_scroll()
            sleep(1)
            self.browser.edit()

        except Exception as msg:
            self.log.info(msg)
            raise


if __name__ == '__main__':
    unittest.main()