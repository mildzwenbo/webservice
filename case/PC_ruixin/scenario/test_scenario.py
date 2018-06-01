from page.PC.pcscenario import PcScenario
from page.PC.pcscenario.PcScenario import PcScenario,browser,pc_url
from common.log import logger


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
        "初始化"

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        "结束"

    def test_purchase_rejected(self):
        '''申购-审核驳回流程'''
        try:
            self.browser.pc_login('13511055879', 'jzj198304', '1')
            text = self.browser.login_name()
            self.assertEqual(text,'金战军')
            sleep(1)
            self.browser.viwe_button()
            sleep(1)
            text = self.browser.info_text()
            self.assertEqual(text, '基本信息')
            self.browser.purchase_button1()
            sleep(1)
            text = self.browser.disclosure_book()
            self.assertEqual(text, '风险揭示书')
            sleep(1)
            self.browser.book_jump()
            sleep(1)
            self.browser.purchase_button_jump(2000)
            sleep(1)
            self.assertEqual(self.browser.successful(),'操作成功')
            sleep(1)
            self.browser.menu()
            sleep(1)
            self.assertEqual(self.browser.time_status(),self.browser.current_time_status())
            sleep(1)
            self.browser.open_url('http://boss.pb-yun.com/')
            sleep(2)
            self.browser.ManageLogin('13511055879','123456','')
            self.assertEqual(self.browser.type_username(),'金战军')
            self.browser.click_menu()
            self.assertEqual(self.browser.manage_status(),'未审核')
            sleep(1)
            self.browser.window_scroll()
            sleep(1)
            self.browser.audit_rejected()
            sleep(2)
            self.assertEqual(self.browser.manage_status(),'已驳回')
        except Exception as msg:
            self.log.info(msg)
            raise


if __name__ == "__main__":
    unittest.main()






