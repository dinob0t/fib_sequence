"""
Algorithm to calculate n numbers of the fibonacci sequence by calcuating the exact elements via 
exponentiation. Makes use of the identity
|1 1|^n   |F(n+1)   F(n)|
|1 0|   = |F(n)   F(n-1)| 
"""
import time

fib_memo = {0:0, 1:1}

def mat_mul(A,B):
	#|A[0], A[1]|   |B[0], B[1]|
	#|A[1] ,A[2]| * |B[1], B[2]|
	return [A[0]*B[0] + A[1]*B[1], A[0]*B[1] + A[1]*B[2], A[1]*B[1] + A[2]*B[2]]

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

def fib_exact(n):
	if n < 0:
		return []
	if n == 0:
		return [0]
	if n == 1:
		return [1, 0]
	return mat_pow([1,1,0], n-1) + fib_exact(n-3)

def fib_recur(n):
    if not n in fib_memo:
        fib_memo[n] = fib_recur(n-1) + fib_recur(n-2)
    return fib_memo[n]


def fib_iter(n):
	fib = [0]
	if n == 0:
		return fib
	fib += [1]
	if n == 1:
		return fib
	else:	
    		for i in range(2,n):
    			fib += [fib[i-1] + fib[i-2]]
    	return fib


fib_terms = 200
	
t0 = time.time()
print "Fib list by exact squaring ", fib_exact(fib_terms-1)
t1 = time.time()
print "Time taken %f s" %(t1-t0)	

t0 = time.time()
fib_recur(fib_terms-1)
print "Fib list by recursion ", fib_memo
t1 = time.time()
print "Time taken %f s" %(t1-t0)

t0 = time.time()
print "Fib list by iteration ", fib_iter(fib_terms)
t1 = time.time()
print "Time taken %f s" %(t1-t0)



