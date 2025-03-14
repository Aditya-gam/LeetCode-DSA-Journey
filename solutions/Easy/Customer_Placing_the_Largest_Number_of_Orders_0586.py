import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the customer(s) who placed the highest number of orders.

    Parameters:
    - orders (pd.DataFrame): Must have columns ['order_number', 'customer_number'].

    Returns:
    - pd.DataFrame with one column ['customer_number'], containing the customer(s)
      who placed the most orders.
    """
    # Group by customer_number and count the orders
    order_counts = orders.groupby('customer_number')[
        'order_number'].count().reset_index(name='order_count')

    # Determine the maximum order count
    max_orders = order_counts['order_count'].max()

    # Filter customers who have the maximum order count
    top_customers = order_counts.loc[order_counts['order_count'] == max_orders, [
        'customer_number']]

    return top_customers


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Basic Example
    # Customer 3 has 2 orders, customers 1 and 2 each have 1
    data_1 = {
        'order_number': [1, 2, 3, 4],
        'customer_number': [1, 2, 3, 3]
    }
    df_orders_1 = pd.DataFrame(data_1)
    result_1 = largest_orders(df_orders_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected: customer_number = 3

    # Test Case 2: Multiple Top Customers
    # Each of customers 5, 6, 7 has 2 orders
    data_2 = {
        'order_number': [10, 11, 12, 13, 14, 15],
        'customer_number': [5, 6, 5, 7, 6, 7]
    }
    df_orders_2 = pd.DataFrame(data_2)
    result_2 = largest_orders(df_orders_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Expected: customer_number in [5, 6, 7]

    # Test Case 3: Single Customer
    data_3 = {
        'order_number': [100, 101, 102],
        'customer_number': [9, 9, 9]
    }
    df_orders_3 = pd.DataFrame(data_3)
    result_3 = largest_orders(df_orders_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Expected: customer_number = 9

    # Test Case 4: Empty DataFrame
    df_orders_4 = pd.DataFrame(columns=['order_number', 'customer_number'])
    result_4 = largest_orders(df_orders_4)
    print("\nTest Case 4 Result:")
    print(result_4)
    # Expected: Empty DataFrame

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n), where n is the number of rows in the orders DataFrame.
#                 Grouping and counting are generally O(n).
# Space Complexity: O(n) for storing grouped data and the final result.
#                  The space complexity can be reduced to O(1) if we only need to return the customer number(s).
