def list_del_nth(lst, index):
    try:
        del lst[index]
        print('Successfully')
    except IndexError:
        print('Index Not Found')
    except Exception:
        print('Unexpected Error')

sample_list = [10, 20, 30, 40, 50]
list_del_nth(sample_list, 2)
print(sample_list)

list_del_nth(sample_list, 10)
list_del_nth(sample_list, 'a')
