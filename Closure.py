# This program Closure.py is called from Closure_module.py

def outerf(*abc): # This is Enclosing function and Enclosing Scop is up to return statement
	print("Outer")
	print(sum(abc))

	def innerf(*pqr): # This is Nested function
		print("Inner")
		q = 1
		for p in pqr:
			mult1 = p * q + sum(abc)
			q = mult1
		print("Multi = ", mult1)

	return innerf

outerf(10,20,30)

call1 = outerf(10,20,30)
call1(2,3,4)
