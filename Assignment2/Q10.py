import numpy as np


def normalize_array(arr):

    mean = np.mean(arr)
    std_dev = np.std(arr)
    normal_arr = (arr - mean) / std_dev
    return normal_arr


sample_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
normalized_sample = normalize_array(sample_array)
print("Original Array:", sample_array)
print("Normalized Array:", normalized_sample)
