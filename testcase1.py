import pytest
import login_operation
import workbench_operation

class TestClass:

    def test_one(self):
        a = login_operation.loginpage_control()
        a.logincloud1("kentestgrp10","12345678")
        b = workbench_operation.workbench_control()
        b.changeorganization()

if __name__ == '__main__':
        pytest.main(['testcase1.py',])