import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame 'products' which has columns:
    - 'product_id' (int)
    - 'low_fats' (str, 'Y' or 'N')
    - 'recyclable' (str, 'Y' or 'N')

    It returns a new DataFrame containing only the 'product_id' of those rows
    where both 'low_fats' and 'recyclable' are 'Y'.

    Parameters:
    products (pd.DataFrame): DataFrame containing product info.

    Returns:
    pd.DataFrame: A DataFrame with one column ('product_id') for products that
                  are both low fat and recyclable.
    """
    # Filter rows for low_fats == 'Y' and recyclable == 'Y', then select 'product_id'
    result_df = products.loc[
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'),
        ['product_id']
    ]

    return result_df


if __name__ == "__main__":
    # Example usage
    data = {
        'product_id': [0, 1, 2, 3, 4],
        'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
        'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
    }
    df_products = pd.DataFrame(data)
    result = find_products(df_products)
    print(result)

    # Expected output:
    #    product_id
    # 1           1
    # 3           3

    # Test Case 1: No products match
    test_data1 = {
        'product_id': [5, 6],
        'low_fats': ['N', 'N'],
        'recyclable': ['N', 'Y']
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = find_products(df_test1)
    assert res1.empty, "Expected no matching products."

    # Test Case 2: All products match
    test_data2 = {
        'product_id': [7, 8],
        'low_fats': ['Y', 'Y'],
        'recyclable': ['Y', 'Y']
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = find_products(df_test2)
    assert len(res2) == 2, "Expected 2 matching products (both)."

    # Test Case 3: Mixed scenario
    test_data3 = {
        'product_id': [9, 10, 11],
        'low_fats': ['Y', 'N', 'Y'],
        'recyclable': ['N', 'Y', 'Y']
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = find_products(df_test3)
    # Only product_id=11 matches (low_fats='Y', recyclable='Y')
    assert len(res3) == 1, "Expected exactly 1 matching product."
    assert res3.iloc[0]['product_id'] == 11

    print("All test cases passed successfully!")

# Explanation:
# - Products with product_id=1 and product_id=3 have both low_fats='Y' and recyclable='Y'.
# - We select only those rows and return the 'product_id' column.

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows, because we perform a single pass filter.
# Space Complexity: O(N), as we might need to store a subset of the original DataFrame in the worst case.
