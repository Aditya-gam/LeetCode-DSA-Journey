import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    This function converts the 'grade' column in the 'students' DataFrame
    from float to integer type and returns the updated DataFrame.
    """
    # Convert the 'grade' column from float to int
    students["grade"] = students["grade"].astype(int)
    return students


# Example usage
if __name__ == "__main__":
    # Example DataFrame
    data = {
        "student_id": [1, 2],
        "name": ["Ava", "Kate"],
        "age": [6, 15],
        "grade": [73.0, 87.0]
    }
    df = pd.DataFrame(data)
    updated_df = changeDatatype(df)
    print(updated_df)
    # Expected output:
    #    student_id  name  age  grade
    # 0           1   Ava    6     73
    # 1           2  Kate   15     87

# The function 'changeDatatype' takes a DataFrame 'students' as input and converts the 'grade' column from float to integer type.
# The 'astype' method is used to change the data type of the 'grade' column.
# The function returns the updated DataFrame with the 'grade' column converted to integer type.
# Example usage demonstrates how the function works with sample data.
# The output shows the DataFrame with the 'grade' column converted to integer type as expected.

# Complexity Analysis
# The time complexity of this function is O(1) since the operation is performed on a single column.
# The space complexity is also O(1) as the function uses a constant amount of memory.
