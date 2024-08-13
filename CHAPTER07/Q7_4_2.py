def test_func():
    try:
        print('try')
        return
    except:
        print('except')
    else:
        print('else')
    finally:
        print('finally')

test_func()
