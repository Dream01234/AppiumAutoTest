import allure
import allure_commons
import pytest
import os
class TestCase:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 1 == 6


if __name__ == '__main__':
    pytest.main(['test_demo.py', "--alluredir=report/alluer_raw"])
    os.system("allure generate C:/Users/41708/PycharmProjects/pythonProject/report/alluer_raw -o C:/Users/41708/PycharmProjects/pythonProject/report/allure_report --clean")

