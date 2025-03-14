import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with columns ['unique_id', 'name'], where 'unique_id' is null if
    the employee does not exist in employee_uni.
    """
    # Perform a left join: employees left, employee_uni right
    merged_df = employees.merge(employee_uni, on='id', how='left')

    # Reorder and rename columns as desired
    # 'unique_id' remains the same, 'name' from employees
    result = merged_df[['unique_id', 'name']]

    return result


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Provided example
    employees_data_1 = {
        'id': [1, 7, 11, 90, 3],
        'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
    }
    employeeuni_data_1 = {
        'id': [3, 11, 90],
        'unique_id': [1, 2, 3]
    }
    df_employees_1 = pd.DataFrame(employees_data_1)
    df_employeeuni_1 = pd.DataFrame(employeeuni_data_1)
    result_1 = replace_employee_id(df_employees_1, df_employeeuni_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Explanation:
    # Alice (id=1) => null
    # Bob   (id=7) => null
    # Meir  (id=11) => 2
    # Winston (id=90) => 3
    # Jonathan (id=3) => 1

    # Test Case 2: All employees have unique IDs
    employees_data_2 = {
        'id': [2, 4],
        'name': ['Charlie', 'Dennis']
    }
    employeeuni_data_2 = {
        'id': [2, 4],
        'unique_id': [10, 20]
    }
    df_employees_2 = pd.DataFrame(employees_data_2)
    df_employeeuni_2 = pd.DataFrame(employeeuni_data_2)
    result_2 = replace_employee_id(df_employees_2, df_employeeuni_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Expected:
    # id=2 => unique_id=10, name=Charlie
    # id=4 => unique_id=20, name=Dennis

    # Test Case 3: No employees in employee_uni
    employees_data_3 = {
        'id': [5, 6],
        'name': ['Eve', 'Frank']
    }
    employeeuni_data_3 = {
        'id': [],
        'unique_id': []
    }
    df_employees_3 = pd.DataFrame(employees_data_3)
    df_employeeuni_3 = pd.DataFrame(employeeuni_data_3)
    result_3 = replace_employee_id(df_employees_3, df_employeeuni_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Expected:
    # All unique_id => null

    # Test Case 4: No employees in employees
    employees_data_4 = {
        'id': [],
        'name': []
    }
    employeeuni_data_4 = {
        'id': [1, 2],
        'unique_id': [10, 20]
    }
    df_employees_4 = pd.DataFrame(employees_data_4)
    df_employeeuni_4 = pd.DataFrame(employeeuni_data_4)
    result_4 = replace_employee_id(df_employees_4, df_employeeuni_4)
    print("\nTest Case 4 Result:")
    print(result_4)
    # Expected:
    # No rows in the output


# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n) for merging, where n is the number of rows in the larger DataFrame.
# Space Complexity: O(n) for storing the merged data and output.
