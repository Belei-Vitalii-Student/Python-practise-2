number = 200

count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count += 1

print(f"Кількість дільників у числа {number} - {count}")