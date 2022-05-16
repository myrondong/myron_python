import os

import pytest

if __name__ == "__main__":
    pytest.main()
    # pytest.main('-vvs', '--alluredir', './report')
    # os.system('allure generate ./report -o ./report --clean')
    # os.system(r"allure generate -c -o allure-report")