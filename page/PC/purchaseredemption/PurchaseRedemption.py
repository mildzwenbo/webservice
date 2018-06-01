from common.PC_login import PCLogin, browser, pc_url
from common.get_url import GetUrl
import time

pc_url = GetUrl().get_pc_url()


class PurchaseRedemption(PCLogin):
    '''申赎记录列表页面'''
    '''菜单申赎记录'''
    menu_loc = ('xpath','//*[@id="app"]/div/div[1]/ul/div/a[5]/li')#申赎记录菜单
    '''列表页面'''
    apply_time_loc = ('xpath','//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div')#列表页面申请时间字段
    status_loc = ('xpath','//*[@id="pane-0"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div')#列表状态字段

    def menu(self):
        '''点击申赎记录菜单'''
        self.click(self.menu_loc)

    def apply_time(self):
        '''获取列表时间信息'''
        text = self.find_element(self.apply_time_loc).text
        return text[:13]

    def current_time(self):
        '''获取当前时间'''
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))[:13]
        return time1

    def status(self):
        '''获取列表状态信息'''
        text = self.find_element(self.status_loc).text
        return text

    def time_status(self):
        submit = []
        time = self.apply_time()
        submit.append(time)
        statu = self.status()
        submit.append(statu)
        return submit
    def current_time_status(self):
        submit1 = []
        time1 = self.current_time()
        submit1.append(time1)
        statu2 = '未审核'
        submit1.append(statu2)
        return submit1



if __name__ == "__main__":
    driver = browser()
    po = PurchaseRedemption(driver)
    po.open_url(pc_url)
    po.pc_login('13511055879','jzj198304','1')
    po.menu()
    submit2 = po.current_time_status()
    print(submit2)
    submit = po.time_status()
    print(submit)
