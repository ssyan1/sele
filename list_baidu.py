#-*- coding:UTF-8 -*-
from selenium import  webdriver
import  time
search_text=['python',u'中文', 'text']
for text in search_text:
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    time.sleep(1)
    driver.quit()
