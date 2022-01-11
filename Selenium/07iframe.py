from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge('msedgedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')


# 先根据name属性值 'innerFrame'，切换到iframe中
wd.switch_to.frame('innerFrame')

# 根据 class name 选择元素，返回的是 一个列表
elements = wd.find_elements(By.CLASS_NAME, 'plant')

for element in elements:
    print(element.text)

# 切换回 最外部的 HTML 中
wd.switch_to.default_content()

# 然后再 选择操作 外部的 HTML 中 的元素
wd.find_element_by_id('outerbutton').click()

wd.quit()