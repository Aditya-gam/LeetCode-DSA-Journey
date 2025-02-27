import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """
    Function: find_classes
    Description:
        This function takes a DataFrame representing student enrollments in various classes.
        Each row has two columns: 'student' and 'class'. The function returns a DataFrame
        listing only those classes that have at least five enrolled students.

    Parameters:
    - courses (pd.DataFrame): A DataFrame with columns ['student', 'class'].

    Returns:
    - pd.DataFrame: A DataFrame with a single column ['class'].
      Contains only the classes that have 5 or more students.
    """
    # Group by 'class' and count the number of distinct students
    class_counts = (
        courses
        .groupby('class')['student']
        .nunique()
        .reset_index(name='student_count')
    )

    # Filter classes with at least 5 students
    result_df = class_counts.loc[class_counts['student_count'] >= 5, ['class']]

    return result_df


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'class':   ['Math', 'English', 'Math', 'Biology', 'Math',
                    'Computer', 'Math', 'Math', 'Math']
    }
    df_courses_1 = pd.DataFrame(data_1)
    result_1 = find_classes(df_courses_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected output: 'Math'

    # Test case 2: All classes have fewer than 5 students
    data_2 = {
        'student': ['A', 'B', 'C', 'D'],
        'class':   ['Math', 'English', 'Biology', 'Computer']
    }
    df_courses_2 = pd.DataFrame(data_2)
    result_2 = find_classes(df_courses_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected: Empty DataFrame (no classes with >= 5 students)

    # Test case 3: Multiple classes with enough students
    data_3 = {
        'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
        'class': [
            'Algebra', 'Algebra', 'Algebra', 'Calculus', 'Algebra', 'Calculus',
            'Physics', 'Physics', 'Physics', 'Physics', 'Physics', 'Calculus'
        ]
    }
    df_courses_3 = pd.DataFrame(data_3)
    result_3 = find_classes(df_courses_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # Algebra has 3 students
    # Calculus has 3 students
    # Physics has 5 students
    # So only 'Physics' should appear

    # Test case 4: Multiple classes with some having 5 students
    data_4 = {
        'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'class': ['Math', 'English', 'Math', 'Biology', 'Math',
                  'Computer', 'Math', 'Math', 'Math', 'Computer']
    }
    df_courses_4 = pd.DataFrame(data_4)
    result_4 = find_classes(df_courses_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected: 'Math' and 'Computer' should appear
    # 'Math' has 6 students, 'Computer' has 2 students
    # So only 'Math' should appear

# Complexity Analysis
# Time Complexity: O(N), where N is the number of rows in the 'courses' DataFrame.
# The function groups the DataFrame by 'class' and counts the number of unique students in each class,
# which takes O(N) time. The final DataFrame is created by filtering classes with at least 5 students,
# which also takes O(N) time.
# Thus, the overall time complexity is O(N).

# Space Complexity: O(N), where N is the number of rows in the 'courses' DataFrame.
# The function creates a DataFrame to store the class counts, which has a space complexity of O(N).
# The final output DataFrame also has a space complexity of O(N).
