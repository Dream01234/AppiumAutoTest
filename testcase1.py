import pytest
import login_operation
import workbench_operation
import module_operation

class TestClass:

    "登录且切换到目标项目"
    def test_one(self):
        a = login_operation.loginpage_control()
        a.logincloud1("kentestgrp10","12345678")
        b = workbench_operation.workbench_control()
        b.changeorganization()

    "选择更多"
    def test_two(self):
        b = workbench_operation.workbench_control()
        b.click_more()

    "选择目标模块"
    def test_three(self):
        b = workbench_operation.workbench_control()
        b.findmodule("实测实量")

    "选择目标任务同步"
    def test_four(self):
        a = module_operation.task_control()
        a.selectall()
        a.selecttask("爆点清单")



if __name__ == '__main__':
        pytest.main(['testcase1.py',])