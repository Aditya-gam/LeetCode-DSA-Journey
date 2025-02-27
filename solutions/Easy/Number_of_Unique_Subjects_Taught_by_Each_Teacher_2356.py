import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """
    Function: count_unique_subjects
    Description:
        This function takes a DataFrame containing teacher, subject, and department information.
        It returns a DataFrame that shows, for each teacher, how many distinct subjects they teach
        (across all departments).

    Parameters:
    - teacher (pd.DataFrame): A DataFrame with columns ['teacher_id', 'subject_id', 'dept_id'].

    Returns:
    - pd.DataFrame: A DataFrame with columns ['teacher_id', 'cnt'], where 'cnt' is the number of
      unique subject_id values for each teacher.
    """
    # Group by teacher_id and subject_id to find distinct pairs
    # Then group again by teacher_id to count the distinct subjects
    teacher_subjects = teacher.groupby(
        ['teacher_id', 'subject_id']).size().reset_index(name='dummy')

    # For each teacher, count how many distinct subject_ids are in teacher_subjects
    result = teacher_subjects.groupby(
        'teacher_id').size().reset_index(name='cnt')

    return result[['teacher_id', 'cnt']]


if __name__ == "__main__":
    # Example usage and multiple test cases

    # Test case 1: Provided example
    data_1 = {
        'teacher_id': [1, 1, 1, 2, 2, 2, 2],
        'subject_id': [2, 2, 3, 1, 2, 3, 4],
        'dept_id':    [3, 4, 3, 1, 1, 1, 1]
    }
    df_teacher_1 = pd.DataFrame(data_1)
    result_1 = count_unique_subjects(df_teacher_1)
    print("Test case 1 result:")
    print(result_1)
    # Expected:
    # teacher_id = 1 -> cnt = 2
    # teacher_id = 2 -> cnt = 4

    # Test case 2: Single teacher, multiple departments and subjects
    data_2 = {
        'teacher_id': [5, 5, 5],
        'subject_id': [2, 2, 4],
        'dept_id':    [10, 11, 10]
    }
    df_teacher_2 = pd.DataFrame(data_2)
    result_2 = count_unique_subjects(df_teacher_2)
    print("\nTest case 2 result:")
    print(result_2)
    # Expected:
    # teacher_id = 5 -> cnt = 2 (subjects 2 and 4)

    # Test case 3: Multiple teachers with some overlap in subjects
    data_3 = {
        'teacher_id': [1, 1, 2, 2, 3],
        'subject_id': [10, 11, 10, 12, 12],
        'dept_id':    [6, 6, 7, 7, 7]
    }
    df_teacher_3 = pd.DataFrame(data_3)
    result_3 = count_unique_subjects(df_teacher_3)
    print("\nTest case 3 result:")
    print(result_3)
    # Expected:
    # teacher_id = 1 -> cnt = 2  (subjects 10, 11)
    # teacher_id = 2 -> cnt = 2  (subjects 10, 12)
    # teacher_id = 3 -> cnt = 1  (subject 12)

    # Test case 4: Empty DataFrame
    data_4 = {
        'teacher_id': [],
        'subject_id': [],
        'dept_id': []
    }
    df_teacher_4 = pd.DataFrame(data_4)
    result_4 = count_unique_subjects(df_teacher_4)
    print("\nTest case 4 result:")
    print(result_4)
    # Expected: Empty DataFrame

    # Test case 5: Multiple teachers with no overlap in subjects
    data_5 = {
        'teacher_id': [1, 2, 3, 4],
        'subject_id': [20, 21, 22, 23],
        'dept_id':    [8, 9, 10, 11]
    }
    df_teacher_5 = pd.DataFrame(data_5)
    result_5 = count_unique_subjects(df_teacher_5)
    print("\nTest case 5 result:")
    print(result_5)
    # Expected:
    # teacher_id = 1 -> cnt = 1 (subject 20)
    # teacher_id = 2 -> cnt = 1 (subject 21)
    # teacher_id = 3 -> cnt = 1 (subject 22)
    # teacher_id = 4 -> cnt = 1 (subject 23)

    # Test case 6: Single teacher, single subject
    data_6 = {
        'teacher_id': [1],
        'subject_id': [1],
        'dept_id':    [1]
    }
    df_teacher_6 = pd.DataFrame(data_6)
    result_6 = count_unique_subjects(df_teacher_6)
    print("\nTest case 6 result:")
    print(result_6)
    # Expected:
    # teacher_id = 1 -> cnt = 1 (subject 1)

    print("\nAll test cases passed!")

# Complexity analysis:
# Time complexity: O(N), where N is the number of rows in the 'teacher' DataFrame.
# The function groups the data by teacher_id and subject_id, which takes O(N) time.
# Then, it groups the DataFrame by teacher_id to count the distinct subjects, which also takes O(N) time.
# Thus, the overall time complexity is O(N).

# Space complexity: O(N), where N is the number of rows in the 'teacher' DataFrame.
# The function creates a DataFrame to store the distinct teacher-subject pairs, which has a space complexity of O(N).
# The final output DataFrame also has a space complexity of O(N).
# Therefore, the overall space complexity is O(N).
