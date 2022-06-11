import os

from selenium import webdriver
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

test_list=['Xiaomi 12 8GB+128GB', '小米数字系列屏幕换新服务 小米8 屏幕换新服务', 'Xiaomi 12 Pro 12GB+256GB', 'Xiaomi 12X 8GB+128GB', 'Xiaomi 12 保护壳', 'Xiaomi 12X 硅胶保护壳 绿色']
class TestSearchXiaoMI():
    @pytest.mark.smoke
    def test_serach_item(self):
        print("smoke")
    @pytest.fixture(scope='module',autouse=True)
    def test_before(self):
        # self.driver = webdriver.Edge(r'D:\GitData\myron_python\autoUI\msedgedriver.exe')
        self.driver = webdriver.Edge(r'F:\git_reposittory\myron_python\autoUI\msedgedriver.exe')
        self.driver.implicitly_wait(6)
        self.driver.get('https://www.mi.com/')
        yield
        print('执行web 清除')
        self.test_before()

    @pytest.mark.parametrize('args',test_list)
    def test_search_info(self,args):
        self.driver.find_element(By.CSS_SELECTOR, '#J_searchForm   #search').send_keys(f"{args}\n")
        #self.driver.find_element(By.CSS_SELECTOR, '#J_searchForm   .search-btn').click()
        a = self.driver.find_elements_by_css_selector('.goods-list  .title')
        data=[i.text for i in a]
        assert args in data

    def test_after(self):
        name_prompt = Alert(self.driver)
        name_prompt.send_keys("Willian Shakephere")
        name_prompt.accept()
        # self.driver.quit()

if __name__ == '__main__':
    pytest.main([
        '--alluredir=tmp/my_allure_results'
    ])
    os.system('allure serve tmp/my_allure_results')