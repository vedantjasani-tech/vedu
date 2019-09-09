from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(chrome_options = options)

time.sleep(5)
elem = browser.find_element_by_link_text('Login')
elem.click()
time.sleep(5)
em = browser.find_element_by_id('email')
em.send_keys('hello@atg.world')
time.sleep(2)
pas = browser.find_element_by_id('password')
pas.send_keys('Pass@123')
time.sleep(5)
sin = browser.find_element_by_class_name('btns-loger')
sin.click()
time.sleep(8)
browser.get('http://www.atg.party/article/')
time.sleep(5)
titl = browser.find_element_by_id('title')
titl.send_keys('test by VEDANT JASANI')
time.sleep(2)
desc = browser.find_element_by_class_name('fr-element.fr-view')
desc.send_keys('Description of VEDANT JASANI created by aws!!!')
time.sleep(5)
pos = browser.find_element_by_id('featurebutton')

print("Output sent")
