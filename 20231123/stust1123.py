class Employee:
    def __init__(emp,name,id,salary,department):
        emp.name=name
        emp.id=id
        emp.salary=salary
        emp.department=department
        
    
    def print_employee_details(emp):
        print("My name is", emp.name)
        print("Id is",emp.id)
        print("Sarlary is", emp.salary)
        print("Department is ",emp.department)
        print("----------------------")
        
    def calculate_emp_salary(emp,salary,hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
            emp.salary = emp.salary + (overtime * (emp.salary / 50))
        else:
            emp.salary = emp.salary * (hours_worked / 50)
        
    def assign_department(emp,newdepartment):
        emp.department = newdepartment
        

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")

employee2.calculate_emp_salary(45000, 30)
employee4.calculate_emp_salary(45000, 0)

print("****************")
print("Updated Employee Details:")

employee2.print_employee_details()
employee4.print_employee_details()

