import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame 'animals' with columns:
    'name', 'species', 'age', 'weight'.
    It returns the 'name' column for those animals whose weight is
    strictly greater than 100, sorted by 'weight' in descending order.

    Parameters:
    animals (pd.DataFrame): A DataFrame of animal data.

    Returns:
    pd.DataFrame: A DataFrame containing a single column 'name' of
                  the animals that weigh over 100 kg, sorted by weight descending.
    """
    return animals.query("weight > 100").sort_values("weight", ascending=False)[["name"]]


if __name__ == "__main__":
    # Example usage
    data = {
        'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
        'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
        'age': [98, 50, 6, 45, 100, 26],
        'weight': [464, 41, 328, 463, 50, 349]
    }
    df_animals = pd.DataFrame(data)
    heavy_animals = findHeavyAnimals(df_animals)
    print(heavy_animals)

    # Expected output:
    #       name
    # 0   Tatiana
    # 3  Jonathan
    # 5     Tommy
    # 2      Alex

    # Test Case 1: No animal is heavier than 100
    test_data1 = {
        'name': ['Light1', 'Light2'],
        'species': ['Bird', 'Fox'],
        'age': [2, 4],
        'weight': [10, 30]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = findHeavyAnimals(df_test1)
    assert res1.empty, "Expected an empty DataFrame when no animal is heavier than 100."

    # Test Case 2: All animals heavier than 100
    test_data2 = {
        'name': ['HeavyA', 'HeavyB'],
        'species': ['Elephant', 'Rhino'],
        'age': [10, 20],
        'weight': [500, 600]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = findHeavyAnimals(df_test2)
    assert len(res2) == 2, "Expected 2 animals."
    assert list(res2['name']) == [
        'HeavyB', 'HeavyA'], "Should be sorted by weight descending."

    # Test Case 3: Mixed weights
    test_data3 = {
        'name': ['Mix1', 'Mix2', 'Mix3'],
        'species': ['Tiger', 'Lion', 'Zebra'],
        'age': [5, 12, 7],
        'weight': [120, 99, 150]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = findHeavyAnimals(df_test3)
    # We expect only Mix1 and Mix3 (both > 100), sorted by weight descending => Mix3 first
    assert list(res3['name']) == [
        'Mix3', 'Mix1'], "Only 'Mix3' and 'Mix1' should appear, in descending weight order."
    print("All test cases passed successfully!")


# Explanation:
# 1. We use a query to filter rows with weight > 100.
# 2. We sort the result by 'weight' in descending order.
# 3. We select only the 'name' column.

# Complexity Analysis
# Time Complexity: O(N log N) due to the sorting step, where N is the number of rows.
# Filtering is O(N), but sorting dominates, resulting in O(N log N).
# Space Complexity: O(N) for the filtered and sorted DataFrame.
