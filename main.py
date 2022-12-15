def reverseString(string):
	if len(string) <= 1:
		return string

	return (String[-1] + reverseString(string)[:-1])
test_string = "This is a test string to test reversal!"
print(test_string)
print(reverseString(test_string))

def fib(x):
	if(x== 1):
		return 1
	elif x == 0:
		return 0
	else:
		returnfib(x-1) + fib(x - 2)
def fibIter(x):
	1 = 0
	a = 0
	b = 1
	while i < x:
		c = a + b
		a = b
		b = c
		1 += 1
	print(b)
fib(50)
