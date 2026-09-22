#This exercise creates a list
coworkers = ['Waseel', 'Alice', 'Ashmeeta', 'Bob', 'Charlie', 'David', 'Eve']

message = f"hello {coworkers[0].title()}!"
print(message)

coworkers.insert(0, "Frank")

#removing a list item by value.
coworkers.remove("Bob")

print(coworkers)

new_coworkers = ["Alice", "Bob"]
print(new_coworkers)

#sorting
coworkers_alpha = coworkers.sort()
coworkers_reverse = coworkers.sort(reverse=True)
print(f"Sorted coworkers: {coworkers_alpha}")
print(f"Reverse alpha {coworkers_reverse}")

print(coworkers)