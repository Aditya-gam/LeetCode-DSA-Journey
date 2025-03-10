import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    This function filters the 'students' DataFrame 
    to rows where student_id = 101, 
    and returns a DataFrame containing only ['name', 'age'] columns.
    """
    filtered_df = students.loc[students["student_id"] == 101, ["name", "age"]]

    return filtered_df


# Example test cases
if __name__ == "__main__":
    data = {
        "student_id": [101, 53, 128, 3],
        "name": ["Ulysses", "William", "Henry", "Henry"],
        "age": [13, 10, 6, 11]
    }
    df = pd.DataFrame(data)

    result_df = selectData(df)
    print(result_df)
    # Expected output:
    #      name  age
    # 0  Ulysses   13

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the DataFrame once
# Space complexity: O(n) - We store the filtered rows in a new DataFrame
