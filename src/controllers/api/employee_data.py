import requests

class EmployeeClient:

    def __init__(self, id):
        self.id = id
        self.request_api = f'https://botgames-employee-data-migration-vwsrh7tyda-uc.a.run.app/employees?id={self.id}'
    
    def request(self):
        
        data = requests.get(self.request_api)                
        return data.json()
    
    def rename_data(self, data):
        data.update({
            "phone": data['phoneNumber']
        })
        data.pop('phoneNumber')
        return data
