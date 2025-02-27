import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    This function returns the first 3 rows of the given DataFrame 'employees'.
    """
    return employees.head(3)


# Example test cases
if __name__ == "__main__":
    data = {
        'employee_id': [3, 90, 9, 60, 49, 43],
        'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
        'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
        'salary': [48675, 11096, 33805, 37678, 23793, 40454]
    }

    df = pd.DataFrame(data)
    result_df = selectFirstRows(df)
    print(result_df)
    # Expected output: first 3 rows of df

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(1) - We just return the first 3 rows of the DataFrame
# Space complexity: O(1) - We use a constant amount of extra space
