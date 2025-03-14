import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    This function removes duplicate rows from the 'customers' DataFrame based on 
    the 'email' column, keeping only the first occurrence of each unique email.
    It returns the resulting DataFrame with duplicates removed.
    """
    # Drop duplicates based on email, keeping only the first occurrence
    cleaned_df = customers.drop_duplicates(subset=['email'], keep='first')

    return cleaned_df


# Example test cases
if __name__ == "__main__":
    data = {
        "customer_id": [1, 2, 3, 4, 5, 6],
        "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        "email": [
            "emily@example.com",
            "michael@example.com",
            "sarah@example.com",
            "john@example.com",
            "john@example.com",
            "alice@example.com"
        ]
    }
    df = pd.DataFrame(data)
    result_df = dropDuplicateEmails(df)
    print(result_df)
    # Expected output:
    #    customer_id     name               email
    # 0            1     Ella   emily@example.com
    # 1            2    David michael@example.com
    # 2            3  Zachary   sarah@example.com
    # 3            4    Alice    john@example.com
    # 5            6   Violet   alice@example.com

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the DataFrame once
# Space complexity: O(n) - We store the cleaned DataFrame with unique rows
