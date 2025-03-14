import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes two DataFrames, df1 and df2, both of which contain the
    columns: 'student_id', 'name', and 'age'. It concatenates df2 below df1,
    effectively stacking them vertically into one DataFrame.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame containing student information.
    df2 (pd.DataFrame): The second DataFrame containing student information.

    Returns:
    pd.DataFrame: A new DataFrame containing all rows from df1 followed by all rows from df2.
    """
    # Concatenate the two DataFrames vertically
    result_df = pd.concat([df1, df2], axis=0, ignore_index=True)

    return result_df


if __name__ == "__main__":
    # Example usage of concatenateTables
    data1 = {
        'student_id': [1, 2, 3, 4],
        'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
        'age': [8, 6, 15, 17]
    }
    data2 = {
        'student_id': [5, 6],
        'name': ['Leo', 'Alex'],
        'age': [7, 7]
    }

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Call the function
    concatenated_df = concatenateTables(df1, df2)
    print(concatenated_df)

    # Expected output:
    #    student_id     name  age
    # 0           1    Mason    8
    # 1           2      Ava    6
    # 2           3   Taylor   15
    # 3           4  Georgia   17
    # 4           5      Leo    7
    # 5           6     Alex    7

    # Test case 1:
    df1_test = pd.DataFrame({
        'student_id': [1],
        'name': ['John'],
        'age': [10]
    })
    df2_test = pd.DataFrame({
        'student_id': [2],
        'name': ['Doe'],
        'age': [12]
    })
    concated_test1 = concatenateTables(df1_test, df2_test)
    assert len(concated_test1) == 2
    assert concated_test1.iloc[0]['name'] == 'John'
    assert concated_test1.iloc[1]['name'] == 'Doe'

    # Test case 2:
    df1_test2 = pd.DataFrame({
        'student_id': [],
        'name': [],
        'age': []
    })
    df2_test2 = pd.DataFrame({
        'student_id': [100, 101, 102],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [9, 10, 11]
    })
    concated_test2 = concatenateTables(df1_test2, df2_test2)
    assert len(concated_test2) == 3
    assert concated_test2.iloc[2]['age'] == 11

    # Test case 3: Duplicate IDs, just to confirm concatenation still works.
    df1_test3 = pd.DataFrame({
        'student_id': [1, 2],
        'name': ['Name1', 'Name2'],
        'age': [11, 12]
    })
    df2_test3 = pd.DataFrame({
        'student_id': [2, 3],
        'name': ['DuplicateName2', 'Name3'],
        'age': [12, 13]
    })
    concated_test3 = concatenateTables(df1_test3, df2_test3)
    assert len(concated_test3) == 4
    # Confirm the second row in df1 and the first row in df2 are both present
    assert concated_test3.iloc[1]['student_id'] == 2
    assert concated_test3.iloc[2]['student_id'] == 2
    print("All test cases passed successfully!")

# The function 'concatenateTables' uses pd.concat to stack df2 underneath df1.
# It returns a single DataFrame containing all the rows from both inputs.

# Complexity Analysis
# Time Complexity: O(n + m), where n is the number of rows in df1, and m is the number of rows in df2.
# This is because pandas needs to process each row once for the concatenation.
# Space Complexity: O(n + m), as the output DataFrame contains all rows from both inputs.
