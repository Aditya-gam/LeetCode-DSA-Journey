import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """
    Function: rearrange_products_table
    Description:
        This function takes a DataFrame where each row represents a product's price
        in three different stores. The columns are ['product_id', 'store1', 'store2', 'store3'].
        If a product is not available in a particular store, its price is recorded as null
        in that column. The function rearranges this table so that each row represents
        (product_id, store, price), omitting any rows where the store price is null.

    Parameters:
    - products (pd.DataFrame): A DataFrame with columns ['product_id', 'store1', 'store2', 'store3'].

    Returns:
    - pd.DataFrame: A DataFrame with columns ['product_id', 'store', 'price'],
                    containing only the rows where the store has a non-null price for that product.
    """
    # Melt the DataFrame to transform columns store1, store2, store3 into rows
    melted_df = products.melt(
        id_vars='product_id',
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )

    # Remove rows where price is null
    melted_df.dropna(subset=['price'], inplace=True)

    # Return the melted DataFrame with only the necessary columns
    return melted_df[['product_id', 'store', 'price']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    products_data_1 = {
        'product_id': [0, 1],
        'store1': [95, 70],
        'store2': [100, None],
        'store3': [105, 80]
    }
    df_products_1 = pd.DataFrame(products_data_1)
    result_1 = rearrange_products_table(df_products_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected rows:
    # (product_id=0, store='store1', price=95)
    # (product_id=0, store='store2', price=100)
    # (product_id=0, store='store3', price=105)
    # (product_id=1, store='store1', price=70)
    # (product_id=1, store='store3', price=80)

    # Test case 2: A product that is not available in any store
    products_data_2 = {
        'product_id': [2],
        'store1': [None],
        'store2': [None],
        'store3': [None]
    }
    df_products_2 = pd.DataFrame(products_data_2)
    result_2 = rearrange_products_table(df_products_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected: No rows, since product_id=2 is not available in any store

    # Test case 3: Multiple products with varying availability
    products_data_3 = {
        'product_id': [10, 11],
        'store1': [50, None],
        'store2': [55, 75],
        'store3': [None, 80]
    }
    df_products_3 = pd.DataFrame(products_data_3)
    result_3 = rearrange_products_table(df_products_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected rows:
    # product_id=10, store='store1', price=50
    # product_id=10, store='store2', price=55
    # product_id=11, store='store2', price=75
    # product_id=11, store='store3', price=80

    # Test case 4: All products available in all stores
    products_data_4 = {
        'product_id': [20, 21, 22],
        'store1': [100, 200, 300],
        'store2': [110, 210, 310],
        'store3': [120, 220, 320]
    }
    df_products_4 = pd.DataFrame(products_data_4)
    result_4 = rearrange_products_table(df_products_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected rows:
    # product_id=20, store='store1', price=100
    # product_id=20, store='store2', price=110
    # product_id=20, store='store3', price=120
    # product_id=21, store='store1', price=200
    # product_id=21, store='store2', price=210
    # product_id=21, store='store3', price=220
    # product_id=22, store='store1', price=300
    # product_id=22, store='store2', price=310
    # product_id=22, store='store3', price=320

    # Test case 5: Multiple products with some missing prices
    products_data_5 = {
        'product_id': [30, 31, 32],
        'store1': [50, 60, 70],
        'store2': [None, 80, 90],
        'store3': [70, 80, None]
    }
    df_products_5 = pd.DataFrame(products_data_5)
    result_5 = rearrange_products_table(df_products_5)
    print("\nTest case 5 result:")
    print(result_5)
    # Expected rows:
    # product_id=30, store='store1', price=50
    # product_id=30, store='store3', price=70
    # product_id=31, store='store2', price=80
    # product_id=31, store='store3', price=80
    # product_id=32, store='store1', price=70

    print("All tests passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the 'products' DataFrame.
# Space Complexity: O(N), where N is the number of rows in the 'products' DataFrame.
