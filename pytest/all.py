import os

import pytest
if __name__ == '__main__':
    # pytest.main(['-vs','./testcase/test_login.py','--reruns=2','-n=3','--maxfail=2','-k=ao'])
    pytest.main()
    os.system('allure generate ./testdemo/report -o ./report --clean')