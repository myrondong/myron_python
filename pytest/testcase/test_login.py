import time
import pytest


class TestLogin:
    def test_01(self):
        time.sleep(2)
        print('test 01')
    @pytest.mark.run(order=1)
    def test_02_ao(self):
        time.sleep(2)
        assert 1==2
        print('test 02')

    def test_03_ao(self):
        time.sleep(2)
        print('test 03')


    def test_04(self):
        time.sleep(2)
        print('test 04')
