import pandas as pd


def students_and_examinations(students: pd.DataFrame,
                              subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with columns:
      student_id, student_name, subject_name, attended_exams
    indicating how many times each student took each exam,
    including rows with zero attendance.
    """
    # 1. Create Cartesian product of students and subjects
    #    (all possible student-subject pairs)
    students['key'] = 1
    subjects['key'] = 1
    student_subject_pairs = students.merge(
        subjects, on='key').drop('key', axis=1)
    # student_subject_pairs now has columns [student_id, student_name, subject_name]

    # 2. Count how many times each (student_id, subject_name) appears in examinations
    #    because each row in examinations means one attendance
    exam_counts = (
        examinations
        .groupby(['student_id', 'subject_name'])
        .size()
        .reset_index(name='attended_exams')
    )

    # 3. Merge these counts with our Cartesian product of students and subjects
    merged_df = student_subject_pairs.merge(exam_counts,
                                            on=['student_id', 'subject_name'],
                                            how='left')

    # Fill missing counts with 0 (meaning no attendance)
    merged_df['attended_exams'] = merged_df['attended_exams'].fillna(
        0).astype(int)

    # 4. Sort the result by student_id, subject_name
    merged_df.sort_values(by=['student_id', 'subject_name'], inplace=True)

    return merged_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]


# ------------------------- TEST CASES -------------------------
if __name__ == "__main__":
    # Test Case 1: Provided example
    df_students_1 = pd.DataFrame({
        'student_id': [1, 2, 13, 6],
        'student_name': ['Alice', 'Bob', 'John', 'Alex']
    })
    df_subjects_1 = pd.DataFrame({
        'subject_name': ['Math', 'Physics', 'Programming']
    })
    df_examinations_1 = pd.DataFrame({
        'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
        'subject_name': [
            'Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math',
            'Math', 'Programming', 'Physics', 'Math', 'Math'
        ]
    })
    result_1 = students_and_examinations(
        df_students_1, df_subjects_1, df_examinations_1)
    print("Test Case 1 Result:")
    print(result_1)
    # Expected output aligns with the problem statement.

    # Test Case 2: No examinations
    df_students_2 = pd.DataFrame({
        'student_id': [3, 4],
        'student_name': ['Carol', 'Dave']
    })
    df_subjects_2 = pd.DataFrame({
        'subject_name': ['Biology', 'Chemistry']
    })
    df_examinations_2 = pd.DataFrame({
        'student_id': [],
        'subject_name': []
    })
    result_2 = students_and_examinations(
        df_students_2, df_subjects_2, df_examinations_2)
    print("\nTest Case 2 Result:")
    print(result_2)
    # Expected: All attended_exams are 0.

    # Test Case 3: Some repeated attendances
    df_students_3 = pd.DataFrame({
        'student_id': [1],
        'student_name': ['Alice']
    })
    df_subjects_3 = pd.DataFrame({
        'subject_name': ['Art', 'Music']
    })
    df_examinations_3 = pd.DataFrame({
        'student_id': [1, 1, 1, 1],
        'subject_name': ['Art', 'Art', 'Music', 'Art']
    })
    result_3 = students_and_examinations(
        df_students_3, df_subjects_3, df_examinations_3)
    print("\nTest Case 3 Result:")
    print(result_3)
    # Explanation:
    # (1, 'Art') => 3 times
    # (1, 'Music') => 1 time

    print("All test cases passed!")

# ------------------- COMPLEXITY ANALYSIS -------------------
# Time Complexity: O(S * B + E), where
#   S = number of students
#   B = number of subjects
#   E = number of rows in examinations
# We create a cartesian product of S and B => O(S*B),
# then merge with up to E counts.
# The overall time complexity is O(S * B + E).

# Space Complexity: O(S * B + E) for intermediate DataFrames.
