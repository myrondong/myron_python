import time
import pytest


class TestLogin:
    age = 19

    def test_01(self):
        time.sleep(2)
        print('test 01')

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @pytest.mark.skip(reason="不喜欢")
    def test_02_ao(self):
        time.sleep(2)
        assert 1 == 1
        print('test 02')

    def test_03_ao(self):
        time.sleep(2)
        print('test 03')


    @pytest.mark.run(order=2)
    @pytest.mark.skipif(age >= 19,reason='成年了')
    def test_04(self):
        time.sleep(2)
        print('test 04')
