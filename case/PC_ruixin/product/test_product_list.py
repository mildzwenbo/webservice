
import unittest
import platform
from pyvirtualdisplay import Display
import time

from page.PC.product.product_list import ProductList, browser, pc_url
from common.log import logger


class TestHome(unittest.TestCase):
    """产品列表页面测试"""
    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 900))
            cls.display.start()
        cls.driver = browser()
        cls.browser = ProductList(cls.driver)
        cls.log = logger
        cls.browser.open_url(pc_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.pc_login('15822816936', 'abc123456', '1')

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()

    def test_click_home(self):
        """点击Home按钮，进入Home页面"""
        try:
            self.browser.home_click()
            time.sleep(1)
            text = self.browser.get_text(('css', '#app > div > div.main-container > '
                                                 'section > div > div:nth-child(2) > span'))
            self.assertEqual('产品名称', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_click_username(self):
        """点击用户名称"""
        try:
            self.browser.username_click()
            text = self.browser.get_text(self.browser.quit_loc)
            time.sleep(1)
            self.assertTrue('退出', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_quit_click(self):
        """退出登录"""
        try:
            self.browser.username_click()
            time.sleep(1)
            self.browser.quit_click()
            text = self.browser.get_text(('class name', 'title'))
            self.assertEqual('基金运营管理系统', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_personal_information_click(self):
        """点击个人信息"""
        try:
            self.browser.username_click()
            time.sleep(1)
            self.browser.personal_information_click()
            time.sleep(1)
            text = self.browser.find_elements(('class name', 'clearfix'))[0].text
            self.assertEqual('账户信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_search_input(self):
        """查询输入框中输入：测试，点击查询，查看结果第一条查询结果"""
        try:
            self.browser.input_search('测试')
            self.browser.search_click()
            time.sleep(1)
            text = self.browser.get_text(('xpath', '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]'
                                                   '/table/tbody/tr[1]/td[2]/div'))
            self.assertIn('测试', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_risk_level_click(self):
        """点击查看更高风险等级产品按钮"""
        try:
            self.browser.risk_level_click()
            time.sleep(1)
            text = self.browser.get_text(('css', '#app > div > div.main-container > section > div > '
                                                 'div:nth-child(1) > h3'))
            self.assertEqual('风险不匹配警示函', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_product_search(self):
        """点击列表中第一个产品的操作栏下的查看按钮"""
        try:
            self.browser.product_search_click()
            time.sleep(1)
            text = self.browser.get_text(('css', '#pane-0 > div:nth-child(1) > div:nth-child(2) > h3'))
            self.assertEqual('基本信息', text)
        except Exception as msg:
            self.log.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()
