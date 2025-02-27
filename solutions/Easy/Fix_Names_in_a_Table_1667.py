import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """
    This function fixes the names in the 'users' DataFrame so that only the first character 
    is uppercase and the rest are lowercase. It returns the updated DataFrame sorted by 'user_id'.

    Parameters:
    users (pd.DataFrame): A DataFrame with columns 'user_id' (int) and 'name' (str).

    Returns:
    pd.DataFrame: A DataFrame with corrected names, ordered by 'user_id'.
    """
    # Use the str.capitalize() method to ensure only the first character is uppercase
    users['name'] = users['name'].str.capitalize()

    # Sort the DataFrame by 'user_id' in ascending order and reset the index
    fixed_users = users.sort_values(by='user_id').reset_index(drop=True)

    return fixed_users


if __name__ == "__main__":
    # Example usage
    data = {
        'user_id': [1, 2],
        'name': ['aLice', 'bOB']
    }
    df_users = pd.DataFrame(data)
    fixed_df = fix_names(df_users)
    print(fixed_df)
    # Expected output:
    #    user_id   name
    # 0        1  Alice
    # 1        2    Bob


# Test Cases


# Test Case 1: Basic names with mixed casing
test_data1 = {
    'user_id': [3, 1, 2],
    'name': ['jOHN', 'aLice', 'bOB']
}
df_test1 = pd.DataFrame(test_data1)
res1 = fix_names(df_test1)
assert list(res1['name']) == ['Alice', 'Bob', 'John'], "Test Case 1 Failed"

# Test Case 2: Names already in proper format should remain unchanged
test_data2 = {
    'user_id': [1, 2],
    'name': ['Alice', 'Bob']
}
df_test2 = pd.DataFrame(test_data2)
res2 = fix_names(df_test2)
assert list(res2['name']) == ['Alice', 'Bob'], "Test Case 2 Failed"

# Test Case 3: Names with all lowercase
test_data3 = {
    'user_id': [1, 2],
    'name': ['eve', 'adam']
}
df_test3 = pd.DataFrame(test_data3)
res3 = fix_names(df_test3)
assert list(res3['name']) == ['Eve', 'Adam'], "Test Case 3 Failed"

print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N log N), where N is the number of rows in the DataFrame.
# Sorting the DataFrame by 'user_id' takes O(N log N) time.
# Space Complexity: O(1), since we are modifying the DataFrame in place.
