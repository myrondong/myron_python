import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPythonOrgSearch():

    def setup(self):
        self.driver = webdriver.Edge('../msedgedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        print(driver.title)
        # self.assertIn("Python", driver.title)
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_baidu_com(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        print(driver.title)
        # self.assertIn("Python", driver.title)
        assert "百度" in driver.title
        elem = driver.find_element_by_name("wd")
        elem.send_keys("神秘复苏")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def teardown(self):
        self.driver.close()
        # pass
        pass


if __name__ == "__main__":

    pytest.main('-vvs', '--alluredir', './report')
    os.system('allure generate ./report -o ./report --clean')
    # os.system(r"allure generate -c -o allure-report")