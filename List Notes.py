# Creating a List
groceries = ["milk", "eggs", "bread", "oranges", "milk"]
boring_list = [7, 7, 7, 7, 7, 7, 0]
numbers = [12, 2, 3.5, 1]
empty_list = []

# Counting items in a list
length = len(groceries)
print("Our grocery list has {} items".format(length))
length2 = len(boring_list)
length3 = len(numbers)

# Accessing items in a list (we do this by index)
print(groceries[2])
print(groceries[0])  # Index starts at 0 not 1
print(groceries[3])
print(groceries[-1])
print(groceries[-2])

# Adding items to a list
print(groceries)
groceries.append("Apples")  # Always adds it to the END
print(groceries)

groceries.insert(1, "soda")  # Adds to index 1
print(groceries)
# print(groceries[1000])

# Removing items from a list
groceries.remove("milk")  # Only the first milk is gone
print(groceries)

groceries.pop(0)  # Removes the item at index 0
print(groceries)

# Finding items
spot = groceries.index("oranges")
print("Oranges are at index {}".format(spot))

print(boring_list)
ind = boring_list.index(7)
print("The number 7 is at index {}".format(ind))
# The index method only finds the first one!

# Sorting the list
print(groceries)
groceries.sort()
print(groceries)

print(numbers)
numbers.sort()
print(numbers)

print(groceries)
groceries.reverse()  # It's backwards!
print(groceries)

for i in groceries:
    print(groceries)
