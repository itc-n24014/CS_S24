X = 'Happy'

def event1():
    print("In event1:", X, end=" -> ")

def event2():
    x = 'Sad'
    print("In event2:", x, end=" -> ")

def event3():
    global X
    X = 'Tired'
    print("In event3:", X, end=" -> ")

def event4():
    x = 'Excite'
    def happening():
        print("In event4:", x, end=" -> ")
    happening()

def event5():
    x = 'Fun'
    def happening():
        nonlocal x
        x = 'Scare'
        print("In event5:", x, end=" -> ")
    happening()

func_list = [event1, event2, event3, event4, event5]
for f in func_list:
    f()
    print("After {}: {}".format(f.__name__, X))
