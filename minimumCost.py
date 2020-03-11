def getMinimumCost(cost, n): 
	cost = sorted(cost) # sorting cost using O(nlg(n)) tim sort
	totalCost = 0

	for i in range(n - 1, 1, -2): #O(n)
		if (i == 2): 
			totalCost += cost[2] + cost[0] 

		else: 
			costFirst = cost[i] + cost[0] + 2 * cost[1] 
			costSecond = cost[i] + cost[i - 1] + 2 * cost[0] 
			totalCost += min(costFirst, costSecond) #why minimum because we want to reduce cost

	if (n == 1): 
		totalCost += cost[0] 
	else: 
		totalCost += cost[1] 

	return totalCost 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        numOfPers = int(input())
        arr = list(map(int,input().split()))
        result = getMinimumCost(arr,numOfPers)
        print(result)

# Space Complexity: O(1) -> we are not using any extra space.
# Time Complexity: O(n*lg(n)) -> Because sort is taking O(n*lg(n)) => lg = log base 2.
