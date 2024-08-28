def avg(lst):
    sum = cnt = 0
    for i in lst:
        sum+=i
        cnt+=1
    return sum/cnt

def sort(lst):
    for i in range(30):
        for j in range(0, 30-i-1):
            if(lst[j]>lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

def delete(lst, day):
        lst.pop(day)


temperatures = [30, 32, 31, 29, 28, 27, 30, 31, 32, 33, 34, 35,
                 33, 32, 31, 30, 29, 28, 30, 31, 32, 33, 34, 35,
                 33, 32, 31, 30, 29, 28, 27, 28, 29, 30, 31, 32,
                 33, 34, 35, 36, 37, 36, 35, 34, 33, 32, 31, 30]
sort(temperatures)
print("Sorted list: ", temperatures)
print("Lowest temperature: ", temperatures[0])
print("\nHighest temperature: ", temperatures[29])
print("\nAverage temperature: ", avg(temperatures))
print("Removing temperature for day 1...")
delete(temperatures, 0)
print(temperatures)
