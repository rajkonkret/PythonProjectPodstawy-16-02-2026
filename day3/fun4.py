# funkcja wewnętrzna, zagnieżdżona


def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun1()  # To jest fun1
xfun = fun1()
print(type(xfun))  # <class 'function'>
print(xfun)  # <function fun1.<locals>.fun2 at 0x00000202FB73B1C0>
xfun()
xfun()
xfun()
xfun()
xfun()
xfun()
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2
