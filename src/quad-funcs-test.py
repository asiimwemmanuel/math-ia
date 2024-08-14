import numpy as np


def original(alpha, aleph, hatted_a, tailed_a, n):
    sum = tailed_a
    for x in range(1, n):
        buffer = alpha
        for y in range(1, x + 1):
            buffer += hatted_a + aleph * (y - 1)
        sum += buffer
    return sum


def optimised(alpha, aleph, hatted_a, tailed_a, n):
    sum = (
        (aleph / 6) * (n**3)
        + ((hatted_a - aleph) / 2) * (n**2)
        + ((6 * alpha - 3 * hatted_a + 2 * aleph) / 6) * n
        + tailed_a
        - alpha
    )
    return sum


# Number of test cases
num_tests = 1000000

# Generate random test cases
np.random.seed(42)  # For reproducibility
alpha_vals = np.random.randint(-10000, 10000, num_tests)
aleph_vals = np.random.randint(-10000, 10000, num_tests)
hatted_a_vals = np.random.randint(-10000, 10000, num_tests)
tailed_a_vals = np.random.randint(-10000, 10000, num_tests)
n_vals = np.random.randint(1, 10000, num_tests)


def test_functions():
    # Define the threshold for acceptable difference
    threshold = 1

    print("Starting tests...")

    # Precompute results using vectorized operations if applicable
    results_original = np.array(
        [
            original(alpha, aleph, hatted_a, tailed_a, n)
            for alpha, aleph, hatted_a, tailed_a, n in zip(
                alpha_vals, aleph_vals, hatted_a_vals, tailed_a_vals, n_vals
            )
        ]
    )
    results_optimised = np.array(
        [
            optimised(alpha, aleph, hatted_a, tailed_a, n)
            for alpha, aleph, hatted_a, tailed_a, n in zip(
                alpha_vals, aleph_vals, hatted_a_vals, tailed_a_vals, n_vals
            )
        ]
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
