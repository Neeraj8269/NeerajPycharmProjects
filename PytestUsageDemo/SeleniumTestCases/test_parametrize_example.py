from pytest import mark
@mark.param_testcase
@mark.parametrize("product_name, product_color", [("silk", "orange"), ("Cap", "yellow"), ("tshirt", "blue") ])
def test_product_detail(product_name, product_color):
    print(f"i am product {product_name} with {product_color}")







# @mark.parametrize("number", [1, 0, 100, -4])
# def test_first(number):
#     assert number > 0

