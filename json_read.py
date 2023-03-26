import json
file=open('C:\\Users\\HP\\OneDrive\\Documents\\Edyoda py practice\\python file handling\\Edyoda_assignment_6\\Assignment_1\\task1\\employee.json')
data=json.load(file)
# print(data)

emp=data.values()


class Employee:
    emplist=[]
    def __init__(self,emp_data):
        self.emp_data=emp_data
    def emp(self):
        for i in emp:
            self.emplist.append(i)
        print(self.emplist)

obj=Employee(emp)
obj.emp()