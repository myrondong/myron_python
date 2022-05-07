import pytest
import time

@pytest.fixture(scope="function")
def my_fixture():
    print('这个前后置方法，可以实现部分或者全部前后置')


class TestMaShang():
    # 这个所有用例之前只执行一次
    def setup_class(self):
        print('在每个类执行初始化工作比如创建日志，创建数据的连接，创建接口对象')

    # 每个用例之前执行一次
    def setup(self):
        print('在执行测试用例之前测试初始化的代码,打开浏览器，加载网页')

    def test_01_al(self):
        print('01 al')

    def test_02_al(self):
        print('02 al')

    def teardown(self):
        print('在执行测试用例之后测试扫尾的代码,关闭浏览器')

    def teardown_class(self):
        print('在每个类执行扫尾工作比如销毁日志对象，断开数据的连接，销毁接口对象')
