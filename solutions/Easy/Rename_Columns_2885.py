import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames the columns of the 'students' DataFrame as follows:
    - 'id' to 'student_id'
    - 'first' to 'first_name'
    - 'last' to 'last_name'
    - 'age' to 'age_in_years'

    Returns the updated DataFrame.
    """
    # Rename columns using the rename method
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })

    return students


# Example usage
if __name__ == "__main__":
    # Sample data to illustrate the column renaming
    data = {
        'id': [1, 2, 3, 4, 5],
        'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
        'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
        'age': [6, 7, 16, 18, 10]
    }
    df = pd.DataFrame(data)
    renamed_df = renameColumns(df)
    print(renamed_df)
    # Expected output:
    #    student_id first_name  last_name  age_in_years
    # 0           1      Mason       King             6
    # 1           2        Ava     Wright             7
    # 2           3     Taylor       Hall            16
    # 3           4    Georgia   Thompson            18
    # 4           5     Thomas      Moore            10

# The function 'renameColumns' takes a DataFrame 'students' as input and renames the columns as specified.
# The 'rename' method is used to rename the columns in the DataFrame.
# The function returns the updated DataFrame with the renamed columns.
# Example usage demonstrates how the function works with sample data.
# The output shows the DataFrame with the columns renamed as expected.

# Complexity Analysis
# The time complexity of this function is O(1) since the number of columns to rename is fixed.
# The space complexity is also O(1) as the function uses a constant amount of memory.
