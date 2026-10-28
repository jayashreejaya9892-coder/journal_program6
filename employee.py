import sys
def employee_details(name,employee_id,department,salary):
    return f"Name:{name}\n Employee id:{employee_id}\n Department:{department}\n Salary:{salary}"

if __name__=="__main__":
    name=sys.argv[1]
    employee_id=sys.argv[2]
    department=sys.argv[3]
    salary=sys.argv[4]

    print("\n Employee Details")
    print("---------------------")
    print(employee_details(name,employee_id,department,salary))