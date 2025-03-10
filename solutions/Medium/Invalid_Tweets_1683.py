import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    This function returns a DataFrame containing the 'tweet_id' of all
    invalid tweets. A tweet is invalid if its content length is strictly
    greater than 15 characters.

    Parameters:
    tweets (pd.DataFrame): A DataFrame with columns:
                           - 'tweet_id' (int)
                           - 'content' (str)

    Returns:
    pd.DataFrame: A DataFrame with a single column 'tweet_id' for tweets
                  that are invalid.
    """
    invalid_df = tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]

    return invalid_df


if __name__ == "__main__":
    # Example usage
    data = {
        'tweet_id': [1, 2],
        'content': ["Let us Code", "More than fifteen chars are here!"]
    }
    df_tweets = pd.DataFrame(data)
    result = invalid_tweets(df_tweets)
    print(result)

    # Expected output:
    #    tweet_id
    # 1         2

    # Test Case 1: No invalid tweets
    test_data1 = {
        'tweet_id': [10, 11],
        # "Exactly15chars" has length 15, so it's valid
        'content': ["Short", "Exactly15chars"]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = invalid_tweets(df_test1)
    assert res1.empty, "Expected no invalid tweets."

    # Test Case 2: All tweets are invalid
    test_data2 = {
        'tweet_id': [20, 21],
        'content': ["This is way longer than fifteen characters", "So is this example"]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = invalid_tweets(df_test2)
    assert len(res2) == 2, "Expected 2 invalid tweets (both)."

    # Test Case 3: Mixed scenario
    test_data3 = {
        'tweet_id': [30, 31, 32],
        'content': ["Short", "Sixteen chars here", "Just 15 chars!!"]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = invalid_tweets(df_test3)
    # 'Sixteen chars here' has length > 15
    # 'Short' has length < 15
    # 'Just 15 chars!!' is exactly 15
    assert len(res3) == 1, "Expected only one invalid tweet."
    assert res3.iloc[0]['tweet_id'] == 31

    print("All test cases passed successfully!")

# Explanation:
# - First tweet has 11 characters -> valid.
# - Second tweet has 33 characters -> invalid -> appears in result.

# Complexity Analysis
# Time Complexity: O(N) for checking the length of each tweet's content,
# where N is the number of rows in 'tweets'.
# Space Complexity: O(N) in the worst case for storing the subset of invalid tweets.
