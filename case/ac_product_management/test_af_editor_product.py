"""
@author:fei
@date:2018-08-22
@brief:编辑已发布页面的测试用例
"""

from pyvirtualdisplay import Display
import unittest
import time
import platform

from common.log import logger
from page.SafeManager.product_management.published_product.editor_product import editor_product_url, EditorProduct, manager_url, browser



class TestEditorProduct(unittest.TestCase):
    """编辑已发布产品"""

    @classmethod
    def setUpClass(cls):
        cls.sty = platform.system()
        if cls.sty == 'Linux':
            cls.display = Display(visible=0, size=(2560, 1600))
            cls.display.start()
        cls.browser = browser()
        cls.driver = EditorProduct(cls.browser)
        cls.driver.open_url(manager_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        if cls.sty == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.driver.yf_manager_login()
        time.sleep(1)
        self.driver.open_url(editor_product_url)
        time.sleep(1)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_a_editor_product(self):
        """在投资信息下主要投资方向编辑信息"""
        try:
            self.driver.editor_product()
            time.sleep(1)
            text = self.driver.get_text(('class name', 'el-message__content'))
            self.assertEqual('保存成功', text)
        except Exception as msg:
            logger.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()
