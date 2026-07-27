fruits = ["яблоко"]
print(fruits)
fruits.append("банан")
print(fruits)
fruits.extend(["апельсин", "груша"])
print(fruits)
fruits.insert(1, "виноград")
print(fruits)

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits)
fruits.remove("банан")
print(fruits)
str1 = fruits.pop()
print(fruits)

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits)
print(fruits.index("банан"))
print(fruits.count("банан"))

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
