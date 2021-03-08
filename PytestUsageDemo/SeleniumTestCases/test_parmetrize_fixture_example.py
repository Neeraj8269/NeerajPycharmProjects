from pytest import mark, fixture


@fixture(params=["apple", "guava", "orange"])
def fruit():
    return request


@mark.parametrize_fixture
def test_fruit(fruit):
    print(f"i am a fruit named {fruit}")





