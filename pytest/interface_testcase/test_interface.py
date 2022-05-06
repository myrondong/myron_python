import pytest


def test_interface_02():
    print('Interface FUCtion')

class TestInterface:
    @pytest.mark.smoke
    def test_interface_01(self):
        print('Interface')


