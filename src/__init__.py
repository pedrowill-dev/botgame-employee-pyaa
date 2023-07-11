from src.controllers.crawler.employee import EmployeeDataMigration
from src.repositories.employee import EmployeeDatabase
from src.controllers.api.employee_data import EmployeeClient
from src.utils.webdriver.chrome import Chrome

def main():

    browser = Chrome()
    browser = browser.get_driver
    browser.get('https://developer.automationanywhere.com/challenges/automationanywherelabs-employeedatamigration.html')
    
    crawler = EmployeeDataMigration(browser=browser)
    emp_database = EmployeeDatabase()
    
    for _ in range(0, 10):
        id_emp = crawler.get_employee_id()
        emp_client = EmployeeClient(id=id_emp)
        emp_request = emp_client.request()
        emp_request_rename = emp_client.rename_data(emp_request)
        json_values = emp_database.handle(id_emp=id_emp)
        json_values.update(emp_request_rename)
        crawler.send_data_employe_input(json_values)
        
        