import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """
    This function filters out users with valid emails.
    A valid email must:
    1. Have a prefix that starts with a letter.
    2. Contain only letters, digits, '_', '.', or '-' in the prefix.
    3. End with '@leetcode.com'.

    Parameters:
    users (pd.DataFrame): A DataFrame with columns 'user_id', 'name', and 'mail'.

    Returns:
    pd.DataFrame: A DataFrame containing users with valid emails.
    """
    import re

    # Define the regex pattern for a valid email
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'

    # Filter the users DataFrame for valid emails
    valid_users = users[users['mail'].str.match(pattern, na=False)]

    return valid_users


if __name__ == "__main__":
    # Example usage
    data = {
        'user_id': [1, 2, 3, 4, 5, 6, 7],
        'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'],
        'mail': [
            'winston@leetcode.com',  # Valid
            'jonathanisgreat',  # No domain -> Invalid
            'bella-@leetcode.com',  # Valid
            'sally.come@leetcode.com',  # Valid
            'quarz#2020@leetcode.com',  # Invalid character '#'
            'david69@gmail.com',  # Wrong domain -> Invalid
            '.shapo@leetcode.com'  # Starts with '.' -> Invalid
        ]
    }
    df_users = pd.DataFrame(data)
    result_df = valid_emails(df_users)
    print(result_df)

    # Expected output:
    #    user_id      name                    mail
    # 0       1   Winston   winston@leetcode.com
    # 2       3  Annabelle    bella-@leetcode.com
    # 3       4     Sally  sally.come@leetcode.com


# Test Cases

# Test Case 1: All emails are valid
test_data1 = {
    'user_id': [8, 9],
    'name': ['Alice', 'Bob'],
    'mail': ['alice99@leetcode.com', 'bob-test@leetcode.com']
}
df_test1 = pd.DataFrame(test_data1)
res1 = valid_emails(df_test1)
assert len(res1) == 2, "Test Case 1 Failed"

# Test Case 2: No valid emails
test_data2 = {
    'user_id': [10, 11],
    'name': ['Charlie', 'David'],
    'mail': ['charlie123@gmail.com', 'david@codeforces.com']
}
df_test2 = pd.DataFrame(test_data2)
res2 = valid_emails(df_test2)
assert res2.empty, "Test Case 2 Failed"

# Test Case 3: Mixed valid and invalid emails
test_data3 = {
    'user_id': [12, 13, 14],
    'name': ['Eve', 'Frank', 'Grace'],
    'mail': ['eve_2023@leetcode.com', 'frank@leetcode', '.grace@leetcode.com']
}
df_test3 = pd.DataFrame(test_data3)
res3 = valid_emails(df_test3)
assert len(res3) == 1 and res3.iloc[0]['user_id'] == 12, "Test Case 3 Failed"

print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the users DataFrame.
# We filter the DataFrame based on the regex pattern, which takes O(N) time.
# Space Complexity: O(N), where N is the number of rows in the users DataFrame.
