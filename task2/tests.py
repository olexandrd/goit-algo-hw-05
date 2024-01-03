from binary_search import binary_search

# Define array and target value
sorted_array = [1, 2.5, 3.5, 5.0, 7.0, 8.2, 10.0]
target_value = 5.0

# Check exact match 
assert binary_search(sorted_array, target_value) == (1, 5.0)
assert binary_search(sorted_array, 2.5) == (2, 2.5)

# Check most relevant match 
assert binary_search(sorted_array, 8.0) == (3, 8.2)

# Check out of range conditions
assert binary_search(sorted_array, 0) == (3, 1)
assert binary_search(sorted_array, 11) == (3, None)

print("Passed")