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
