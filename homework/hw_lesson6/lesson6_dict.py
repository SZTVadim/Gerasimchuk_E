dict1 = {
    "имя": "Иван",
    "возраст": "20",
    "курс": 2,
    "город": "Москва"
}
print(dict1.keys())
print(dict1.values())
for key, value in dict1.items():
    print(key, value)
for value in dict1.values():
    print(value)

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = {key: value for key, value in student1.items()}
student3.update(student2)
student1.update(student2)
print(student1)
print(student1, student2, student3)

