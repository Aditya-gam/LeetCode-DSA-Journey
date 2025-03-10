import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Groups by date_id and make_name, computing the distinct count of lead_id and partner_id.
    Returns a DataFrame with columns:
      [date_id, make_name, unique_leads, unique_partners].
    """
    # Group by date_id and make_name
    grouped = daily_sales.groupby(['date_id', 'make_name'], as_index=False).agg({
        'lead_id': pd.Series.nunique,
        'partner_id': pd.Series.nunique
    })

    # Rename columns to match desired output
    grouped.rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners'
    }, inplace=True)

    return grouped


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Provided example
    data_1 = {
        'date_id': [
            '2020-12-8', '2020-12-8', '2020-12-8',
            '2020-12-7', '2020-12-7', '2020-12-8',
            '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'
        ],
        'make_name': [
            'toyota', 'toyota', 'toyota',
            'toyota', 'toyota', 'honda',
            'honda', 'honda', 'honda', 'honda'
        ],
        'lead_id': [
            0, 1, 1,
            0, 0, 1,
            2, 0, 1, 2
        ],
        'partner_id': [
            1, 0, 2,
            2, 1, 2,
            1, 1, 2, 1
        ]
    }
    df_sales_1 = pd.DataFrame(data_1)
    result_1 = daily_leads_and_partners(df_sales_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected Output (any order of rows is acceptable):
    # date_id   make_name  unique_leads  unique_partners
    # 2020-12-8 toyota           2               3
    # 2020-12-7 toyota           1               2
    # 2020-12-8 honda            2               2
    # 2020-12-7 honda            3               2

    # Test Case 2: Single date, multiple makes
    data_2 = {
        'date_id': [
            '2021-01-01', '2021-01-01', '2021-01-01',
            '2021-01-01', '2021-01-01'
        ],
        'make_name': [
            'ford', 'ford', 'toyota', 'toyota', 'toyota'
        ],
        'lead_id': [1, 2, 2, 3, 3],
        'partner_id': [5, 5, 6, 6, 7]
    }
    df_sales_2 = pd.DataFrame(data_2)
    result_2 = daily_leads_and_partners(df_sales_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Explanation:
    # For date=2021-01-01, "ford" has lead_id=[1,2], partner_id=[5] => unique_leads=2, unique_partners=1
    #                    "toyota" has lead_id=[2,3], partner_id=[6,7] => unique_leads=2, unique_partners=2

    # Test Case 3: Multiple dates, single make
    data_3 = {
        'date_id': ['2021-02-01', '2021-02-02', '2021-02-02'],
        'make_name': ['bmw', 'bmw', 'bmw'],
        'lead_id': [10, 11, 10],
        'partner_id': [20, 20, 21]
    }
    df_sales_3 = pd.DataFrame(data_3)
    result_3 = daily_leads_and_partners(df_sales_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Explanation:
    # date=2021-02-01 -> make_name="bmw", lead_id=[10], partner_id=[20]
    # date=2021-02-02 -> make_name="bmw", lead_id=[10,11], partner_id=[20,21]

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n), where n is the number of rows in daily_sales.
#                  Grouping and distinct counting in Pandas typically run in O(n).
# Space Complexity: O(n), primarily for intermediate group structures.
