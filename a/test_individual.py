"""
@author:xin
@date:2018-7-3
@brief:管理端-客户管理-个人客户各项功能测试用例
"""

import os
import platform
import time
import unittest


from pyvirtualdisplay import Display

from common.log import logger
from common.read_excel import ReadExcel
from page.SafeManager.client.individual_client import IndividualClient, browser, manager_url
from selenium.webdriver.common.keys import Keys

class Individual(unittest.TestCase):
    """客户管理-个人客户各项功能测试用例"""

    @classmethod
    def setUpClass(cls):
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display = Display(visible=0, size=(1280, 800))
            cls.display.start()
        cls.log = logger
        cls.driver = browser()
        cls.browser = IndividualClient(cls.driver)
        cls.browser.open_url(manager_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        syt = platform.platform()
        if syt[:5] == 'Linux':
            cls.display.stop()

    def setUp(self):
        self.browser.delete_all_cookies()
        self.browser.refresh()
        self.browser.lx_manager_login()
        self.browser.click_client()

    def tearDown(self):
        time.sleep(1)
        self.browser.click(self.browser.quit_button)
        self.browser.click(self.browser.confirm)
        time.sleep(1)

    def test_client_inquire(self):
        """客户名称查询结果"""
        try:
            self.browser.find_client('查询')
            self.browser.click_inquire()
            result = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result), 4)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_investor_inquire(self):
        # 投资者分类：普通投资者查询结果
        try:
            time.sleep(1)
            self.browser.find_investor()
            self.browser.click_inquire()
            result1 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result1), 6)
            # 投资者分类：专业投资者查询结果
            self.browser.find_profession()
            self.browser.click_inquire()
            time.sleep(1)
            result2 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result2), 2)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_risk_inquire(self):
        """风险等级偏好：C1查询结果"""
        try:
            time.sleep(1)
            self.browser.find_c1()
            self.browser.click_inquire()
            result1 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result1), 2)
            # 风险等级偏好：C2查询结果
            self.browser.find_c2()
            self.browser.click_inquire()
            time.sleep(1)
            result2 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result2), 2)
            # 风险等级偏好：C3查询结果
            self.browser.find_c3()
            self.browser.click_inquire()
            time.sleep(1)
            result3 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result3), 2)
            # 风险等级偏好：C4查询结果
            self.browser.find_c4()
            self.browser.click_inquire()
            time.sleep(1)
            result4 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result4), 3)
            # 风险等级偏好：C5查询结果
            self.browser.find_c5()
            self.browser.click_inquire()
            time.sleep(1)
            result5 = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result5), 2)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_sell_inquire(self):
        """销售代表查询结果"""
        try:
            self.browser.find_sell('刘鑫')
            self.browser.click_inquire()
            result = self.browser.find_elements(('class name', 'laytable-cell-checkbox'))
            self.assertEqual(len(result), 4)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_bulk_import(self):
        """批量导入-下载模板"""
        try:
            time.sleep(1)
            self.browser.click_template()
            # 删除文件夹下的指定文件
            # path = "..\..\..\Download\个人投资者模板.xlsx"
            # path = "..\Download\个人投资者模板.xlsx"
            # each =os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            each = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(each, 'Download')
            if '个人投资者模板.xlsx' in os.listdir(path):
                result = True
                file = os.path.join(path, os.listdir(path)[-1])
                os.remove(file)
                # os.unlink(file)
            else:
                result = False
            self.assertEqual(result, True)
            time.sleep(1)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_add_representative(self):
        """添加销售代表"""
        try:
            time.sleep(1)
            self.browser.add_representative()
            all_allocated = ("class name", 'gropID0001')
            allocated1 = self.browser.find_elements(all_allocated)[4].text
            allocated2 = self.browser.find_elements(all_allocated)[5].text
            self.assertEqual(allocated1, '已分配')
            self.assertEqual(allocated2, '已分配')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_delete_representative(self):
        """删除销售代表"""
        try:
            time.sleep(1)
            self.browser.delete_representative()
            all_allocated = ("class name", 'gropID0001')
            allocated1 = self.browser.find_elements(all_allocated)[4].text
            allocated2 = self.browser.find_elements(all_allocated)[5].text
            self.assertEqual(allocated1, '未分配')
            self.assertEqual(allocated2, '未分配')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    # def test_derived_data(self):
    #     """导出全部数据"""
    #     try:
    #         time.sleep(1)
    #         self.browser.derive()
    #         # path = "..\..\..\Download\个人投资者.xlsx"
    #         path = "..\Download\个人投资者.xlsx"
    #         self.assertEqual(os.path.exists(path), True)
    #         if os.path.exists(path):
    #             # 删除文件，可使用以下两种方法。
    #             os.remove(path)
    #             # os.unlink(my_file)
    #         else:
    #             print('不存在的文件:%s' % path)
    #     except Exception as msg:
    #         self.log.info(str(msg))
    #         raise

    # def test_inquire_derived_data(self):
    #     """导出查询结果数据"""
    #     try:
    #         time.sleep(1)
    #         self.browser.find_client('查询')
    #         self.browser.click_inquire()
    #         time.sleep(1)
    #         self.browser.derive()
    #         # path = "..\..\..\Download\个人投资者.xlsx"
    #         path = "..\Download\个人投资者.xlsx"
    #         data = ReadExcel(path, 'Sheet1').data_list()
    #         self.assertEqual(len(data), 5)
    #         self.assertEqual(os.path.exists(path), True)
    #         if os.path.exists(path):
    #             # 删除文件，可使用以下两种方法。
    #             os.remove(path)
    #             # os.unlink(my_file)
    #         else:
    #             print('不存在的文件:%s' % path)
    #     except Exception as msg:
    #         self.log.info(str(msg))
    #         raise

    # def test_select_derived_data(self):
    #     """导出选中客户的数据"""
    #     try:
    #         time.sleep(1)
    #         self.browser.find_elements(self.browser.check_box)[4].click()
    #         self.browser.find_elements(self.browser.check_box)[5].click()
    #         self.browser.find_elements(self.browser.check_box)[6].click()
    #         self.browser.derive()
    #         # path = "..\..\..\Download\个人投资者.xlsx"
    #         path = "..\Download\个人投资者.xlsx"
    #         data = ReadExcel(path, 'Sheet1').data_list()
    #         self.assertEqual(len(data), 5)
    #         self.assertEqual(os.path.exists(path), True)
    #         if os.path.exists(path):
    #             # 删除文件，可使用以下两种方法。
    #             os.remove(path)
    #             # os.unlink(my_file)
    #         else:
    #             print('不存在的文件:%s' % path)
    #     except Exception as msg:
    #         self.log.info(str(msg))
    #         raise

    @unittest.skip('pass')
    def test_edit(self):
        """点击操作>编辑按钮，跳转到编辑页面"""
        try:
            time.sleep(1)
            self.browser.click_edit()
            edit_client = self.browser.find_element(('class name', 'statisticsName')).text
            self.assertEqual(edit_client, '编辑客户')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_state_changes(self):
        """点击操作>状态变更-冻结"""
        try:
            time.sleep(1)
            self.browser.click_freeze()
            time.sleep(1)
            state_freeze1 = self.browser.find_elements(('class name', 'laytable-cell-2-customerStatus'))[3].text
            self.assertEqual(state_freeze1, '冻结')
            # 点击操作>状态变更-注销
            self.browser.click_logout()
            time.sleep(1)
            state_freeze2 = self.browser.find_elements(('class name', 'laytable-cell-3-customerStatus'))[3].text
            self.assertEqual(state_freeze2, '注销')
            # 点击操作>状态变更-有效
            self.browser.click_valid()
            time.sleep(1)
            state_freeze3 = self.browser.find_elements(('class name', 'laytable-cell-4-customerStatus'))[3].text
            self.assertEqual(state_freeze3, '有效')
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_investor_transition(self):
        """投资者类型转换：普通投资者->专业投资者"""
        time.sleep(1)
        self.browser.click_invest()
        self.browser.find_elements(('class name', 'layui-form-radio'))[4].click()
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-2-investorType'))[3].text
        self.assertEqual(state_freeze, '专业投资者')
        # 投资者类型转换：专业投资者->普通投资者
        self.browser.scroll_right()
        self.browser.click_invest()
        self.browser.find_elements(('class name', 'layui-form-radio'))[3].click()
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-3-investorType'))[3].text
        self.assertEqual(state_freeze, '普通投资者')

    def test_change_risk(self):
        """更改风险等级-C2"""
        time.sleep(1)
        self.browser.click_risk()
        self.browser.find_elements(self.browser.search)[7].click()
        self.browser.find_element(('css', '#risk-grade-change-pop > form > div:nth-child(3) > div > div > dl > dd:nth-child(3)')).click()
        self.browser.fill_score('25')
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-2-riskLevelCode'))[3].text
        self.assertEqual(state_freeze, 'C2')
        # 更改风险等级-C3
        self.browser.scroll_right()
        self.browser.click_risk()
        self.browser.find_elements(self.browser.search)[7].click()
        self.browser.find_element(
            ('css', '#risk-grade-change-pop > form > div:nth-child(3) > div > div > dl > dd:nth-child(4)')).click()
        self.browser.fill_score('50')
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-3-riskLevelCode'))[3].text
        self.assertEqual(state_freeze, 'C3')
        # 更改风险等级-C4
        self.browser.scroll_right()
        self.browser.click_risk()
        self.browser.find_elements(self.browser.search)[7].click()
        self.browser.find_element(
            ('css', '#risk-grade-change-pop > form > div:nth-child(3) > div > div > dl > dd:nth-child(5)')).click()
        self.browser.fill_score("80")
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-4-riskLevelCode'))[3].text
        self.assertEqual(state_freeze, 'C4')
        # 更改风险等级-C5
        self.browser.scroll_right()
        self.browser.click_risk()
        self.browser.find_elements(self.browser.search)[7].click()
        self.browser.find_element(
            ('css', '#risk-grade-change-pop > form > div:nth-child(3) > div > div > dl > dd:nth-child(6)')).click()
        self.browser.fill_score("100")
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-5-riskLevelCode'))[3].text
        self.assertEqual(state_freeze, 'C5')
        # 更改风险等级-C1
        self.browser.scroll_right()
        self.browser.click_risk()
        self.browser.find_elements(self.browser.search)[7].click()
        self.browser.find_element(
            ('css', '#risk-grade-change-pop > form > div:nth-child(3) > div > div > dl > dd:nth-child(2)')).click()
        self.browser.fill_score("15")
        self.browser.click(self.browser.confirm)
        time.sleep(1)
        state_freeze = self.browser.find_elements(('class name', 'laytable-cell-6-riskLevelCode'))[3].text
        self.assertEqual(state_freeze, 'C1')

    # def test_questionnaire_score(self):
    # 分数验证
    #     self.browser.scroll_right()
    #     self.browser.click_risk()
    #     self.browser.fill_score('1000')
    #     self.browser.click(self.browser.confirm)
    #     time.sleep(1)
    #     print(self.browser.find_element(('class name', 'layui-layer-content')).text)

if __name__ == '__main__':
    unittest.main()

