def prime_generator():
    x = 2
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1

i = prime_generator()
for c in range(10):
    print(next(i), end=" ")
print("")

