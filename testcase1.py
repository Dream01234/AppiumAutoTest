import pytest
import login_operation
import workbench_operation
import module_operation
import logger

log = logger.Log()

class TestClass:


    "登录且切换到目标项目"
    def test_one(self):
        log.info("-----------用例开始---------")
        a = login_operation.loginpage_control()
        a.logincloud1("kentestgrp10","12345678")
        log.info("--------输入账号密码，点击登录---------")
        b = workbench_operation.workbench_control()
        # b.noupdate()
        log.info("------切换组织-----------")
        b.changeorganization()

        log.info("------登录且切换到目标项目 用例已完成----")

    "选择更多"
    def test_two(self):
        b = workbench_operation.workbench_control()
        b.click_more()
        log.info("------点击更多----")

    "选择目标模块"
    def test_three(self):
        b = workbench_operation.workbench_control()
        b.findmodule("实测实量")
        log.info("------选择实测实量----")

    "选择目标任务同步"
    def test_four(self):
        a = module_operation.task_control()
        # a.Synchronization_task("爆点清单")
        a.selectall()
        a.selecttask("爆点清单")
        log.info("-----同步完成后，选择爆点清单----")


if __name__ == '__main__':
        pytest.main(['testcase1.py',])