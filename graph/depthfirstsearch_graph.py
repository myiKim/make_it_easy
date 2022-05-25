import os
import time

def dfs_traverese(graph, start_node=1):

	t1 = time.time()

	#######################CORE###########################
	
	curr = None
	stack = [start_node]
	visited = []
	while stack:
		#put all the neighbors into the stack
		curr = stack.pop()
		print(curr)
		if curr not in visited:
			visited.append(curr)
		else: # skip already visited node
			continue 
		for neighbor in graph[curr]:
			print("neigh: ", neighbor)
			stack.append(neighbor)


	######################################################


	t2 = time.time()

	elapsed = t2 - t1

	return visited, elapsed






def algorithm(graph, start_node=1):


	return dfs_traverese(graph, start_node)


def test():

	print("Test 1 begins: ")
	elapsed_times = []

	#Adjacent nodes are represented as a dict
	graph = {
		1 :[2,3,4][::-1], #reverse it b/c I want to visit smallest numbered neighbor first?
		2 :[1,5,6][::-1],
		3 :[1,5][::-1],
		4 :[1,5][::-1],
		5 :[2,3,4,6][::-1],
		6 :[2,5][::-1] 
	}
	

	result1, elapsed_time = algorithm(graph, 1)
	elapsed_times.append(elapsed_time)

	print("Test 1 finished: (result/expected): " , result1, " / " )
	
	print("Test 2 begins: ")
	
	graph = {
		1 :[2,3,4][::-1], #reverse it b/c I want to visit smallest numbered neighbor first?
		2 :[1,5,6][::-1],
		3 :[1,5][::-1],
		4 :[1,5][::-1],
		5 :[2,3,4,6][::-1],
		6 :[2,5][::-1] 
	}
	

	result2, elapsed_time = algorithm(graph, 2)
	elapsed_times.append(elapsed_time)
	

	print("Test 2 finished: (result/expected): " , result2, " / ")
	

	avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)
	print("Avg elapsed time: ", avg_elapsed_time)

if __name__ == "__main__":

	test()
