from pywinauto import *

class EmployeeDatabase():

    def __init__(self):
        self.app = Application()
        self.employee = self.app.start(r'EmployeeList.exe')
        self.set_window = self.employee['Employee Database']
    

    def search_employee(self, id_emp):
        emp_number = self.set_window['Enter the Emp numberEdit']
        emp_number.set_text(id_emp)
        self.set_window['Search'].click()
        self.set_window['Search'].type_keys('{ENTER}')

    def get_fields_values(self):
        fields_db = [
            'First Name',
            'Last Name',
            'Email Id',
            'City',
            'Zip Code',
            'State',
            'Manager',
            'Department',
            'Search'
        ]
        fields_id = [
            'firstName',
            'lastName',
            'email',
            'city',
            'zip',
            'state',
            'manager',
            'department',
            'title',

        ]
        
        values_db = [self.employee['Employee Database'][field + 'Edit'].element_info.name for field in fields_db]
        
        zipValues = dict(zip(fields_id, values_db))        
        return zipValues


    def handle(self, id_emp):
        self.search_employee(id_emp=id_emp)
        return self.get_fields_values()
