"""
@author:liuxin
@date:2018-8-7
@brief:数据维护-所有产品-数据日历页面测试用例
"""



import unittest
import platform
from pyvirtualdisplay import Display
import time

from page.SafeManager.data_maintenance.data_calendar import Calendar, browser, manager_url
from common.log import logger
url = "http://testpvt.boss.pb-test.com/#/dataMaintain/DataCalendar?fundCode=910070&fundName=%E3%80%90SX7490%E3%80%91%E5%85%B4%E9%91%AB-%E6%B4%9B%E4%B9%A6%E7%9D%BF%E4%B8%B4%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86%E8%AE%A1%E5%88%92"
@unittest.skip('pass')
class DataCalendar(unittest.TestCase):
    """对数据维护-所有产品-数据日历页面所有元素的测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.syt = platform.system()
        if cls.syt == 'Linux':
            cls.display = Display(visible=0, size=(5120, 2880))
            cls.display.start()
        cls.browser = browser()
        cls.driver = Calendar(cls.browser)
        cls.driver.open_url(manager_url)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.syt == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.lx_manager_login()
        # self.driver.click_bar()
        # self.driver.click_date()
        self.driver.open_url(url)

    def tearDown(self):
        time.sleep(1)

    def test_c_return(self):
        """点击数据日历页面的返回列表按钮测试用例"""
        try:
            time.sleep(2)
            self.driver.get_shot('abc.jpg')
            js = "return document.documentElement.outerHTML"
            html = self.driver.js_execute(js)
            print(html)
            # jpgself.driver.find_elements(('class name', 'el-button--medium'))[2].click()
            # time.sleep(1)
            self.driver.get_shot('bcd.jpg')
            # log_text = self.driver.find_element(('class name', 'hovers')).text
            # self.assertEqual(log_text, '所有产品')
        except Exception as msg:
            logger.info(str(msg))
            raise


if __name__ == '__main__':
    unittest.main()

