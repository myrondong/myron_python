

import pytest
import os

if __name__ == '__main__':
    pytest.main(['-s', '-vv', '--alluredir', './report/xml'])
    # os.system('allure generate ./temp -o ./report --clean')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
