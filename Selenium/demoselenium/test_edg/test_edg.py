import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestPythonOrgSearch():

    def setup_class(self):
        self.driver = webdriver.Edge('F:\git_reposittory\myron_python\Selenium\demoselenium/msedgedriver.exe')
        self.driver.implicitly_wait(3)
    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     print(driver.title)
        # # self.assertIn("Python", driver.title)
        # assert "Python" in driver.title
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    def test_search_in_baidu_com(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        #driver.get("https://www.baidu.com/s?ie=UTF-8&wd=selenium%20%E5%AE%9A%E4%BD%8D%E7%94%A8%E5%93%AA%E4%B8%AA%E5%A5%BD")
        print(driver.title)
        # assert "百度" in driver.title
        # /html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li[6]/a/span[2]
        #elem = driver.find_element_by_name("wd")
        elem = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/ul/li[6]/a[1]').click()

        print(elem.get_attribute('class'))
        print(elem.text)
        # elem.click()

        #print(driver.page_source)/html/body/div/div/div/div/a[1]
        #print(elem.get_attribute('href'))
        # elem.send_keys("神秘复苏")
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source

    def teardown_class(self):
        # self.driver.close()
        pass


if __name__ == "__main__":

    pytest.main(['-vs'])
    #os.system('allure generate ./report -o ./temp --clean')
    # os.system(r"allure generate -c -o allure-report")