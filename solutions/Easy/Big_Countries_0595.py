import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a DataFrame 'world' with the following columns:
    - 'name' (str)
    - 'continent' (str)
    - 'area' (int)
    - 'population' (int)
    - 'gdp' (int or float)

    A country is considered "big" if it has an area >= 3,000,000 
    or a population >= 25,000,000.

    The function returns a DataFrame containing only the 'name', 'population',
    and 'area' columns for all "big" countries.
    """
    # Filter for big countries and select required columns
    big_countries_df = world.query("area >= 3000000 or population >= 25000000")[
        ["name", "population", "area"]]
    return big_countries_df


if __name__ == "__main__":
    # Example usage:
    data = {
        'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
        'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
        'area': [652230, 28748, 2381741, 468, 1246700],
        'population': [25500100, 2831741, 37100000, 78115, 20609294],
        'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
    }
    df_world = pd.DataFrame(data)
    result_df = big_countries(df_world)
    print(result_df)

    # Expected output:
    #            name  population     area
    # 0  Afghanistan    25500100   652230
    # 2      Algeria    37100000  2381741

    # Test Case 1: No countries meet the criteria
    test_data1 = {
        'name': ['SmallCountry1', 'SmallCountry2'],
        'continent': ['Asia', 'Europe'],
        'area': [50000, 100000],
        'population': [1000000, 2000000],
        'gdp': [5000000, 6000000]
    }
    df_test1 = pd.DataFrame(test_data1)
    res1 = big_countries(df_test1)
    assert res1.empty, "Expected no rows to be returned when no countries are big."

    # Test Case 2: All countries meet one of the criteria
    test_data2 = {
        'name': ['GiantLand', 'MegaCountry'],
        'continent': ['Asia', 'Africa'],
        'area': [4000000, 4500000],
        'population': [30000000, 50000000],
        'gdp': [100000000000, 200000000000]
    }
    df_test2 = pd.DataFrame(test_data2)
    res2 = big_countries(df_test2)
    assert len(res2) == 2, "Expected both rows to be returned."

    # Test Case 3: Mixed scenario
    test_data3 = {
        'name': ['CountryA', 'CountryB', 'CountryC'],
        'continent': ['ContinentX', 'ContinentY', 'ContinentZ'],
        'area': [3100000, 2500000, 1000000],
        'population': [24000000, 30000000, 5000000],
        'gdp': [10000000000, 20000000000, 30000000000]
    }
    df_test3 = pd.DataFrame(test_data3)
    res3 = big_countries(df_test3)
    # "CountryA" -> area >= 3000000, population < 25000000 => qualifies
    # "CountryB" -> area < 3000000, population >= 25000000 => qualifies
    # "CountryC" -> area < 3000000, population < 25000000 => does NOT qualify
    assert len(res3) == 2, "Expected exactly 2 countries to qualify."
    assert 'CountryC' not in res3['name'].values, "CountryC should not be in the result."

    print("All test cases passed successfully!")

# Explanation:
# 1. We use pandas' query to filter rows where area >= 3000000 or population >= 25000000.
# 2. We select only the columns 'name', 'population', and 'area'.

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the DataFrame, since we're iterating
# through all rows once for the filtering operation.
# Space Complexity: O(N), as we create a filtered subset of the DataFrame.
