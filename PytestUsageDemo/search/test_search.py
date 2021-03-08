from pytest import mark
flag=0

def test_search_getstarted():
    assert [1,2] == [1,2,3]


def test_search_yatra():
    assert "i am a QA" == "I am a QA"
    global flag
    flag = 1


@mark.skipif(flag=1)
def test_search_Demo():
    assert "This is" == "This test will be failed"

