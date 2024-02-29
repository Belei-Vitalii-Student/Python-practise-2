n = 100
last = 1
fibonachi = 0

while fibonachi < n:
    print(fibonachi)
    fibonachi, last = fibonachi + last, fibonachi

counter = 1
fibonachi = 0
last = 1

while counter <= 20:
    if counter >= 5:
        print(fibonachi)
    fibonachi, last = fibonachi + last, fibonachi
    counter += 1