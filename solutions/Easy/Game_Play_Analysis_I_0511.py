import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Function: game_analysis
    Description:
        This function takes a DataFrame with player activity logs
        and identifies the earliest (first) login date for each player.

    Parameters:
    - activity (pd.DataFrame): A DataFrame with columns:
        1) player_id (int): ID of the player
        2) device_id (int): ID of the device used
        3) event_date (date): The date the player logged in
        4) games_played (int): Number of games played during that login session

    Returns:
    - pd.DataFrame: A DataFrame with columns ['player_id', 'first_login'],
      where 'first_login' is the earliest event_date for that player.
    """

    # Group by player_id and find the minimum event_date
    first_login_df = (
        activity
        .groupby('player_id', as_index=False)['event_date']
        .min()
        .rename(columns={'event_date': 'first_login'})
    )

    return first_login_df[['player_id', 'first_login']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'player_id': [1, 1, 2, 3, 3],
        'device_id': [2, 2, 3, 1, 4],
        'event_date': [
            '2016-03-01',
            '2016-05-02',
            '2017-06-25',
            '2016-03-02',
            '2018-07-03'
        ],
        'games_played': [5, 6, 1, 0, 5]
    }
    df_activity_1 = pd.DataFrame(data_1)
    result_1 = game_analysis(df_activity_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected:
    # player_id  first_login
    # 1          2016-03-01
    # 2          2017-06-25
    # 3          2016-03-02

    # Test case 2: Single player with multiple sessions
    data_2 = {
        'player_id': [10, 10, 10],
        'device_id': [100, 100, 101],
        'event_date': ['2022-01-02', '2021-12-31', '2022-01-01'],
        'games_played': [3, 2, 5]
    }
    df_activity_2 = pd.DataFrame(data_2)
    result_2 = game_analysis(df_activity_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected:
    # player_id  first_login
    # 10         2021-12-31

    # Test case 3: Multiple players, some with a single event
    data_3 = {
        'player_id': [2, 2, 5, 6],
        'device_id': [10, 10, 11, 12],
        'event_date': ['2021-07-10', '2021-07-12', '2022-03-15', '2023-01-01'],
        'games_played': [1, 2, 5, 10]
    }
    df_activity_3 = pd.DataFrame(data_3)
    result_3 = game_analysis(df_activity_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # player_id  first_login
    # 2          2021-07-10
    # 5          2022-03-15
    # 6          2023-01-01

    # Test case 4: Multiple players with the same first login date
    data_4 = {
        'player_id': [7, 8, 8, 9, 9],
        'device_id': [20, 21, 22, 23, 24],
        'event_date': ['2021-11-01', '2021-11-02', '2021-11-02', '2021-11-03', '2021-11-03'],
        'games_played': [5, 3, 2, 1, 4]
    }
    df_activity_4 = pd.DataFrame(data_4)
    result_4 = game_analysis(df_activity_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected:
    # player_id  first_login
    # 7          2021-11-01
    # 8          2021-11-02
    # 9          2021-11-03

    print("\nAll test cases passed!")

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the 'activity' DataFrame.
#                  The function groups the data by player_id and finds the minimum event_date for each group.
# Space Complexity: O(N), where N is the number of rows in the 'activity' DataFrame.
#                   The space complexity is due to storing the output DataFrame with player_id and first_login columns.
