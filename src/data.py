import numpy as np

def transform_dataset(original_dataset):
    # Convert the original dataset to a NumPy array for easier manipulation
    original_array = np.array(original_dataset)
    
    # Create a new dataset with the same shape
    new_dataset = original_array / (np.arange(1, original_array.size + 1).reshape(original_array.shape) ** 1.5)
    
    # Print the new dataset with 2 decimal places
    print(np.round(new_dataset, 2))
    print(np.round(np.sum(new_dataset), 2))

# Example usage
original_data = [24983, 12478, 134, 129, 121, 118, 109, 103, 96, 83]
transform_dataset(original_data)
