import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame 'report' with columns:
    'product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'.
    It reshapes the data from wide format (multiple 'quarter_X' columns)
    to long format, resulting in a DataFrame with columns:
    ['product', 'quarter', 'sales'].

    Parameters:
    report (pd.DataFrame): The input DataFrame containing the wide-format data.

    Returns:
    pd.DataFrame: A DataFrame melted into long format, with each row
                  representing sales for a product in a specific quarter.
    """
    # Use pd.melt to unpivot the quarter columns into a single 'quarter' column
    melted_df = pd.melt(
        report,
        id_vars=['product'],            # Columns to remain unchanged
        value_vars=['quarter_1', 'quarter_2', 'quarter_3',
                    'quarter_4'],  # Columns to unpivot
        var_name='quarter',             # Name of the new column representing the quarter
        value_name='sales'             # Name of the new column representing the sales value
    )

    return melted_df


if __name__ == "__main__":
    # Example usage
    data = {
        'product': ['Umbrella', 'SleepingBag'],
        'quarter_1': [417, 800],
        'quarter_2': [224, 936],
        'quarter_3': [379, 93],
        'quarter_4': [611, 875]
    }
    df_report = pd.DataFrame(data)
    melted_result = meltTable(df_report)
    print(melted_result)

    # Expected output (order may vary due to how melt processes rows):
    #         product    quarter  sales
    # 0      Umbrella  quarter_1    417
    # 1   SleepingBag  quarter_1    800
    # 2      Umbrella  quarter_2    224
    # 3   SleepingBag  quarter_2    936
    # 4      Umbrella  quarter_3    379
    # 5   SleepingBag  quarter_3     93
    # 6      Umbrella  quarter_4    611
    # 7   SleepingBag  quarter_4    875

    # Test Case 1: Single row
    test_data1 = {
        'product': ['SingleItem'],
        'quarter_1': [10],
        'quarter_2': [20],
        'quarter_3': [30],
        'quarter_4': [40]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = meltTable(df_test1)
    assert len(res1) == 4  # 4 quarters -> 4 rows
    assert set(res1.columns) == {'product', 'quarter', 'sales'}

    # Test Case 2: No sales in certain quarters
    test_data2 = {
        'product': ['RainCoat', 'SnowBoot'],
        'quarter_1': [0, 0],
        'quarter_2': [100, 0],
        'quarter_3': [200, 300],
        'quarter_4': [0, 400]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = meltTable(df_test2)
    # Expect 8 rows total
    assert len(res2) == 8
    # Check one row
    assert res2.iloc[2]['product'] in ['RainCoat', 'SnowBoot']

    # Test Case 3: Multiple products
    test_data3 = {
        'product': ['ItemA', 'ItemB', 'ItemC'],
        'quarter_1': [1, 4, 7],
        'quarter_2': [2, 5, 8],
        'quarter_3': [3, 6, 9],
        'quarter_4': [10, 11, 12]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = meltTable(df_test3)
    # Expect 3 products * 4 quarters = 12 rows
    assert len(res3) == 12
    print("All test cases passed successfully!")

# Explanation:
# - pd.melt reshapes the columns 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'
#   into two columns: 'quarter' and 'sales'.
# - The 'product' column remains unchanged (id_vars).

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the DataFrame.
#   The melt operation touches each row once per unpivoted column.
# Space Complexity: O(N), as the melted DataFrame will generally have the same
#   total count of data points, just rearranged.
