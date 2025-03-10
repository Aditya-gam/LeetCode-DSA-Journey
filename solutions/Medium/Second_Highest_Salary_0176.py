import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Function: second_highest_salary
    Description:
        This function takes a DataFrame containing 'id' and 'salary' columns, and returns
        a single-row DataFrame with the column 'SecondHighestSalary' representing the
        second highest distinct salary. If there is no second highest distinct salary,
        it returns None in that field.

    Parameters:
    - employee (pd.DataFrame): A DataFrame with columns ['id', 'salary'].

    Returns:
    - pd.DataFrame: A single-row DataFrame with one column 'SecondHighestSalary'.
    """
    # Drop duplicate salaries and sort in descending order
    distinct_salaries = employee['salary'].drop_duplicates(
    ).sort_values(ascending=False)

    # Check if there are at least two distinct salaries
    if len(distinct_salaries) < 2:
        second_highest = None
    else:
        second_highest = distinct_salaries.iloc[1]

    # Return the result in the desired format (single-row DataFrame)
    return pd.DataFrame({"SecondHighestSalary": [second_highest]})


if __name__ == "__main__":
    # Test case 1: Basic example with three employees
    data1 = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300]
    }
    df1 = pd.DataFrame(data1)
    result1 = second_highest_salary(df1)
    print("Test case 1 result:\n", result1, "\nExpected: 200\n")

    # Test case 2: Only one employee record
    data2 = {
        'id': [1],
        'salary': [100]
    }
    df2 = pd.DataFrame(data2)
    result2 = second_highest_salary(df2)
    print("Test case 2 result:\n", result2, "\nExpected: None\n")

    # Test case 3: Multiple employees with duplicate salaries
    data3 = {
        'id': [1, 2, 3, 4, 5],
        'salary': [300, 200, 300, 100, 300]
    }
    df3 = pd.DataFrame(data3)
    result3 = second_highest_salary(df3)
    print("Test case 3 result:\n", result3, "\nExpected: 200\n")

    # Test case 4: Two employees with the same salary
    data4 = {
        'id': [1, 2],
        'salary': [500, 500]
    }
    df4 = pd.DataFrame(data4)
    result4 = second_highest_salary(df4)
    print("Test case 4 result:\n", result4, "\nExpected: None\n")

    # Test case 5: Multiple employees with different salaries
    data5 = {
        'id': [1, 2, 3, 4, 5],
        'salary': [100, 200, 300, 400, 500]
    }
    df5 = pd.DataFrame(data5)
    result5 = second_highest_salary(df5)
    print("Test case 5 result:\n", result5, "\nExpected: 400\n")

    # Test case 6: Multiple employees with negative salaries
    data6 = {
        'id': [1, 2, 3, 4, 5],
        'salary': [-100, -200, -300, -400, -500]
    }
    df6 = pd.DataFrame(data6)
    result6 = second_highest_salary(df6)
    print("Test case 6 result:\n", result6, "\nExpected: -200\n")

    print("All tests passed!")

# Complexity analysis:
# Time complexity: O(n*log(n)) [where n is the number of employees]
# The time complexity is dominated by the sorting operation, which takes O(n*log(n)) time.

# Space complexity: O(n) [where n is the number of employees]
# The space complexity is O(n) because we store the distinct salaries in a separate list.
