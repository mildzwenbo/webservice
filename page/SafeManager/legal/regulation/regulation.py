"""
@author:
@date:
@brief: 法律法规页面
"""


from common.manager_login import ManagerLogin, manager_url, browser
from common.get_url import GetUrl

import time

regulation_url = GetUrl().get_admin_url()+'main.html?page=laws/index.html&type=0'


class Regulation(ManagerLogin):

    labels_loc = ('class name', 'nav-name')    #导航栏的class name定位
    regulation_loc = ('link text', '法规库')   #法规库按钮

    def laws_and_regulations_click(self):
        """
        点击导航栏的法律法规,进入到法规库中
        :return:
        """
        self.find_elements(self.labels_loc)[9].click()
        self.click(self.regulation_loc)








if __name__ == '__main__':
    driver = browser()
    r = Regulation(driver)
    r.open_url(manager_url)
    r.manager_login()
    r.laws_and_regulations_click()



