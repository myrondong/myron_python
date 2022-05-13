import os
import requests
import pytest

from testdemo.yaml_util import YamlUtil


class TestApi():

    # @pytest.mark.parametrize('args',['小王','小刘','小李'])
    @pytest.mark.parametrize('args', ['小王', '小刘', '小李'])
    def test_01_alang(self, args):
        print(args)

    @pytest.mark.parametrize('name,age', [['小王', 35], ['小刘', 56], ['小李', 56]])
    def test_02_alang(self, name, age):
        print(name, age)

    @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+'/testdemo/test_api.yaml').read_yaml())
    def test_api_ali(self,args):
        url =args['request']['url']
        params=args['request']['params']
        res = requests.get(url,params=params).text
        print(res)
        print(args)
        print('args')

        # 断言

if __name__ == '__main__':
    pytest.main()
    # os.system('allure generate ./temp -o ./report --clean')
    os.system(r"allure generate -c -o allure-report")
