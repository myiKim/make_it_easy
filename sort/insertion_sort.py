import os
import time

def algorithm_ONsq(intlist):

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

def algorithm_effcient(intlist):

	t1 = time.time()


	#######################CORE###########################
	N = len(intlist) #length of list

	#devided into two groups: S(searched) / U (Unserached)
	for i in range(1,N,1):
		this = intlist[i] #temporarily store the first elem. of U (will be inserted)
		j = i # the index that will cover the searched space(S) starting from j-1, which is the last elem. of S  
		move = True if intlist[j-1] > this else False
		
		#idea: move only when needed(current pointer element less than previous one) so that it reduces runtimes
		while (move and  j>0): 
			#while loop iterates until it finds the point this value will be inserted
			intlist[j] = intlist[j-1] #prev one move behind 
			j -=1 #decreasing index
			
		intlist[j] = this #represent the "insertion"; the i th elem. of list now gets inserted into the place we want.

	######################################################


	t2 = time.time()

	elapsed = t2 - t1

	return intlist, elapsed





def algorithm(intlist):

	#return algorithm_ONsq(intlist)
	return algorithm_effcient(intlist)


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

	test()
