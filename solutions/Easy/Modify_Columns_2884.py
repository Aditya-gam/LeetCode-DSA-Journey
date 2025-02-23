import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    This function doubles the 'salary' column of the employees DataFrame in-place
    and returns the updated DataFrame.
    """
    employees["salary"] = employees["salary"] * 2

    return employees


if __name__ == "__main__":
    data = {
        "name": ["Jack", "Piper", "Mia", "Ulysses"],
        "salary": [19666, 74754, 62509, 54866]
    }
    df = pd.DataFrame(data)

    # Modify the salary column by doubling each salary
    result_df = modifySalaryColumn(df)
    print(result_df)
    # Expected:
    #      name  salary
    # 0    Jack   39332
    # 1   Piper  149508
    # 2     Mia  125018
    # 3 Ulysses  109732

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate over the DataFrame once.
# Space complexity: O(1) - We use a constant amount of extra space.
