import pytest
from pytest_ordering import orderable


def test1():
    print("First test case")


@pytest.yield_fixture
def setup1():
    print("It's a fixture")
    yield
    print("It's yield")

def test3(setup1):
    print("3rd test case")

@pytest.mark.skip
def test2():
    print("2nd test case")




