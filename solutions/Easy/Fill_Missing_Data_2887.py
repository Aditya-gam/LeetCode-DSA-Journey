import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame 'products' which has columns:
    'name', 'quantity', and 'price'.
    It fills any missing values (None or NaN) in the 'quantity' column with 0.

    Parameters:
    products (pd.DataFrame): The input DataFrame containing product information.

    Returns:
    pd.DataFrame: A DataFrame with all missing 'quantity' values filled with 0.
    """
    # Fill missing values in the 'quantity' column with 0
    products['quantity'] = products['quantity'].fillna(0)

    return products


if __name__ == "__main__":
    # Example usage
    data = {
        'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
        'quantity': [None, None, 779, 849],
        'price': [135, 821, 9319, 3051]
    }
    df = pd.DataFrame(data)
    filled_df = fillMissingValues(df)
    print(filled_df)

    # Expected output:
    #              name  quantity  price
    # 0     Wristwatch         0    135
    # 1 WirelessEarbuds         0    821
    # 2      GolfClubs       779   9319
    # 3        Printer       849   3051

    # Test Case 1: No missing values
    test_data1 = {
        'name': ['Item1', 'Item2'],
        'quantity': [10, 20],
        'price': [100, 200]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = fillMissingValues(df_test1)
    # Expect the same DataFrame (no changes)
    assert (res1['quantity'] == [10, 20]).all()

    # Test Case 2: All missing quantities
    test_data2 = {
        'name': ['Item3', 'Item4'],
        'quantity': [None, None],
        'price': [300, 400]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = fillMissingValues(df_test2)
    # Expect all quantities to be 0
    assert (res2['quantity'] == [0, 0]).all()

    # Test Case 3: Some missing, some not
    test_data3 = {
        'name': ['Item5', 'Item6', 'Item7'],
        'quantity': [5, None, 15],
        'price': [500, 600, 700]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = fillMissingValues(df_test3)
    # Only the missing one should become 0
    assert res3.iloc[0]['quantity'] == 5
    assert res3.iloc[1]['quantity'] == 0
    assert res3.iloc[2]['quantity'] == 15

    print("All test cases passed successfully!")

# Explanation:
# We use the fillna(0) function to replace any missing values in the 'quantity' column with 0.
# The updated DataFrame is then returned.

# Complexity Analysis
# Time Complexity: O(n), where n is the number of rows in the products DataFrame.
# We are iterating only once over the 'quantity' column to fill missing values.
# Space Complexity: O(1), since we are modifying the DataFrame in place and not using significant extra space.
