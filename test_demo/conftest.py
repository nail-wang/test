import pytest
from test_demo.cal import Calculator

@pytest.fixture()
def basic():
        print("开始计算")
        cal = Calculator()
        yield cal
        print("计算结束")
