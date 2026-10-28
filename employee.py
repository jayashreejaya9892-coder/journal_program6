import sys
def employee_details(name,employee_id,department,salary):
    return f"Name:{name}\n Employee id:{employee_id}\n Department:{department}\n Salary:{salary}"

if __name__=="__main__":
    name=str(sys.argv[1])
    employee_id=str(sys.argv[2])
    department=str(sys.argv[3])
    salary=str(sys.argv[4])

    print("\n Employee Details")
    print("---------------------")
    print(employee_details(name,employee_id,department,salary))