from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Edge('msedgedriver.exe')
wd.implicitly_wait(3)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com/')
# 根据属性选择元素
element = wd.find_element(By.CSS_SELECTOR, '#bottom_layer .text-color')
html_address = element.get_attribute('href')
print(html_address)
# 打印出元素对应的html
print(element.get_attribute('outerHTML'))
a = requests.post(html_address).text
print(a)