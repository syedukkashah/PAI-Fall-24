def product(lst):
    result = 1
    for i in lst:
        result*=i
    return result


list = [1, 2, 3, 4, 5]
print(product(list))


