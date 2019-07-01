# Without Decorator, function math returns 'SUM'
# With Decorator, function math returns list of [SUM, DIFF, MUL, DIV]
def decor(func):
    def decor_func(c,d):
        diff = c - d
        su = func(c,d)
        mul = c * d
        div = c / d
        return [su, diff, mul, div]
    return decor_func

@decor
def math(a,b):
    return a+b

l = math(2,3)
print(l)
