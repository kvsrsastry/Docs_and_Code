def add(a,b,*args):
    sum = a + b
    for num in args:
        sum += num
    return sum

def div(a, b):
    if(b == 0):
        print('Divisor cannot be ZERO')
        return
    else:
        return a/b

if __name__ == '__main__':
    print(add(3,4))
    print(div(7,3))

