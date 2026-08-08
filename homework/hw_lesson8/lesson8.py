temps = [18, 22, -3, 25, 19, -1, 21]
temps_far = [x * 9 / 5 + 32 for x in temps]
print(temps_far)

users = {
    "Ivan": "qwerty",
    "maria": "12345",
    "petr": "admin",
    "anna": "pass",
    "guest": "guest"
}
users_new = {login: len(password) for login, password in users.items()}
print(users_new)

scores = (10, 7, 0, 9, 8, 5)
scores_x_10 = tuple(x * 1.1 for x in scores)
print(scores_x_10)
