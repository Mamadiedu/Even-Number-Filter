def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6])) 
print(get_even_numbers([11, 13, 15])) 
print(get_even_numbers([10, 20, 25, 30])) 
