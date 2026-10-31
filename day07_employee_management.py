employee = [
    { "id": "EMP001", "name": "Ali", "department": "Development", "salary": 50000 }, 
    { "id": "EMP002", "name": "Sara", "department": "HR", "salary": 60000 }, 
    { "id": "EM003", "name": "Ahmed", "department": "Development", "salary": 49000 } 
]
def add_employee():
    id = input("Enter the employee id : ")
    name = input("Enter the name oo employee : ")
    department = input("Enter the department name : ")
    while True:
        try:
            salary = int(input("Enter the salary : "))
            if(salary < 0):
                print("salary  should not be negative.")
                continue
            break
        except ValueError:
                print("Error: Please enter a valid whole number.")
    emp = {
        "id": id,
        "name": name,
        "department": department,
        "salary": salary
    }
    employee.append(emp)
    print("Employee data has been add.")
def view_employees():
    if not employee:
        print("No employee records found!\n")
        return
    
    print("\n" + "="*50)
    print("           ALL EMPLOYEES LIST           ")
    print("="*50)
    for index, emp in enumerate(employee, start=1):
        print(f"{index}. ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")
    print("="*50 + "\n")

def search_employee():
    search_id = input("Enter the employee ID to search (e.g., EMP001): ")
    found = False
    
    for emp in employee:
        if emp['id'].lower() == search_id.lower():
            print("\n" + "="*40)
            print("           EMPLOYEE FOUND           ")
            print("="*40)
            print(f"ID         : {emp['id']}")
            print(f"Name       : {emp['name']}")
            print(f"Department : {emp['department']}")
            print(f"Salary     : {emp['salary']}")
            print("="*40 + "\n")
            found = True
            break
            
    if not found:
        print(f"Error: Employee with ID '{search_id}' not found.\n")

while True:
    print("\n===== TechNova Employee Management =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 4.")