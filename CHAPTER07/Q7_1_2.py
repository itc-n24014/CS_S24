def list_average(number):
    try:
        return sum(number) / len (number)
    except ZeroDivisionError:
        print('list_lenght:', len(number))
        return 'none'
print(list_average([1.5, 2.5, 3.5]))
print(list_average([]))
