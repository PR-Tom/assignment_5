def remove_uneven(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


original_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_uneven(original_list)

print("Original list:", original_list)
print("List without uneven numbers:", new_list)
