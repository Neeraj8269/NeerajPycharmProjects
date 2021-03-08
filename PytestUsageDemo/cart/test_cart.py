from pytest import mark

def test_cart_first():
    assert [1,2, 3] == [1,2,3]


@mark.smoke
def test_cart_second():
    assert "i am" == "I am a QA"


def test_cart_third():
    assert "This is" == "This test will be failed"