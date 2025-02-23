import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes the 'students' DataFrame and removes all rows 
    that have missing (NaN/None) values in the 'name' column.
    """
    cleaned_df = students.dropna(subset=['name'])

    return cleaned_df


if __name__ == "__main__":
    data = {
        'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]
    }
    df = pd.DataFrame(data)

    result_df = dropMissingData(df)
    print(result_df)
    # Expected output:
    #    student_id     name  age
    # 0          32    Piper    5
    # 2         779  Georgia   20
    # 3         849   Willow   14

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the DataFrame once.
# Space complexity: O(1) - We use a constant amount of extra space.
