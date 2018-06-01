from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver1 = webdriver.Firefox()
driver.get('http://inv.pb-yun.com')
pc_windows=driver.current_window_handle
driver.maximize_window()
# driver.implicitly_wait(20)
# ActionChains(driver).send_keys(Keys.CONTROL,'t').perform()
driver1.get('http://boss.pb-yun.com/')
manage_window = driver.current_window_handle
sleep(2)
driver.close()
