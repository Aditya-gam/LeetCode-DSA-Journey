import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Finds managers who have at least five direct reports and returns a
    DataFrame with a single column ['name'] containing the manager's name.
    """
    # Group by managerId and count how many direct reports each manager has
    manager_counts = (
        employee
        .groupby('managerId', as_index=False)['id']
        .count()
        .rename(columns={'id': 'report_count'})
    )

    # Filter for managerIds that have at least 5 direct reports
    manager_with_5 = manager_counts.loc[manager_counts['report_count']
                                        >= 5, 'managerId']

    # Join back to employee to get the manager's name
    # The 'id' is the manager's own ID in the employee table
    managers_df = (
        employee
        .merge(manager_with_5, left_on='id', right_on='managerId')
        [['name']]
    )

    # Note: The result can be returned in any order
    return managers_df


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1 (Provided example)
    data_1 = {
        'id': [101, 102, 103, 104, 105, 106],
        'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
        'department': ['A', 'A', 'A', 'A', 'A', 'B'],
        'managerId': [None, 101, 101, 101, 101, 101]
    }
    df_employee_1 = pd.DataFrame(data_1)
    result_1 = find_managers(df_employee_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Explanation:
    # John (id=101) manages Dan(102),James(103),Amy(104),Anne(105),Ron(106) => 5 direct reports
    # So output => John

    # Test Case 2: No manager with enough direct reports
    data_2 = {
        'id': [1, 2, 3, 4],
        'name': ['A', 'B', 'C', 'D'],
        'department': ['X', 'X', 'Y', 'Z'],
        'managerId': [None, 1, 1, 2]
    }
    df_employee_2 = pd.DataFrame(data_2)
    result_2 = find_managers(df_employee_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Explanation:
    # Manager 1 => 2 direct reports (2, 3)
    # Manager 2 => 1 direct report (4)
    # No one meets the threshold of 5

    # Test Case 3: Multiple managers meeting the threshold
    data_3 = {
        'id': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'name': ['BossA', 'EmpB1', 'EmpB2', 'EmpB3', 'EmpB4', 'BossC', 'EmpC1', 'EmpC2', 'EmpC3', 'EmpC4'],
        'department': ['HR', 'HR', 'HR', 'HR', 'HR', 'Sales', 'Sales', 'Sales', 'Sales', 'Sales'],
        'managerId': [None, 10, 10, 10, 10, None, 15, 15, 15, 15]
    }
    df_employee_3 = pd.DataFrame(data_3)
    result_3 = find_managers(df_employee_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Explanation:
    # BossA (id=10) => 4 direct reports (11,12,13,14)
    # BossC (id=15) => 4 direct reports (16,17,18,19)
    # Neither meets the threshold => empty result

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n), where n is the number of rows in the employee DataFrame,
#                  for grouping and merging operations.
# Space Complexity: O(n) for intermediate DataFrames and final output.
