import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the patients DataFrame to return only those patients who have a condition 
    starting with 'DIAB1', indicating Type I Diabetes.

    The 'conditions' column may contain multiple codes separated by spaces. 
    A valid condition for Type I Diabetes should start with 'DIAB1' either at the 
    beginning of the string or immediately after a whitespace.

    Parameters:
        patients (pd.DataFrame): DataFrame with columns 'patient_id', 'patient_name', and 'conditions'.

    Returns:
        pd.DataFrame: Filtered DataFrame containing only patients with a condition starting with 'DIAB1'.
    """
    # Use regex with a non-capturing group to ensure 'DIAB1' is either at the start of the string or follows a whitespace.
    filtered_patients = patients[patients['conditions'].str.contains(
        r'(?:^|\s)DIAB1', na=False)]

    return filtered_patients


if __name__ == "__main__":
    # Example usage
    data = {
        'patient_id': [1, 2, 3, 4, 5],
        'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
        'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
    }
    df_patients = pd.DataFrame(data)
    result_df = find_patients(df_patients)
    print(result_df)

    # Expected output:
    #    patient_id patient_name      conditions
    # 2          3         Bob  DIAB100 MYOP
    # 3          4      George  ACNE DIAB100


# Test Cases

# Test Case 1: No patients have Type I Diabetes
test_data1 = {
    'patient_id': [10, 11],
    'patient_name': ['Charlie', 'David'],
    'conditions': ['FEVER FLU', 'MALARIA']
}
df_test1 = pd.DataFrame(test_data1)
res1 = find_patients(df_test1)
assert res1.empty, "Test Case 1 Failed"

# Test Case 2: All patients have Type I Diabetes
test_data2 = {
    'patient_id': [12, 13],
    'patient_name': ['Eve', 'Frank'],
    'conditions': ['DIAB100', 'DIAB100 HYPERTENSION']
}
df_test2 = pd.DataFrame(test_data2)
res2 = find_patients(df_test2)
assert len(res2) == 2, "Test Case 2 Failed"

# Test Case 3: Mixed valid and invalid patients
test_data3 = {
    'patient_id': [14, 15, 16],
    'patient_name': ['Grace', 'Hannah', 'Ian'],
    'conditions': ['DIAB100', 'COLD', 'DIAB199 FLU']
}
df_test3 = pd.DataFrame(test_data3)
res3 = find_patients(df_test3)
assert len(res3) == 2, "Test Case 3 Failed"
assert set(res3['patient_id']) == {14, 16}, "Incorrect patient filtering"

print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N * M) where N is the number of patients and M is the average length of the conditions.
# Space Complexity: O(N) where N is the number of patients.
