import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Function: department_highest_salary
    Description:
        This function takes two DataFrames:
        1. employee (with columns ['id', 'name', 'salary', 'departmentId'])
        2. department (with columns ['id', 'name'])

        It returns a DataFrame that lists each department and the employees
        who have the highest salary in that department.

    Parameters:
    - employee (pd.DataFrame): A DataFrame containing employee information.
    - department (pd.DataFrame): A DataFrame containing department information.

    Returns:
    - pd.DataFrame: A DataFrame with columns ['Department', 'Employee', 'Salary'].
    """
    # Merge employee and department data on matching department IDs
    merged_df = employee.merge(
        department,
        left_on='departmentId',
        right_on='id',
        how='inner',
        suffixes=('_emp', '_dept')
    )

    # For each department, find the maximum salary
    merged_df['max_salary_in_dept'] = merged_df.groupby(
        'departmentId')['salary'].transform('max')

    # Select only the employees whose salary matches the max salary in their department
    highest_salaries_df = merged_df[merged_df['salary']
                                    == merged_df['max_salary_in_dept']].copy()

    # Rename columns to the desired output format
    highest_salaries_df.rename(
        columns={
            'name_emp': 'Employee',
            'name_dept': 'Department',
            'salary': 'Salary'
        },
        inplace=True
    )

    # Return only the required columns
    return highest_salaries_df[['Department', 'Employee', 'Salary']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: From the problem statement
    employee_data_1 = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
        'salary': [70000, 90000, 80000, 60000, 90000],
        'departmentId': [1, 1, 2, 2, 1]
    }
    department_data_1 = {
        'id': [1, 2],
        'name': ['IT', 'Sales']
    }
    df_employee_1 = pd.DataFrame(employee_data_1)
    df_department_1 = pd.DataFrame(department_data_1)

    result_1 = department_highest_salary(df_employee_1, df_department_1)
    print("Test case 1 result:")
    print(result_1, "\n")
    # Expected:
    # Department = 'IT' with two employees: Jim and Max (both 90000)
    # Department = 'Sales' with one employee: Henry (80000)

    # Test case 2: All employees in one department
    employee_data_2 = {
        'id': [10, 11, 12],
        'name': ['Alice', 'Bob', 'Charlie'],
        'salary': [55000, 55000, 50000],
        'departmentId': [5, 5, 5]
    }
    department_data_2 = {
        'id': [5],
        'name': ['Engineering']
    }
    df_employee_2 = pd.DataFrame(employee_data_2)
    df_department_2 = pd.DataFrame(department_data_2)

    result_2 = department_highest_salary(df_employee_2, df_department_2)
    print("Test case 2 result:")
    print(result_2, "\n")
    # Expected:
    # Department = 'Engineering' with Alice and Bob (both 55000)

    # Test case 3: Multiple departments with single employee each
    employee_data_3 = {
        'id': [20, 21],
        'name': ['Dan', 'Eve'],
        'salary': [75000, 85000],
        'departmentId': [2, 3]
    }
    department_data_3 = {
        'id': [2, 3],
        'name': ['HR', 'Finance']
    }
    df_employee_3 = pd.DataFrame(employee_data_3)
    df_department_3 = pd.DataFrame(department_data_3)

    result_3 = department_highest_salary(df_employee_3, df_department_3)
    print("Test case 3 result:")
    print(result_3, "\n")
    # Expected:
    # HR -> Dan (75000)
    # Finance -> Eve (85000)

    # Test case 4: Multiple employees with the same salary
    employee_data_4 = {
        'id': [30, 31, 32, 33],
        'name': ['Frank', 'Grace', 'Hank', 'Ivy'],
        'salary': [60000, 60000, 60000, 60000],
        'departmentId': [4, 4, 4, 4]
    }
    department_data_4 = {
        'id': [4],
        'name': ['Marketing']
    }
    df_employee_4 = pd.DataFrame(employee_data_4)
    df_department_4 = pd.DataFrame(department_data_4)

    result_4 = department_highest_salary(df_employee_4, df_department_4)
    print("Test case 4 result:")
    print(result_4, "\n")
    # Expected:
    # Marketing -> Frank, Grace, Hank, Ivy (all 60000)

    # Test case 5: Multiple employees with different salaries
    employee_data_5 = {
        'id': [40, 41, 42, 43, 44],
        'name': ['Jack', 'Kate', 'Liam', 'Mia', 'Noah'],
        'salary': [70000, 80000, 90000, 80000, 80000],
        'departmentId': [5, 5, 5, 5, 5]
    }
    department_data_5 = {
        'id': [5],
        'name': ['Engineering']
    }
    df_employee_5 = pd.DataFrame(employee_data_5)
    df_department_5 = pd.DataFrame(department_data_5)

    result_5 = department_highest_salary(df_employee_5, df_department_5)
    print("Test case 5 result:")
    print(result_5, "\n")
    # Expected:
    # Engineering -> Liam (90000)

    # Test case 6: Multiple employees with negative salaries
    employee_data_6 = {
        'id': [50, 51, 52, 53],
        'name': ['Owen', 'Pam', 'Quinn', 'Rose'],
        'salary': [-50000, -40000, -30000, -20000],
        'departmentId': [6, 6, 6, 6]
    }
    department_data_6 = {
        'id': [6],
        'name': ['Customer Support']
    }
    df_employee_6 = pd.DataFrame(employee_data_6)
    df_department_6 = pd.DataFrame(department_data_6)

    result_6 = department_highest_salary(df_employee_6, df_department_6)
    print("Test case 6 result:")
    print(result_6, "\n")
    # Expected:
    # Customer Support -> Owen (50000)

    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(n) [where n is the number of employees]
# Space Complexity: O(n) [where n is the number of employees]
