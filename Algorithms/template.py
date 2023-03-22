import os
import time

def some_algo():

	t1 = time.time()



	t2 = time.time()

	elapsed = t2 - t1

	return elapsed

def test():

	num = [3,1,14,5,6]

	result = some_algo(num)

	return result

if __name__ == "__main__":

	test_result = test()
	print("Test Finished: ")