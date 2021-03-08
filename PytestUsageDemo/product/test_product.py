from pytest import mark


@mark.product
class Product_test:
    @mark.smoke

    def test_product_first(self):
        assert [1, 2] == [1, 2, 3]

    def test_product_second(self):
        assert "i am a QA" == "I am a QA"


    def test_product_third(self):
        assert "This is" == "This test will be failed"



