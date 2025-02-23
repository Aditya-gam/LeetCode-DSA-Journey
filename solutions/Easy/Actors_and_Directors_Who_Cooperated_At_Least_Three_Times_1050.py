import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """
    Finds (actor_id, director_id) pairs that have cooperated at least three times.
    """
    # Group by actor_id and director_id, counting occurrences
    cooperation_count = (
        actor_director
        .groupby(['actor_id', 'director_id'], as_index=False)
        .size()
        .rename(columns={'size': 'cooperation_count'})
    )

    # Filter pairs with at least three cooperations
    result_df = cooperation_count.loc[cooperation_count['cooperation_count'] >= 3, [
        'actor_id', 'director_id']]

    return result_df


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Provided example
    data_1 = {
        'actor_id':    [1, 1, 1, 1, 1, 2, 2],
        'director_id': [1, 1, 1, 2, 2, 1, 1],
        'timestamp':   [0, 1, 2, 3, 4, 5, 6]
    }
    df_ad_1 = pd.DataFrame(data_1)
    result_1 = actors_and_directors(df_ad_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected: (1, 1) with exactly 3 cooperations

    # Test Case 2: Multiple pairs each with different counts
    data_2 = {
        'actor_id':    [1, 1, 2, 2, 3, 3, 3, 3],
        'director_id': [1, 1, 1, 3, 2, 2, 2, 1],
        'timestamp':   [10, 11, 12, 13, 14, 15, 16, 17]
    }
    df_ad_2 = pd.DataFrame(data_2)
    result_2 = actors_and_directors(df_ad_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Analysis:
    # (1,1) => 2 times
    # (2,1) => 1 time
    # (2,3) => 1 time
    # (3,2) => 3 times
    # (3,1) => 1 time
    # Only (3,2) appears 3 times

    # Test Case 3: Edge case with single row
    data_3 = {
        'actor_id': [5],
        'director_id': [5],
        'timestamp': [0]
    }
    df_ad_3 = pd.DataFrame(data_3)
    result_3 = actors_and_directors(df_ad_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Expected: Empty, because there's only 1 cooperation

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(n), where n is the number of rows in actor_director.
#                  Grouping and counting are typically O(n).
# Space Complexity: O(n), for the intermediate grouped data and final result.
