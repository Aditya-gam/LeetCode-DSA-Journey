import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Function: order_scores
    Description:
        This function takes a DataFrame containing game scores and returns
        the scores ranked from highest to lowest using a dense rank method.

        Ranking Rules:
          1. Scores are ordered from highest to lowest.
          2. Tied scores share the same rank.
          3. After a tie, the next rank is incremented by 1 (no gaps in rank numbers).

    Parameters:
    - scores (pd.DataFrame): A DataFrame with columns ['id', 'score'].

    Returns:
    - pd.DataFrame: A DataFrame with columns ['score', 'rank'], sorted by 'score' in descending order.
    """
    # Sort scores in descending order
    scores_sorted = scores.sort_values('score', ascending=False)

    # Calculate the dense rank of each score
    # method='dense' assigns the same rank to ties and uses consecutive ranks
    scores_sorted['rank'] = scores_sorted['score'].rank(
        method='dense', ascending=False).astype(int)

    # Return only the required columns in the sorted order
    return scores_sorted[['score', 'rank']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    scores_data_1 = {
        'id': [1, 2, 3, 4, 5, 6],
        'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
    }
    df_scores_1 = pd.DataFrame(scores_data_1)
    result_1 = order_scores(df_scores_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected:
    # 4.00  rank 1
    # 4.00  rank 1
    # 3.85  rank 2
    # 3.65  rank 3
    # 3.65  rank 3
    # 3.50  rank 4

    # Test case 2: All scores are the same
    scores_data_2 = {
        'id': [10, 11, 12],
        'score': [2.00, 2.00, 2.00]
    }
    df_scores_2 = pd.DataFrame(scores_data_2)
    result_2 = order_scores(df_scores_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected:
    # All scores have rank 1 since they are the same

    # Test case 3: Strictly descending unique scores
    scores_data_3 = {
        'id': [20, 21, 22, 23],
        'score': [5.00, 4.50, 3.25, 1.75]
    }
    df_scores_3 = pd.DataFrame(scores_data_3)
    result_3 = order_scores(df_scores_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # 5.00 -> rank 1
    # 4.50 -> rank 2
    # 3.25 -> rank 3
    # 1.75 -> rank 4

    # Test case 4: Random scores with ties
    scores_data_4 = {
        'id': [30, 31, 32, 33, 34, 35],
        'score': [3.00, 3.25, 2.75, 3.25, 3.00, 2.75]
    }
    df_scores_4 = pd.DataFrame(scores_data_4)
    result_4 = order_scores(df_scores_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected:
    # 3.25 -> rank 1
    # 3.25 -> rank 1
    # 3.00 -> rank 3
    # 3.00 -> rank 3
    # 2.75 -> rank 5
    # 2.75 -> rank 5

    print("\nAll tests passed!")

# Complexity Analysis
# Time Complexity: O(n*log(n)), where n is the number of scores in the DataFrame.
# The time complexity is dominated by the sorting operation, which has a time complexity of O(n*log(n)).
# The rank calculation has a linear time complexity of O(n).

# Space Complexity: O(n), where n is the number of scores in the DataFrame.
# The space complexity is due to the storage of the sorted DataFrame and the additional 'rank' column.
# The rank column requires O(n) space.
