import numpy as np
random_array = np.random.rand(1000)
average = np.mean(random_array)
variance = np.var(random_array)
std_deviation = np.std(random_array)
results = f"Average: {average}\nVariance: {variance}\nStandard Deviation: {std_deviation}"
file_name = "array_statistics.txt"
with open(file_name, 'w') as file:
    file.write(results)
print(f"Results saved to {file_name}")
