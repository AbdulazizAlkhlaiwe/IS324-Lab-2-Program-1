costs = []

while True:
    cost = float(input("Enter the cost for an item , Enter -1 to STOP "))
    if cost == -1:
        break
    costs.append(cost)

print("Costs:", costs)
print("the number of elements:", len(costs))
print("Highest cost:", max(costs))
print("Lowest cost:", min(costs))

total = sum(costs)
print("Total cost:", total)

Avg = total / len(costs)
print("Average cost:", Avg)

if len(costs) >5:
    print("orginal list:", costs)
    costs[5]=40
    print("new list:", costs)

else:
    print("there is no index 5")

if len(costs) >=4:
    print("old list:", costs)
    del costs[4]
    print("new list:", costs)
else:
    print("there is no index 4")

if 48 in costs:
    costs.remove(48)
    print("old list:", costs)
else:
    print("there is no 48")

############# part c
#costs_list = []

#while True:
#    cost = float(input("Enter the cost of an item (-1 to stop): "))
#    if cost == -1:
#        break
#    costs_list.append(cost)

#costs_tuple = tuple(costs_list)
#print("Cost Tuple:", costs_tuple)

#print("Number of elements in the tuple:", len(costs_tuple))

#if costs_tuple:
#    print("Highest cost in the tuple:", max(costs_tuple))

#    print("Lowest cost in the tuple:", min(costs_tuple))

#    total_costs = sum(costs_tuple)
#    print("Total of the costs in the tuple:", total_costs)

#    average_cost = total_costs / len(costs_tuple) if costs_tuple else 0
#    print("Average cost:", average_cost)



