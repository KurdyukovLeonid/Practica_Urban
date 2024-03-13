def test(args):
    for i, arg in enumerate(args):
        print(arg, end = ' ')

par = 12, False, 5.6, 'строка'
test(par)

def factorial(n):
    if n == 1:
        return 1
    fact_n = factorial(n-1)
    return n * fact_n

print(factorial(9))