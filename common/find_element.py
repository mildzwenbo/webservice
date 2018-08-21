# coding=utf-8
"""
author:
time:
brief:
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as   EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import platform
import os

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
download_path = os.path.join(path, 'Download')
if os.path.isdir(download_path):
    pass
else:
    os.makedirs(download_path)

# import time


def browser(browser='firefox', name='application/vnd.ms-excel'):
    """
    打开浏览器
    :param browser:
    :return:
    """
    try:
        if browser == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.download.folderList", 2)
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            fp.set_preference("browser.download.dir", download_path)
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk", name)
            driver = webdriver.Firefox(firefox_profile=fp)
            # file_path = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\2mnajvb0.default'
            # f = webdriver.FirefoxProfile(file_path)
            # driver = webdriver.Firefox(f)
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == "ie":
            driver = webdriver.Ie()
        elif browser == 'phantomjs':
            driver = webdriver.PhantomJS(r'F:\F_lianxi\Scripts\phantomjs.exe')
        else:
            print("No found this browser , You can enter 'firefox, chrome, ie, phantomjs'")
        return driver
    except Exception as msg:
        print("The browser failed to launch the cause of success: %s" % msg)


class FindElement():
    """
    基于selenium框架的二次封装
    """
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url, t='', timeout=10):
        """
        打开url
        :param url:
        :param t:
        :param timeout:
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutError:
            print("open %s url is error" % url)
        except Exception as msg:
            print("Error: %s" % msg)

    def find_element(self, locator, timeout=10):
        """
        查看元素
        :param locator:
        :param timeout:
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout, 1).until(lambda x: x.find_element(*locator))
        except TimeoutException:
            print('未找到元素：%s' % str(locator))
            return False
        else:
            return element

    def find_elements(self, locator, timeout=10):
        """
        查找一组元素
        :param locator:
        :param timeout:
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout, 1).until(lambda x: x.find_elements(*locator))
        except TimeoutException:
            print('未找到元素组：%s' % str(locator))
        else:
            return elements

    def click(self, locator):
        """
        点击元素
        :param locator:
        :return:
        """
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """
        输入
        :param locator:
        :param text:
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否和显示的
        text值相等，定位到返回True，没有返回False
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print("没有找到元素 %s" % str(locator))
            return False
        else:
            return result

    def is_text_in_element_value(self, locator, text, timeout=10):
        """
        判断文本是否为元素的value的值，定位到返回True，没有返回False
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until\
                (EC.text_to_be_present_in_element_value(locator, text))
        except TimeoutException:
            print("没有找到元素 %s" % str(locator))
            return False
        else:
            return result

    def is_title(self, text, timeout=10):
        """
        判断title完全等于
        :param text:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(text))
        except TimeoutException:
            print("title不等于 %s" % text)
            return False
        else:
            return result

    def is_title_contains(self, text, timeout=10):
        """
        判断title包含text
        :param text:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(text))
        except TimeoutException:
            print("title不包含 %s" % text)
            return False
        else:
            return result

    def is_selected(self, locator, timeout=10):
        """
        判断元素是否被选中，选中返回True， 未选中返回False
        :param locator:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        except TimeoutException:
            print("未选中元素：%s" % str(locator))
            return False
        else:
            return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        """
        判断元素的选中状态是否符合预期，符合返回True，不符合返回False
        :param locator:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(locator, selected))
        except TimeoutException:
            print('元素%s的选中状态和预期的不符' % str(locator))
            return False
        else:
            return result

    def is_alert_present(self, timeout=10):
        """
        判断页面是否有alert
        :return:有alert返回True，没有返回False
        """
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        except TimeoutException:
            print("没有弹窗")
            return False
        else:
            return True

    def is_visibility(self, locator, timeout=10):
        """
        元素可见返回本身，否则返回False
        :param locator:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("元素%s不可见" % str(locator))
            return False
        else:
            return result

    def is_clickable(self, locator, timeout=10):
        """
        元素可以点击返回元素本身，不可点击返回False
        :param locator:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print("元素%s, 没有找到或者不可点击" % str(locator))
            return False
        else:
            return result

    def is_located(self, locator, timeout=10):
        """
        元素是否被定为到(并不一定可见)
        :param locator:
        :param timeout:
        :return:被定位到返回element  没有被定位到返回False
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("元素%s没有被定位到" % str(locator))
            return False
        else:
            return result

    def move_to_element(self, locator):
        """
        鼠标悬停
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        返回到上一页面
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        进入到下一个页面
        :return:
        """
        self.driver.forward()

    def get_title(self):
        """
        获取title
        :return:
        """
        return self.driver.title

    def get_text(self, locator):
        """
        获取文本信息
        :return:
        """
        element = self.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        """
        获取对应属性的值
        :return:
        """
        element = self.find_element(locator)
        return self.driver.get_attribute(element, name)

    def js_execute(self, js):
        """
        执行js
        :param js:
        :return:
        """
        return self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        """
        选择通过索引， 从0开始
        :param locator:
        :param index:
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """
        选择通过value值
        :param locator:
        :param value:
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """
        选择通过文本
        :param locator:
        :param text:
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)

    def js_focus_element(self, locator):
        """
        聚焦元素
        :param locator:
        :return:
        """
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """
        滚动到顶部
        :return:
        """
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, num1, num2):
        """
        滚动到底部
        :return:
        """
        js = "window.scrollTo(%d,%d)" % (int(num1), int(num2))
        self.driver.execute_script(js)

    def delete_all_cookies(self):
        """
        刪除所有cookies
        :return:
        """
        self.driver.delete_all_cookies()

    def refresh(self):
        """
        刷新浏览器
        :return:
        """
        self.driver.refresh()

    def close(self):
        """
        关闭一个窗口
        :return:
        """
        self.driver.close()

    def add_cookie(self, cookie):
        """
        添加cookie
        :param cookie:
        :return:
        """
        self.driver.add_cookie(cookie)

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()

    def get_shot(self, img):
        """
        获取图片
        :return:
        """
        self.driver.get_screenshot_as_file(img)

