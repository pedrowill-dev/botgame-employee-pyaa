from selenium.webdriver.common.by import By

class EmployeeDataMigration:

    def __init__(self, browser):
        self.browser = browser

    def get_employee_id(self):
        id_emp = self.browser.find_element(By.ID, 'employeeID')
        id_emp = id_emp.get_property('value')
        return id_emp

    def send_data_employe_input(self, data: dict):
        for key_id, value in data.items():
            id_emp = self.browser.find_element(By.ID, key_id)
            id_emp.send_keys(value)

        submit = self.browser.find_element(By.ID, 'submitButton')
        submit.click()

    