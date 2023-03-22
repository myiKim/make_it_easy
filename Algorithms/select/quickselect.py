import os
import time


def partition(intlist, left, right, pivot_index=None):

    pivot_index = right if pivot_index == None else pivot_index
    pivot = intlist[right] #choose the right pointer to be the pivot

    switch = left #switch variable: to be used for switching
    for j in range(left,right,1):

        if intlist[j] <= pivot: #when less than pivot,that means it is a small number, so we move it to the left
            intlist[switch], intlist[j] = intlist[j], intlist[switch]
            switch +=1

    #Lastly, move pivot to (in it's  place)
    intlist[switch], intlist[right] = intlist[right] ,intlist[switch]

    return switch


def quickSelect(array, k):
    #find the k th smallest
    t1 = time.time()

    #######################CORE###########################
    def recursion_helper( left, right, k_small):
        if left == right:
            #only one element in the array
            return

        pivot_index = partition(array, left, right)
        if k_small > pivot_index:
            #this means indices to the left of pivot_index is already well partitioned.
            recursion_helper(pivot_index+1,right , k_small)
        elif k_small < pivot_index:
            recursion_helper(left, pivot_index-1, k_small)

        else: #when values are equal it finishes calculation
            return

    N = len(array)

    recursion_helper( 0, N-1, k)

    print("processed array: ",array)

    ######################################################
    t2 = time.time()
    elapsed = t2 -t1
    return array[:k], elapsed


def algorithm(numlist, k):

	return quickSelect(numlist, k)


def test():

	print("Test 1 begins: ")
	elapsed_times = []

	numslist = [31,19, -2, 175,-7,6, 12, 24, -3, -21, 55, 92, 3, 7, 22,16,14,18,13.3 ,33.5, 23.1, 73.4, 90.9, 372.5, 7.7, 3]
	k = 15
	expected = [-21, -7, -3, -2, 3, 3, 6, 7, 7.7, 12, 13.3, 14, 16, 18, 19]

	result1, elapsed_time = algorithm(numslist, k)
	elapsed_times.append(elapsed_time)

	print("Test 1 finished: (result/expected): " , sorted(result1), " / " , expected)

	print("Test 2 begins: ")

	numslist = [31,19, -2, 175,-7,6, 12, 24, -3, -21, 55, 92, 3, 7, 22,16,14,18,13.3 ,33.5, 23.1, 73.4, 90.9, 372.5, 7.7, 3]
	k =1
	expected = [-21]

	result2, elapsed_time = algorithm(numslist,k)
	elapsed_times.append(elapsed_time)


	print("Test 2 finished: (result/expected): " , sorted(result2), " / " , expected)

	avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)
	print("Avg elapsed time: ", avg_elapsed_time)

if __name__ == "__main__":

	test()
