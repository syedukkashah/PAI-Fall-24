import numpy as np
students = np.array([
    ('Alice', 5.5, '10th'),
    ('Bob', 6.0, '9th'),
    ('Charlie', 5.7, '10th'),
    ('David', 5.8, '9th'),
    ('Eva', 5.9, '10th')
], dtype=[('name', 'U10'), ('height', 'f4'), ('class', 'U5')])
sorted_students = np.sort(students, order=['class', 'height'])
print(sorted_students)
