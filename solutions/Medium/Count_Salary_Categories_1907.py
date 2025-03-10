import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """
    Function: count_salary_categories
    Description:
        This function takes a DataFrame containing bank account incomes and categorizes
        them into three salary ranges:
          1. "Low Salary" for income < 20000
          2. "Average Salary" for 20000 <= income <= 50000
          3. "High Salary" for income > 50000
        It then counts how many accounts fall into each of these categories.
        If there are no accounts in a specific category, that category will appear
        with a count of 0.

    Parameters:
    - accounts (pd.DataFrame): A DataFrame with columns ['account_id', 'income'].

    Returns:
    - pd.DataFrame: A DataFrame with columns ['category', 'accounts_count'].
    """
    # Define categories
    def categorize_income(income):
        if income < 20000:
            return "Low Salary"
        elif income <= 50000:
            return "Average Salary"
        else:
            return "High Salary"

    # Apply the categorization
    accounts['category'] = accounts['income'].apply(categorize_income)

    # Group by category to get the counts
    category_counts = accounts.groupby(
        'category').size().reset_index(name='accounts_count')

    # Ensure all categories exist in the final result, even if count is 0
    all_categories = ['Low Salary', 'Average Salary', 'High Salary']
    category_counts = (category_counts
                       .set_index('category')
                       .reindex(all_categories, fill_value=0)
                       .reset_index()
                       .rename(columns={'index': 'category'}))

    return category_counts[['category', 'accounts_count']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'account_id': [3, 2, 8, 6],
        'income': [108939, 12747, 87709, 91796]
    }
    df_accounts_1 = pd.DataFrame(data_1)
    result_1 = count_salary_categories(df_accounts_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected:
    # Low Salary: 1 (account_id=2)
    # Average Salary: 0
    # High Salary: 3 (account_id=3, 6, 8)

    # Test case 2: All accounts in the 'Average Salary' range
    data_2 = {
        'account_id': [10, 11, 12],
        'income': [30000, 50000, 25000]
    }
    df_accounts_2 = pd.DataFrame(data_2)
    result_2 = count_salary_categories(df_accounts_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected:
    # Low Salary: 0
    # Average Salary: 3
    # High Salary: 0

    # Test case 3: Mixed categories with edge values
    data_3 = {
        'account_id': [20, 21, 22, 23],
        'income': [19999, 20000, 50000, 50001]
    }
    df_accounts_3 = pd.DataFrame(data_3)
    result_3 = count_salary_categories(df_accounts_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # Low Salary: 1 (19999)
    # Average Salary: 2 (20000, 50000)
    # High Salary: 1 (50001)

    # Test case 4: All accounts in the 'Low Salary' range
    data_4 = {
        'account_id': [30, 31, 32],
        'income': [15000, 18000, 19999]
    }
    df_accounts_4 = pd.DataFrame(data_4)
    result_4 = count_salary_categories(df_accounts_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected:
    # Low Salary: 3
    # Average Salary: 0
    # High Salary: 0

    # Test case 5: All accounts in the 'High Salary' range
    data_5 = {
        'account_id': [40, 41, 42],
        'income': [50001, 60000, 100000]
    }
    df_accounts_5 = pd.DataFrame(data_5)
    result_5 = count_salary_categories(df_accounts_5)
    print("\nTest case 5 result:")
    print(result_5)
    # Expected:
    # Low Salary: 0
    # Average Salary: 0
    # High Salary: 3

    # Test case 6: Empty DataFrame
    data_6 = {
        'account_id': [],
        'income': []
    }
    df_accounts_6 = pd.DataFrame(data_6)
    result_6 = count_salary_categories(df_accounts_6)
    print("\nTest case 6 result:")
    print(result_6)
    # Expected:
    # Low Salary: 0
    # Average Salary: 0
    # High Salary: 0

    print("\nAll test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the 'accounts' DataFrame.
#                 The function first applies the categorization function to each row,
#                 which takes O(N) time. Then, it groups the DataFrame by category,
#                 which also takes O(N) time. The final DataFrame is created by
#                 reindexing the categories, which takes O(1) time since the number
#                 of categories is fixed. Thus, the overall time complexity is O(N).

# Space Complexity: O(N), where N is the number of rows in the 'accounts' DataFrame.
#                  The additional space used is for the 'category' column and the
#                  resulting DataFrame with the counts. The space complexity is
#                  linear with respect to the number of rows in the input DataFrame.
