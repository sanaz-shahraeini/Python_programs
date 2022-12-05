# fizz_buzz = []
# i = 1
# while i <= 100:
#     if i % 15 == 0:
#         fizz_buzz.append("fizzbuzz")
#     elif i % 3 == 0:
#         fizz_buzz.append("fizz")
#     elif i % 5 == 0:
#         fizz_buzz.append("Buzz")
#     else:
#         fizz_buzz.append(i)
#     i += 1
# print(fizz_buzz)
# for i in fizz_buzz:
#     print(i)
#----------------
fizz_buzz = []
for i in range(1, 101):
    if i % 15 == 0:
        fizz_buzz.append("fizzbuzz")
    elif i % 3 == 0:
        fizz_buzz.append("fizz")
    elif i % 5 == 0:
        fizz_buzz.append("Buzz")
    else:
        fizz_buzz.append(i)
    i += 1
print(fizz_buzz)
for i in fizz_buzz:
    print(i)
