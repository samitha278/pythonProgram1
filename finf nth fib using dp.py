fibo = {1:0 , 2:1}

def fib(n):
	if n == 1:          #base case
		return 0
	if n == 2:
		return 1

	try:
		x1 = fibo[n-1] 
	except KeyError:
		x1 = fib(n-1)
		fibo[n-1] = x1

	try:
		x2 = fibo[n-2]
	except KeyError:
		x2 = fib(n-2)
		fibo[n-2] = x2

	return x1 + x2


print(fib(35))
