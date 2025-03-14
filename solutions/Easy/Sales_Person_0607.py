import pandas as pd


def sales_person(sales_person: pd.DataFrame,
                 company: pd.DataFrame,
                 orders: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame containing the names of all the salespersons who did 
    not have any orders related to the company named "RED".
    """
    # 1. Get the com_id for "RED"
    red_com_id = company.loc[company['name'] == 'RED', 'com_id']

    # 2. Filter orders for that 'red_com_id' to find all sales who sold to RED
    sold_to_red = orders.loc[orders['com_id'].isin(
        red_com_id), 'sales_id'].unique()

    # 3. Filter out those salespersons from 'sales_person'
    remaining_sales = sales_person.loc[~sales_person['sales_id'].isin(sold_to_red), [
        'name']]

    return remaining_sales


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Provided example
    data_sales_person_1 = {
        'sales_id': [1, 2, 3, 4, 5],
        'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
        'salary': [100000, 12000, 65000, 25000, 5000],
        'commission_rate': [6, 5, 12, 25, 10],
        'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
    }
    data_company_1 = {
        'com_id': [1, 2, 3, 4],
        'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
        'city': ['Boston', 'New York', 'Boston', 'Austin']
    }
    data_orders_1 = {
        'order_id': [1, 2, 3, 4],
        'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
        'com_id': [3, 4, 1, 1],
        'sales_id': [4, 5, 1, 4],
        'amount': [10000, 5000, 50000, 25000]
    }
    df_sp1 = pd.DataFrame(data_sales_person_1)
    df_c1 = pd.DataFrame(data_company_1)
    df_o1 = pd.DataFrame(data_orders_1)

    result_1 = sales_person(df_sp1, df_c1, df_o1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected: Amy, Mark, Alex

    # Test Case 2: No salesperson sold to RED
    data_sales_person_2 = {
        'sales_id': [10, 20],
        'name': ['Alice', 'Bob'],
        'salary': [70000, 80000],
        'commission_rate': [5, 10],
        'hire_date': ['3/1/2010', '6/1/2011']
    }
    data_company_2 = {
        'com_id': [11, 12],
        'name': ['RED', 'BLUE'],
        'city': ['Boston', 'Seattle']
    }
    data_orders_2 = {
        'order_id': [101, 102],
        'order_date': ['1/1/2020', '1/2/2020'],
        'com_id': [12, 12],  # None to com_id 11
        'sales_id': [10, 20],
        'amount': [3000, 4000]
    }
    df_sp2 = pd.DataFrame(data_sales_person_2)
    df_c2 = pd.DataFrame(data_company_2)
    df_o2 = pd.DataFrame(data_orders_2)

    result_2 = sales_person(df_sp2, df_c2, df_o2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Explanation: Nobody sold to RED => all salespersons remain.

    # Test Case 3: All sold to RED
    data_sales_person_3 = {
        'sales_id': [100, 200],
        'name': ['Charlie', 'Diane'],
        'salary': [90000, 85000],
        'commission_rate': [15, 20],
        'hire_date': ['5/1/2015', '8/1/2017']
    }
    data_company_3 = {
        'com_id': [101],
        'name': ['RED'],
        'city': ['Boston']
    }
    data_orders_3 = {
        'order_id': [1001, 1002],
        'order_date': ['6/1/2020', '6/2/2020'],
        'com_id': [101, 101],
        'sales_id': [100, 200],
        'amount': [10000, 20000]
    }
    df_sp3 = pd.DataFrame(data_sales_person_3)
    df_c3 = pd.DataFrame(data_company_3)
    df_o3 = pd.DataFrame(data_orders_3)

    result_3 = sales_person(df_sp3, df_c3, df_o3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Explanation: Everyone sold to RED => no one remains.

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(s + c + o), where
#   s = number of rows in sales_person
#   c = number of rows in company
#   o = number of rows in orders
# The main cost is in the merges/joins or isins, which are generally O(n).
# Space Complexity: O(s + c + o) for intermediate structures and final output.
