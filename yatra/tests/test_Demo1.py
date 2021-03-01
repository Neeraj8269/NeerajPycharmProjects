import pytest


@pytest.fixture(params=[("Neeraj", "Kumar", "Male"), ("Abhishek", "Sharma", "Male")])
def get_data_new(self, request):
    return request.param


