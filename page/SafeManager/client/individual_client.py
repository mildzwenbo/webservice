"""
@author:xin
@date:2018-7-3
@brief:管理端-客户管理-个人客户页面所有元素定位
"""
import time

from common.manager_login import ManagerLogin, manager_url, browser
from selenium.webdriver.common.keys import Keys


class IndividualClient(ManagerLogin):
    quit_button = ('id', 'go-out')  # 管理端退出按钮定位
    close_button = ('class name', 'layui-layer-close1')  # 弹框的关闭按钮
    confirm = ('class name', 'layui-layer-btn0')  # 弹框里的确定按钮
    nav_bar = ('class name', 'nav-tit')  # 客户管理导航栏定位
    individual_client = ('link text', '个人客户')  # 二级导航栏个人中心定位
    search = ('class name', 'layui-input')  # 查询字段所有文本框定位
    find_button = ('id', 'btn-search')  # 查询按钮定位
    new_client = ('id', 'btn-addCustomer')  # 新建客户按钮定位
    bulk_import = ('id', 'btn-batchLeadingIn')  # 批量导入按钮定位
    download_temp = ('id', 'btn-download-temp')  # 下载模板按钮定位
    import_file = ('id', 'btn-import')  # 导入文件按钮定位
    sell_button = ('id', 'btn-sellRepresentative')  # 销售代表按钮定位
    add_button = ('id', 'add-sellRepresentative')  # 批量添加销售代表按钮定位
    remove_button = ('id', 'remove-sellRepresentative')  # 批量移除销售代表按钮定位
    derived_data = ('id', 'btn-LeadingOutData')  # 导出数据按钮定位
    check_box = ('class name', 'layui-form-checkbox')  # 页面复选框
    operation = ('class name', 'btn-edit')  # 列表中所有操作按钮定位
    edit = ('id', 'editCustomer')  # 操作>编辑按钮定位
    status = ('id', 'statusChange')  # 操作>状态变更按钮定位
    invest = ('id', 'investTypeChange')  # 操作>投资者类型转换按钮定位
    risk = ('id', 'riskGradeChange')  # 操作>更改风险等级按钮定位
    send = ('id', 'sendRiskEval')  # 操作>发送调查问卷按钮定位
    send_return = ('id', 'sendReturn')  # 操作>适当性回访按钮定位
    document_manage = ('id', 'documentManage')  # 操作>文档管理按钮定位


    def click_client(self):
        """进入客户管理-个人客户页面"""
        self.find_elements(self.nav_bar)[6].click()
        time.sleep(1)
        self.click(self.individual_client)

    def find_client(self, name):
        """查询：客户名称输入内容"""
        self.find_elements(self.search)[0].send_keys(name)

    def find_sell(self, sell):
        """查询：销售代表输入内容"""
        self.find_elements(self.search)[3].send_keys(sell)

    def find_investor(self):
        """查询：投资者类型为：普通投资者"""
        self.find_elements(self.search)[1].click()
        self.click(('xpath', '//*[@id="search-box"]/div[2]/div/div/dl/dd[2]'))

    def find_profession(self):
        """查询：投资者类型为：专业投资者"""
        self.find_elements(self.search)[1].click()
        self.click(('xpath', '//*[@id="search-box"]/div[2]/div/div/dl/dd[3]'))

    def find_c1(self):
        """查询：风险等级偏好-C1"""
        self.find_elements(self.search)[2].click()
        self.click(('css', '#search-box > div:nth-child(3) > div > div > dl > dd:nth-child(2)'))

    def find_c2(self):
        """查询：风险等级偏好-C2"""
        self.find_elements(self.search)[2].click()
        self.click(('css', '#search-box > div:nth-child(3) > div > div > dl > dd:nth-child(3)'))

    def find_c3(self):
        """查询：风险等级偏好-C3"""
        self.find_elements(self.search)[2].click()
        self.click(('css', '#search-box > div:nth-child(3) > div > div > dl > dd:nth-child(4)'))

    def find_c4(self):
        """查询：风险等级偏好-C4"""
        self.find_elements(self.search)[2].click()
        self.click(('css', '#search-box > div:nth-child(3) > div > div > dl > dd:nth-child(5)'))

    def find_c5(self):
        """查询：风险等级偏好-C5"""
        self.find_elements(self.search)[2].click()
        self.click(('css', '#search-box > div:nth-child(3) > div > div > dl > dd:nth-child(6)'))

    def click_inquire(self):
        """点击查询按钮"""
        self.click(self.find_button)

    def click_new(self):
        """点击新建按钮"""
        self.click(self.new_client)

    def click_template(self):
        """点击批量导入下的下载模板"""
        self.click(self.bulk_import)
        self.click(('id', 'btn-download-temp'))

    # 点击批量导入的导入文件-待研究

    def add_representative(self):
        """批量添加销售代表"""
        self.find_elements(self.check_box)[5].click()
        self.find_elements(self.check_box)[6].click()
        self.click(self.sell_button)
        self.click(('id', 'add-sellRepresentative'))
        self.find_elements(self.check_box)[11].click()
        self.click(self.confirm)

    def delete_representative(self):
        """批量删除销售代表"""
        self.find_elements(self.check_box)[5].click()
        self.find_elements(self.check_box)[6].click()
        self.click(self.sell_button)
        self.click(('id', 'remove-sellRepresentative'))
        self.find_elements(self.check_box)[11].click()
        self.click(('class name', 'layui-layer-btn0'))

    def scroll_right(self):
        """页面内部滚动条向右滚动"""
        js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
        self.js_execute(js)

    def click_edit(self):
        """点击列表中操作>编辑按钮按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.edit)

    def click_freeze(self):
        """点击列表中操作>状态变更-冻结,修改账号状态"""
        self.scroll_right()
        self.find_elements(self.operation)[2].click()
        self.click(self.status)
        self.find_elements(('class name', 'layui-anim'))[3].click()
        self.click(self.confirm)

    def click_logout(self):
        """点击列表中操作>状态变更-注销,修改账号状态"""
        self.scroll_right()
        self.find_elements(self.operation)[2].click()
        self.click(self.status)
        self.find_elements(('class name', 'layui-anim'))[4].click()
        self.click(self.confirm)

    def click_valid(self):
        """点击列表中操作>状态变更-有效,修改账号状态"""
        self.scroll_right()
        self.find_elements(self.operation)[2].click()
        self.click(self.status)
        self.find_elements(('class name', 'layui-anim'))[2].click()
        self.click(self.confirm)

    def click_invest(self):
        """点击列表中操作>投资者类型转换按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.invest)

    def click_risk(self):
        """点击列表中操作>更改风险等级按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.risk)

    def click_send(self):
        """点击列表中操作>发送调查问卷按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.send)

    def click_send_return(self):
        """点击列表中操作>适当性回访按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.send_return)

    def click_document_manage(self):
        """点击列表中操作>文档管理按钮"""
        self.scroll_right()
        # time.sleep(1)
        self.find_elements(self.operation)[2].click()
        self.click(self.document_manage)

    def fill_score(self, number):
        """填写分数"""
        score = self.find_elements(self.search)[8]
        score.click()
        score.send_keys(Keys.CONTROL, 'a')
        score.send_keys(number)

    def derive(self):
        """导出数据"""
        self.click(self.derived_data)


if __name__ == '__main__':
    driver = browser()
    c = IndividualClient(driver)
    c.open_url(manager_url)
    c.lx_manager_login()
    c.click_client()
    time.sleep(1)
