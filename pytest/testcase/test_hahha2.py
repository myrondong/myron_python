import pytest

# @pytest.fixture(scope="function")
# def my_fixture():
#     print('这个前后置方法，可以实现部分或者全部前后置')
#     yield
#     print('这个确实后置方法')

class TestHaha():
    def test_01_hah(self):
        print('hah 01 al')

    def test_02_hah(self,my_fixture):
        print('haha 02')
