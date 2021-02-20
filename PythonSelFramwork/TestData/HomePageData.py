import openpyxl
import public as public


class HomePageDy:
    home_Page_Data = [{"FirstName": "Neeraj", "LastName": "Kumar", "Gender": "Male"}, {"FirstName": "Priya", "LastName": "Kumari", "Gender": "Female"}]

    @staticmethod
    def getTestData(test_case_name):
        dict = {}
        book = openpyxl.load_workbook("E:\\SourceSoft\\Demo.xlsx")
        sheet = book.active

        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):
                    dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

        return[dict]

































