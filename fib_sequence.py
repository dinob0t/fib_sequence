"""
Algorithm to calculate n numbers of the fibonacci sequence by calcuating the exact elements via 
exponentiation. Makes use of the identity
|1 1|^n   |F(n+1)   F(n)|
|1 0|   = |F(n)   F(n-1)| 
"""

def mat_mul(A,B):
	#|a,b|   |d,e|
	#|b,c| * |e,f|
	a,b,c = A
	d,e,f = B
	return a*d + b*e, a*e + b*f, b*e + c*f

def mat_pow(A,n):
	if n == 0:
		return 1
	if n < 0:
		return mat_pow(1.0/A,-n)
	if n==1:
		return A
	if n % 2 == 0: 
		return mat_pow(mat_mul(A,A), n//2)
	else:
		return mat_mul(A, mat_pow(mat_mul(A,A), (n-1)//2))

def fib(n):
	if n <1:
		return 0
	if n == 1:
		return 1, 0
	return mat_pow((1,1,0), n-1)

print fib(8) 		

