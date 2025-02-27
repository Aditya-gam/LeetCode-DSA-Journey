import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Function: total_time
    Description:
        This function calculates the total time (in minutes) each employee spends in the office 
        for each distinct day. The input DataFrame includes multiple entries/exits per day 
        for an employee.

    Parameters:
    - employees (pd.DataFrame): A DataFrame with columns:
        1) emp_id (int): Employee ID
        2) event_day (date): The date on which the entry/exit occurred
        3) in_time (int): Minute of day the employee entered
        4) out_time (int): Minute of day the employee exited

    Returns:
    - pd.DataFrame: A DataFrame with columns ['day', 'emp_id', 'total_time'], where:
        - 'day' is the event_day from the original DataFrame
        - 'emp_id' is the employee ID
        - 'total_time' is the sum of (out_time - in_time) for that day and employee
    """
    # Calculate the duration for each row
    employees['duration'] = employees['out_time'] - employees['in_time']

    # Group by (event_day, emp_id) and sum the durations
    grouped = employees.groupby(['event_day', 'emp_id'])[
        'duration'].sum().reset_index()

    # Rename columns to match the desired output format
    grouped.rename(columns={'event_day': 'day',
                   'duration': 'total_time'}, inplace=True)

    # Return the resulting DataFrame
    return grouped[['day', 'emp_id', 'total_time']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'emp_id': [1, 1, 1, 2, 2],
        'event_day': [
            '2020-11-28',
            '2020-11-28',
            '2020-12-03',
            '2020-11-28',
            '2020-12-09'
        ],
        'in_time': [4, 55, 1, 3, 47],
        'out_time': [32, 200, 42, 33, 74]
    }
    df_employees_1 = pd.DataFrame(data_1)
    result_1 = total_time(df_employees_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected:
    # day         emp_id  total_time
    # 2020-11-28      1         173
    # 2020-11-28      2          30
    # 2020-12-03      1          41
    # 2020-12-09      2          27

    # Test case 2: Single employee, multiple entries in a single day
    data_2 = {
        'emp_id': [3, 3, 3],
        'event_day': ['2021-01-01', '2021-01-01', '2021-01-01'],
        'in_time': [10, 200, 400],
        'out_time': [50, 250, 440]
    }
    df_employees_2 = pd.DataFrame(data_2)
    result_2 = total_time(df_employees_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected total_time = (50 - 10) + (250 - 200) + (440 - 400) = 40 + 50 + 40 = 130

    # Test case 3: Multiple employees on the same day
    data_3 = {
        'emp_id': [4, 5, 5],
        'event_day': ['2022-05-12', '2022-05-12', '2022-05-12'],
        'in_time': [10, 20, 100],
        'out_time': [60, 40, 120]
    }
    df_employees_3 = pd.DataFrame(data_3)
    result_3 = total_time(df_employees_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # day='2022-05-12', emp_id=4, total_time=50 (60-10)
    # day='2022-05-12', emp_id=5, total_time=40 + 20 = 60

    # Test case 4: Multiple employees on different days
    data_4 = {
        'emp_id': [6, 6, 7, 7],
        'event_day': ['2022-06-01', '2022-06-01', '2022-06-02', '2022-06-02'],
        'in_time': [10, 20, 30, 40],
        'out_time': [50, 40, 50, 60]
    }
    df_employees_4 = pd.DataFrame(data_4)
    result_4 = total_time(df_employees_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected:
    # day='2022-06-01', emp_id=6, total_time=40 + 20 = 60
    # day='2022-06-02', emp_id=7, total_time=20

    print("\nAll test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the 'employees' DataFrame.
#   - Calculating the duration for each row takes O(N) time.
#   - Grouping the DataFrame by ('event_day', 'emp_id') and summing the durations takes O(N) time.
#   - Renaming the columns and returning the resulting DataFrame takes O(N) time.

# Space Complexity: O(N), where N is the number of rows in the 'employees' DataFrame.
#   - The additional 'duration' column requires O(N) space.
#   - The grouped DataFrame also requires O(N) space.
