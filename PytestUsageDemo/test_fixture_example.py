from pytest import fixture
from pytest import mark


@fixture(scope="function")
def connect_db():
    print("I need to connect DB")
    yield
    print(" Yes, its end")


@mark.fixture_example
def test_first(connect_db):
    print("verify agaist ID")


@mark.fixture_example
def test_second(connect_db):
    print("verify against departmemt")


@mark.fixture_example
def test_third(connect_db):
    print("verify against supervisor")


@mark.fixture_example
def test_fourth(connect_db):
    print("I don't need to connect DB")
