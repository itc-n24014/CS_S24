test = 'out_test.txt'
s = 'Hello out_test.txt'
with open(test, 'w') as f:
    f.write(s)

with open(test, 'r') as f:
    for line in f:
        print(line, end="")
