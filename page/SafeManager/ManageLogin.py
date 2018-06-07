from common.find_element import FindElement,browser
from common.get_url import GetUrl
from time import sleep

ManageLoginUrl = GetUrl.admin_url

class ManageLoginPage(FindElement):
    """管理端登录页面的元素定位及方法"""
    username_loc = ('id','login-name')           #用户名称定位
    passwd_loc = ('id','login-password')         #密码定位
    verification_loc = ('xpath','//*[@id="verifyCode"]')        #验证码定位
    submit_loc = ('xpath','//*[@id="login-btn"]')             #登录按钮定位
    alarm1_loc = ('class name','layui-layer')
    alarm2_loc = ('class name','layui-layer-dialog')
    alarm3_loc = ('class name','layui-layer-broder')
    alarm4_loc = ('class name','layui-layer-msg')
    longin_username_loc = ('xpath','//*[@id="username"]')

    def username(self,username):
        '''用户名字段输入用户名'''
        self.send_keys(self.username_loc,username)

    def passwd(self,passwd):
        '''密码字段输入密码'''
        self.send_keys(self.passwd_loc,passwd)

    def verifi(self,verifi):
        '''验证码字段输入验证码'''
        self.send_keys(self.verification_loc,verifi)

    def sbm(self):
        '''点击登录按钮'''
        self.click(self.submit_loc)

    def type_alarm1(self):
        '''用户不存在'''
        text = self.find_element(self.alarm1_loc).text
        return text
    def type_alarm2(self):
        ''''''
        text = self.find_element(self.alarm2_loc).text
        return text
    def type_alarm3(self):
        text = self.find_element(self.alarm3_loc).text
        return text
    def type_alarm4(self):
        '''账号被锁定'''
        text = self.find_element(self.alarm4_loc).text
        return text
    def type_username(self):
        text = self.find_element(self.longin_username_loc).text
        return text

    def ManageLogin(self,usernam,passwd,verifi):
        self.username(usernam)
        sleep(1)
        self.passwd(passwd)
        sleep(1)
        self.verifi(verifi)
        sleep(1)
        self.sbm()
        sleep(4)

if __name__ == '__main__':
    driver = browser()
    po = ManageLoginPage(driver)
    po.open_url(ManageLoginUrl)
    # po.username('13688888888')
    # po.passwd('123456')
    po.sbm()
    # text = po.type_username()
    # print(text)
    text1 = po.type_alarm1()
    print(text1)
    text2 = po.type_alarm2()
    print(text2)
    # text3 = po.type_alarm3()
    # print(text3)
    # text4 = po.type_alarm4()
    # print(text4)






