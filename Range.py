def convert_to_range(numbers, x, y):
    min_num = min(numbers)
    max_num = max(numbers)
    old_range = max_num - min_num
    new_range = y - x
    converted_numbers = [(num - min_num) * new_range / old_range + x for num in numbers]
    return converted_numbers

# Example usage:
numbers = [i for i in range(60,460)]
#print(numbers)
x = 131
y = -80
converted_numbers = convert_to_range(numbers, x, y)
print(len(numbers))
print(len(converted_numbers))
d={}
for i in range(len(numbers)):
    d[numbers[i]]=converted_numbers[i]
print(d)