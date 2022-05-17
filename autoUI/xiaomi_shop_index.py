import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestMiShop():

    def setup_class(self):
        self.driver = webdriver.Edge(r'F:\git_reposittory\myron_python\autoUI\msedgedriver.exe')
        self.driver.implicitly_wait(6)

    def test_open_index(self):
        self.driver.get('https://www.mi.com/')

    # 鼠标悬停
    def test_mouse_huang(self):
        self.ac = ActionChains(self.driver)
        xiaomi_menu = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]/a/span')
        self.ac.move_to_element(xiaomi_menu).perform()


    def teardown_class(self):
        # self.driver.close()
        pass

if __name__ == '__main__':
    pytest.main()