from page.SafeManager.ManageLogin import ManageLoginPage,ManageLoginUrl,browser
import time


class Appointment(ManageLoginPage):
    '''销售管理-预约申请列表页面'''
    '''菜单'''
    menu_sales_loc = ('xpath','/html/body/div[1]/div[2]/div[1]/ul/li[7]/div/span')#菜单销售管理
    menu_appointment_loc = ('xpath','/html/body/div[1]/div[2]/div[1]/ul/li[7]/ul/li[4]/a')#菜单预约申请
    '''列表'''
    apply_time_loc = ('xpath','//*[@id="main-right"]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[5]/div')#申请时间
    status_loc = ('xpath','//*[@id="main-right"]/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/div')#状态
    '''点击菜单'''
    def sales(self):
        '''点击销售管理菜单'''
        self.click(self.menu_sales_loc)

    def appointment(self):
        '''点击预约申请菜单'''
        self.click(self.menu_appointment_loc)

    def click_menu(self):
        '''点击销售管理-预约申请菜单'''
        self.sales()
        self.appointment()

        '''获取时间及状态'''
    def apply_time(self):
        '''申请时间'''
        text = self.find_element(self.apply_time_loc).text
        return text

    def current_time(self):
        '''获取当前时间'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[:10]
        return time1

    def status(self):
        '''状态'''
        test =self.find_element(self.status_loc).text
        return test
    def time_status(self):
        timestatus = []
        time = self.apply_time()
        timestatus.append(time)
        sta = self.status()
        timestatus.append(sta)
        return timestatus
    '''滚动条'''
    def scroll(self):
        self.js_scroll_end(0,800)

    def current_time_status(self):
        current = []
        time1 = self.current_time()
        current.append(time1)
        sta = "未审核"
        current.append(sta)
        return current

if __name__ == "__main__":
    driver = browser()
    po = Appointment(driver)
    po.open_url(ManageLoginUrl)
    po.ManageLogin('13511055879','123456','')
    po.sales()
    po.appointment()
    po.scroll()


    js = "document.getElementsByClassName('layui-table-body')[0].scrollLeft=10000"
    driver.execute_script(js)



    # text = po.time_status()
    # print(text)
    # text1 = po.current_time_status()
    # print(text1)


