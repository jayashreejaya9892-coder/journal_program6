from employee import employee_details

def test_employee_details():
    result = employee_details("Rahul", "EMP01", "IT", "50000")

    expected = "Name:Rahul\n Employee id:EMP01\nDepartment:IT\nSalary:50000"

    assert result == expected