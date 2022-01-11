from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Edge('msedgedriver.exe')
wd.implicitly_wait(3)
# 调用WebDriver 对象的get方法

wd.get('http://cdn1.python3.vip/files/selenium/sample1a.html')
elements = wd.find_elements(By.CSS_SELECTOR, 'div,#BYHY')
for element in elements:
    print(element.text)
wd.quit()