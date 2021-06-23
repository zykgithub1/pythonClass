def enter_background():
    print("go into background")

def delete_order():
    i=0
    print("delete order")
    def func():
        nonlocal i
        print(i)
        i=10
        print(i)
    return func
result=delete_order()
print(result())
