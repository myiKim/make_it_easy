import os
import time

def algorithm(intlist):

	t1 = time.time()


	#######################CORE###########################
	N = len(intlist) #length of list

	#bound is for sorting space boundary(endpoint)
	for bound in range(1,N,1):
		#inside sorting space
		for i in range(bound, 0,-1):
			this = intlist[i]
			prev = intlist[i-1]
			if this < prev:
				#swap two
				intlist[i-1], intlist[i] = this, prev
	######################################################


	t2 = time.time()

	elapsed = t2 - t1

	return intlist, elapsed

def test():

	print("Test 1 begins: ")
	elapsed_times = []

	num = [3,1,14,5,6]
	expected = [1,3,5,6,14]

	result1, elapsed_time = algorithm(num)
	elapsed_times.append(elapsed_time)

	print("Test 1 finished: (result/expected): " , result1, " / " , expected)

	print("Test 2 begins: ")

	num = [3,1,14,5,6]
	expected = [1,3,5,6,14]

	result2, elapsed_time = algorithm(num)
	elapsed_times.append(elapsed_time)


	print("Test 2 finished: (result/expected): " , result2, " / " , expected)

	avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)
	print("Avg elapsed time: ", avg_elapsed_time)

if __name__ == "__main__":

	test_result, elapsed_time = test()
	print("Test Finished! (Elapsed time recorded as ): ", elapsed_time)
