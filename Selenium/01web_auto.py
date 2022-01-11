import sys

from selenium import webdriver
from selenium.webdriver.common.by import By



# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Edge('msedgedriver.exe')
# 加一个timeout机制 目的每次寻找元素时候 每半秒搜索一次 持续等待 10s

wd.implicitly_wait(10)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('白月黑羽\n')
# 通过 find_element 去寻找元素

send_inf0 = web_egde.find_elements(By.TAG_NAME, "span")
for i in send_inf0:
    print(i.text)
pass

