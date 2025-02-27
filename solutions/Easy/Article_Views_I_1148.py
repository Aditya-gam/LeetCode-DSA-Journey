import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """
    This function returns a DataFrame of authors (in ascending order by id)
    who viewed at least one of their own articles. 
    The output has a single column named 'id'.

    Parameters:
    views (pd.DataFrame): A DataFrame with columns 'article_id', 'author_id', 'viewer_id', and 'view_date'.

    Returns:
    pd.DataFrame: A DataFrame with a single column 'id', listing authors who viewed their own articles.
    """
    # Filter rows where author_id == viewer_id
    same_person_df = views[views['author_id'] == views['viewer_id']]

    # Get unique author_id, sort them, then rename to "id"
    result_df = (
        same_person_df['author_id']
        .drop_duplicates()
        .sort_values()
        .to_frame(name='id')
        .reset_index(drop=True)
    )

    return result_df


if __name__ == "__main__":
    # Example usage:
    data = {
        'article_id': [1, 1, 2, 2, 4, 3, 3],
        'author_id':  [3, 3, 7, 7, 7, 4, 4],
        'viewer_id':  [5, 6, 7, 6, 1, 4, 4],
        'view_date':  [
            '2019-08-01', '2019-08-02', '2019-08-01',
            '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21'
        ]
    }
    df_views = pd.DataFrame(data)
    result = article_views(df_views)
    print(result)

    # Expected output:
    #    id
    # 0   4
    # 1   7

    # Test Case 1: No one views their own articles
    test_data1 = {
        'article_id': [1, 2],
        'author_id': [10, 20],
        'viewer_id': [30, 40],
        'view_date': ['2021-01-01', '2021-01-02']
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = article_views(df_test1)
    assert res1.empty, "Expected no authors who viewed their own articles."

    # Test Case 2: Everyone views their own articles
    test_data2 = {
        'article_id': [3, 4],
        'author_id': [5, 6],
        'viewer_id': [5, 6],
        'view_date': ['2021-01-03', '2021-01-04']
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = article_views(df_test2)
    # Both authors 5 and 6 should appear
    assert len(res2) == 2
    assert list(res2['id']) == [5, 6]

    # Test Case 3: Mixed
    test_data3 = {
        'article_id': [10, 10, 11],
        'author_id': [1, 2, 3],
        'viewer_id': [1, 4, 5],
        'view_date': ['2022-05-01', '2022-05-02', '2022-05-03']
    }
    # Here only author 1 viewed their own article
    df_test3 = pd.DataFrame(test_data3)
    res3 = article_views(df_test3)
    assert len(res3) == 1
    assert res3.iloc[0]['id'] == 1

    print("All test cases passed successfully!")

# Explanation:
# - Row with author_id=7, viewer_id=7 indicates that author 7 viewed their own article.
# - Rows with author_id=4, viewer_id=4 show that author 4 viewed their own article as well.
# - Authors 4 and 7 are returned in ascending order by 'id'.

# Complexity Analysis
# Time Complexity: O(N) to filter and extract unique values from the DataFrame,
# where N is the number of rows.
# Space Complexity: O(N) in the worst case for storing the filtered DataFrame subset.
