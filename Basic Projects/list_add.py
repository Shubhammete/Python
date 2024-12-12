
def add_many_numbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = add_many_numbers(numbers)
print(sum_of_numbers)