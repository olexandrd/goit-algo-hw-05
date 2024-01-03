from hashTable import HashTable

H = HashTable(5)
# Insert data
assert H.insert("apple", 10) == True
assert H.insert("orange", 20) == True
assert H.insert("banana", 30) == True
assert H.insert("pineaple", 30) == True


# Get data
assert H.get("apple") == 10
assert H.get("orange") == 20
assert H.get("banana") == 30
assert H.get("cucumber") == None

# Delete data
assert H.delete("apple") == True
assert H.delete("cucumber") == False

# Display table
print(H.table)

print("Passed")