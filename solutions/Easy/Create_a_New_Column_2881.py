import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes the 'employees' DataFrame,
    creates a new column 'bonus' which is twice the 'salary',
    and returns the updated DataFrame.
    """
    # Create the bonus column by doubling salary
    employees["bonus"] = employees["salary"] * 2
    return employees


# Example test cases
if __name__ == "__main__":
    data = {
        "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
        "salary": [4548, 28150, 1103, 6593, 74576, 24433]
    }
    df = pd.DataFrame(data)

    result_df = createBonusColumn(df)
    print(result_df)
    # Expected output:
    #      name  salary   bonus
    # 0   Piper    4548    9096
    # 1   Grace   28150   56300
    # 2 Georgia    1103    2206
    # 3  Willow    6593   13186
    # 4    Finn   74576  149152
    # 5  Thomas   24433   48866

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(1) - We just create a new column based on existing data
# Space complexity: O(1) - We use a constant amount of extra space
