#def test(*args, **kwargs):
#    print(args, kwargs)
#
#
#test(1, 2, 3, 4, 5, a="main", b="homework")

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Введите число:"))
print("Факториал:")
print(factorial(n))
