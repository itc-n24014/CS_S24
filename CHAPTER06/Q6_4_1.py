import random
random.seed(1)
msgs = ["HI", "Hello", "Good Morning", "Good night", "See you later", "How are you", "Have a good day"]

with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write(f"{i}, {random.choice(msgs)}\n")

with open("some.txt", "r") as f:
    for i in range(3):
        line = f.readline()
        print(line.rstrip())
