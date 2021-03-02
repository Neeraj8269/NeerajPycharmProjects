import pytest


class TestData:
    submission_data = [{"Firstname": "Neeraj","Lastname": "Kumar", "Gender": "Male"}, {"Firstname": "Abhishek", "Lastname": "Sharma","Gender": "Male"}]

    @pytest.fixture(params=submission_data)
    def get_data_new(self, request):
        return request.param

