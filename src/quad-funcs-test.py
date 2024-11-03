import numpy as np


def original(alpha, aleph, hatted_a, tailed_a, n):
    sum = tailed_a
    for i in range(1, n):
        for j in range(1, i):
            sum += hatted_a + aleph * (j - 1)
        sum += alpha
    return sum


def optimised(alpha, aleph, hatted_a, tailed_a, n):
    return round(
        (aleph / 6) * (n**3)
        + ((hatted_a - 2 * aleph) / 2) * (n**2)
        + ((11 * aleph - 9 * hatted_a + 6 * alpha) / 6) * n
        + tailed_a
        + hatted_a
        - alpha
        - aleph
    )


# def GPT_optimised(alpha, aleph, hatted_a, tailed_a, n):
#     return round(
#         tailed_a
#         + alpha * (n - 1)
#         + hatted_a * (n - 1) * (n - 2) // 2
#         + aleph * (n - 1) * n * (2 * n - 10 + 12 / n) / 12
#     )


# Generate random test cases
np.random.seed(42)  # For reproducibility
num_tests = 10  # few because of bottleneck somewhere down here
alpha_vals = np.random.randint(-10000, 10000, num_tests)
aleph_vals = np.random.randint(-10000, 10000, num_tests)
hatted_a_vals = np.random.randint(-10000, 10000, num_tests)
tailed_a_vals = np.random.randint(-10000, 10000, num_tests)
n_vals = np.random.randint(1, 10000, num_tests)


def test_functions():
    # Define the threshold for acceptable difference
    threshold = 1e-5

    print("Starting tests...")

    # Vectorize the function calls
    results_original = np.vectorize(original)(
        alpha_vals, aleph_vals, hatted_a_vals, tailed_a_vals, n_vals
    )
    results_optimised = np.vectorize(optimised)(
        alpha_vals, aleph_vals, hatted_a_vals, tailed_a_vals, n_vals
    )

    # Calculate differences
    differences = np.abs(results_original - results_optimised)

    # Check if any differences exceed the threshold
    if np.any(differences > threshold):
        indices = np.where(differences > threshold)[0]
        for i in indices:
            print(f"Error in test case {i}:")
            print(f"  alpha       = {alpha_vals[i]}")
            print(f"  aleph       = {aleph_vals[i]}")
            print(f"  hatted_a    = {hatted_a_vals[i]}")
            print(f"  tailed_a    = {tailed_a_vals[i]}")
            print(f"  n           = {n_vals[i]}")
            print(f"  original    = {results_original[i]}")
            print(f"  optimised   = {results_optimised[i]}")
            print(f"  Difference  = {differences[i]}")
        return  # Exit on the first error found

    print("All test cases passed successfully.")


# Run the test function
test_functions()
