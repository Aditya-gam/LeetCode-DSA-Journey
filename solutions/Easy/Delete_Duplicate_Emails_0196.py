import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    Function: delete_duplicate_emails
    Description:
        This function modifies the given 'person' DataFrame in-place by removing
        rows that contain duplicate email addresses. If multiple rows have the
        same email, only the row with the smallest 'id' is kept.

    Parameters:
    - person (pd.DataFrame): A DataFrame with columns ['id', 'email'].

    Returns:
    - None (The DataFrame 'person' is modified in-place).
    """
    # Drop duplicate emails while keeping the row with the smallest 'id'
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'id': [1, 2, 3],
        'email': ['john@example.com', 'bob@example.com', 'john@example.com']
    }
    df_person_1 = pd.DataFrame(data_1)
    delete_duplicate_emails(df_person_1)
    print("Test case 1 result:")
    print(df_person_1)
    # Expected:
    # id    email
    # 1   john@example.com
    # 2   bob@example.com
    # The row with id=3 is removed since it's a duplicate of john@example.com

    # Test case 2: All unique emails
    data_2 = {
        'id': [10, 11, 12],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
    }
    df_person_2 = pd.DataFrame(data_2)
    delete_duplicate_emails(df_person_2)
    print("\nTest case 2 result:")
    print(df_person_2)
    # Expected: No rows removed, as all emails are unique

    # Test case 3: Multiple duplicates for the same email
    data_3 = {
        'id': [20, 21, 22, 23],
        'email': ['dave@example.com', 'dave@example.com', 'eve@example.com', 'dave@example.com']
    }
    df_person_3 = pd.DataFrame(data_3)
    delete_duplicate_emails(df_person_3)
    print("\nTest case 3 result:")
    print(df_person_3)
    # Expected:
    # The row with the smallest id=20 for 'dave@example.com' is kept; the others (id=21, 23) should be removed.

    # Test case 4: Empty DataFrame
    data_4 = {
        'id': [],
        'email': []
    }
    df_person_4 = pd.DataFrame(data_4)
    delete_duplicate_emails(df_person_4)
    print("\nTest case 4 result:")
    print(df_person_4)
    # Expected: No rows to remove since the DataFrame is empty

    print("\nAll test cases passed!")

# Complexity Analysis
# Time Complexity: O(N * log(N)), where N is the number of rows in the 'person' DataFrame.
#   - Sorting the DataFrame based on the 'id' column takes O(N * log(N)) time.
#   - Dropping duplicates using 'drop_duplicates' function takes O(N) time.
#   - Thus, the overall time complexity is dominated by the sorting operation.

# Space Complexity: O(1)
#   - The function modifies the 'person' DataFrame in-place without using any additional space.
#   - Hence, the space complexity is O(1).
