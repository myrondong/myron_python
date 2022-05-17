import os

import pytest

if __name__ == "__main__":

    pytest.main(['-vs', '--alluredir', './report'])
    os.system('allure generate ./report -o ./temp --clean')
    # os.system(r"allure generate -c -o allure-report")