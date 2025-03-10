import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculates a special bonus for each employee:
    - Bonus is the salary if 'employee_id' is odd and the 'name' does not start with 'M'.
    - Otherwise, the bonus is 0.

    Parameters:
    employees (pd.DataFrame): A DataFrame with columns 'employee_id', 'name', and 'salary'.

    Returns:
    pd.DataFrame: A DataFrame with columns 'employee_id' and 'bonus', sorted by 'employee_id'.
    """
    # Define the condition: odd employee_id AND name not starting with 'M'
    condition = (employees['employee_id'] %
                 2 != 0) & ~employees['name'].str.startswith('M')

    # Apply the condition to determine the bonus
    employees['bonus'] = employees['salary'].where(condition, other=0)

    # Sort by employee_id
    employees_sorted = employees.sort_values(
        by='employee_id').reset_index(drop=True)

    # Return only the required columns
    return employees_sorted[['employee_id', 'bonus']]


if __name__ == "__main__":
    # Example usage
    data = {
        'employee_id': [2, 3, 7, 8, 9],
        'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
        'salary': [3000, 3800, 7400, 6100, 7700]
    }
    df_employees = pd.DataFrame(data)
    result_df = calculate_special_bonus(df_employees)
    print(result_df)

    # Expected output:
    #    employee_id  bonus
    # 0            2      0
    # 1            3      0
    # 2            7   7400
    # 3            8      0
    # 4            9   7700

    # Test Case 1: No employees meet the bonus criteria
    test_data1 = {
        'employee_id': [2, 4, 10],
        'name': ['Megan', 'Marco', 'Mallory'],
        'salary': [1000, 2000, 3000]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = calculate_special_bonus(df_test1)
    # All IDs are even or names start with 'M'
    assert all(res1['bonus'] == 0), "Expected all bonuses to be 0."

    # Test Case 2: All employees meet the bonus criteria
    test_data2 = {
        'employee_id': [1, 5, 7],
        'name': ['Alice', 'Bella', 'Clark'],  # None start with 'M'
        'salary': [1000, 2000, 3000]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = calculate_special_bonus(df_test2)
    # All IDs are odd and names do not start with 'M'
    assert all(res2['bonus'] == df_test2['salary']
               ), "Expected all bonuses to match salaries."

    # Test Case 3: Mixed scenario
    test_data3 = {
        'employee_id': [11, 12, 13],
        # 'Miles' starts with 'M'; 'michael' starts with lowercase 'm'
        'name': ['Miles', 'Oscar', 'michael'],
        'salary': [5000, 6000, 7000]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = calculate_special_bonus(df_test3)
    # 11 -> odd, but name starts with 'M' => 0
    # 12 -> even => 0
    # 13 -> odd, but name starts with 'm' (lowercase) => does NOT start with uppercase 'M', so this qualifies
    assert res3.iloc[0]['bonus'] == 0  # employee 11
    assert res3.iloc[1]['bonus'] == 0  # employee 12
    assert res3.iloc[2]['bonus'] == 7000  # employee 13

    print("All test cases passed successfully!")

# Explanation:
# - Employee 2 (even id) -> bonus = 0
# - Employee 3 (odd id) but name starts with 'M' -> bonus = 0
# - Employee 7 (odd id, name does not start with 'M') -> bonus = salary = 7400
# - Employee 8 (even id) -> bonus = 0
# - Employee 9 (odd id, name does not start with 'M') -> bonus = salary = 7700

# Complexity Analysis
# Time Complexity: O(N), where N is the number of employees, as we evaluate each row once.
# Space Complexity: O(N) for storing the output and any intermediate columns.
