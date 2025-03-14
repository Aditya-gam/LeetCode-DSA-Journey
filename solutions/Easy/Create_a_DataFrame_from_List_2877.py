import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """
    This function takes a 2D list `student_data`, where each sub-list contains
    [student_id, age], and returns a pandas DataFrame with the same order
    and two columns: 'student_id' and 'age'.
    """
    # Create the DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=["student_id", "age"])

    return df


# Example test cases
if __name__ == "__main__":
    # Test case 1
    student_data1 = [[1, 20], [2, 21], [3, 22]]
    df1 = createDataframe(student_data1)
    assert df1.equals(pd.DataFrame(
        student_data1, columns=["student_id", "age"]))

    # Test case 2
    student_data2 = [[4, 23], [5, 24], [6, 25]]
    df2 = createDataframe(student_data2)
    assert df2.equals(pd.DataFrame(
        student_data2, columns=["student_id", "age"]))

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the number of rows in the input 2D list.
# Space Complexity: O(n), where n is the number of rows in the input 2D list.
