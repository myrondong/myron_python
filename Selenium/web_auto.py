from selenium import webdriver
from selenium.webdriver.common.by import By

web_egde = webdriver.Edge('msedgedriver.exe')

# 鼠标点击
web_egde.get("https://www.baidu.com")
keys = web_egde.find_element(By.LINK_TEXT, "点击一下，了解更多")
webdriver.ActionChains(web_egde).click(keys).perform()
print(keys)

"""
# 元素选择
print(web_egde)
web_egde.get("https://www.baidu.com")
# sned_inf0 =web_egde.find_element_by_id("kw")
sned_inf0 = web_egde.find_elements(By.TAG_NAME, "span")
for i in sned_inf0:
    print(i.text)
pass
"""
