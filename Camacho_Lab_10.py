#River Camacho
#Lab 10 - Classes
#5/8/2019

#Incomplete
#Could not figure out how to label each instance of the class.

import employee

def main():

    data = make_list()

    display_list(data)

def make_list():

    employee_data = []

    for count in range(1,4):

        
    
        name = input("Enter employee name: ")

        id_number = input("Enter employee id number: ")

        department = input("Enter employee department: ")

        job_title = input("Enter the employee job title: ")

        


        worker = employee.Employee(name, id_number, department, job_title)


        employee_data.append(worker)

    return employee_data

def display_list(employee_data):


    for item in employee_data:
        
        print()
        print(item)
       
        
        

main()

        

    
    
    
