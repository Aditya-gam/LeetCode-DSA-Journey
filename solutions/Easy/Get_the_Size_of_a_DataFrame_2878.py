import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    This function takes the 'players' DataFrame and returns 
    its shape as [number_of_rows, number_of_columns].
    """
    rows, cols = players.shape  # shape returns (rows, columns)

    return [rows, cols]


# Example test cases
if __name__ == "__main__":
    # Test case 1
    players1 = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
    })
    assert getDataframeSize(players1) == [3, 2]

    # Test case 2
    players2 = pd.DataFrame({
        "Name": ["David", "Eve", "Frank"],
        "Age": [40, 45, 50],
        "Score": [60, 70, 80]
    })
    assert getDataframeSize(players2) == [3, 3]

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(1).
# Space Complexity: O(1).
