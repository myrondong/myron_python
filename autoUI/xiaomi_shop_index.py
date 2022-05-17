import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestMiShop():

    def setup_class(self):
        self.driver = webdriver.Edge(r'D:\GitData\myron_python\autoUI\msedgedriver.exe')
        self.driver.implicitly_wait(6)

    def test_open_index(self):
        self.driver.get('https://www.mi.com/')

    # 鼠标悬停
    def test_mouse_huang(self):
        self.ac = ActionChains(self.driver)
        xiaomi_menu = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]/a/span')
        self.ac.move_to_element(xiaomi_menu).perform()

    def test_get_product_information(self):
        # self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[3]/div[2]/div/ul/li[1]/a/div[2]").click()
        product_list = self.driver.find_elements(By.CSS_SELECTOR,'#J_navMenu .title')
        for son_list in product_list:
            son_list.click()
    def teardown_class(self):
        # self.driver.close()
        pass

if __name__ == '__main__':
    pytest.main()