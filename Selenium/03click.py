from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge('msedgedriver.exe')
wd.implicitly_wait(2)

wd.get('https://www.baidu.com/')

# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, ".s-hotsearch-title>.hot-title")


print(link.text)
link.click()
wd.quit()

# wd.title属性是当前窗口的标题栏 文本
#print(wd.title)
