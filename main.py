def compound_interest(initial_balance, interest_rate,years_past):
    if years_past == 0:
        return init_bal
    if init_bal == 0:
        return 0

def reverseString(string):
    if len(string) <= 1:
        return string

    return string[-1] + reverseString(string[:-1])

print(Palidrome)
print(reverseString(Palidrome))

def fib(x):
    if(x == 1):
        return 1
    elif x == 0:
        return 0
    else:
        return fib(x-1) + fib(x - 2)

def fibIter(x):
    i = 0
    a = 0
    b = 1
    while i < x:
        c = a + b
        a = b
        b = c
        i += 1
    print(b)