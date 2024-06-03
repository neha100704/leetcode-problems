def twoCitySchedCost(self, costs):
    costs.sort(key=lambda x:x[0]-x[1])
    total_cost=0
    n=len(costs)//2
    for i in range(n):
        total_cost+=costs[i][0]
    for i in range(n,len(costs)):
        total_cost+=costs[i][1]
    return total_cost

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))
