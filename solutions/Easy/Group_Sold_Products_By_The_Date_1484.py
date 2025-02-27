import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates the sold products by date, returning a DataFrame that shows:
      - The date (sell_date),
      - The number of different products sold that date (num_sold),
      - The sorted list of product names in a comma-separated string (products).
    """
    # Group by date, collect unique products
    grouped = (
        activities.groupby('sell_date')['product']
        .apply(lambda x: sorted(set(x)))  # Sort and remove duplicates
        .reset_index(name='product_list')
    )

    # Count how many unique products per date
    grouped['num_sold'] = grouped['product_list'].apply(len)

    # Convert the product list into a comma-separated string
    grouped['products'] = grouped['product_list'].apply(
        lambda lst: ",".join(lst))

    # Drop the 'product_list' column since it's no longer needed
    grouped.drop(columns=['product_list'], inplace=True)

    # Sort by date (if not already sorted)
    grouped.sort_values('sell_date', inplace=True)

    return grouped[['sell_date', 'num_sold', 'products']]


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test case 1: Provided example
    data_1 = {
        'sell_date': [
            '2020-05-30', '2020-06-01', '2020-06-02',
            '2020-05-30', '2020-06-01', '2020-06-02',
            '2020-05-30'
        ],
        'product': [
            'Headphone', 'Pencil', 'Mask',
            'Basketball', 'Bible', 'Mask',
            'T-Shirt'
        ]
    }
    df_activities_1 = pd.DataFrame(data_1)
    result_1 = categorize_products(df_activities_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected:
    #   sell_date  num_sold                    products
    #  2020-05-30         3   Basketball,Headphone,T-Shirt (sorted as "Basketball,Headphone,T-Shirt")
    #  2020-06-01         2                   Bible,Pencil (sorted as "Bible,Pencil")
    #  2020-06-02         1                          Mask

    # Test Case 2: Single date, multiple duplicates
    data_2 = {
        'sell_date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
        'product': ['Apple', 'Apple', 'Banana', 'Apple']
    }
    df_activities_2 = pd.DataFrame(data_2)
    result_2 = categorize_products(df_activities_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Expected:
    #   sell_date  num_sold    products
    #  2021-01-01         2  Apple,Banana

    # Test Case 3: Multiple dates, some repeated products
    data_3 = {
        'sell_date': ['2021-02-10', '2021-02-10', '2021-02-11', '2021-02-12', '2021-02-10'],
        'product': ['Coffee', 'Coffee', 'Bagel', 'Donut', 'Sugar']
    }
    df_activities_3 = pd.DataFrame(data_3)
    result_3 = categorize_products(df_activities_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Expected:
    #   sell_date  num_sold              products
    #  2021-02-10         2        Coffee,Sugar  (sorted lex order: "Coffee,Sugar")
    #  2021-02-11         1              Bagel
    #  2021-02-12         1              Donut

    # Test Case 4: Empty DataFrame
    df_activities_4 = pd.DataFrame(columns=['sell_date', 'product'])
    result_4 = categorize_products(df_activities_4)
    print("\nTest Case 4 Result:")
    print(result_4)
    # Expected: Empty DataFrame

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n log n) in the worst case, where n is the number of rows.
#                  - Grouping by date is O(n) or O(n log n) depending on implementation.
#                  - For each group, we sort the set of unique products.
#                  If k is the maximum number of products in a single date, that sort costs O(k log k).
#                  Summed across all groups, we can approximate it as O(n log n) in the worst case.
# Space Complexity: O(n) for storing intermediate structures (unique sets, etc.).
#                 The final output DataFrame is also O(n) in size.
