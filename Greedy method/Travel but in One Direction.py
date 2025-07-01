#Travel but in One Direction
# -------------------------------------
# There are N gas stations arranged in a circular route.
# Each gas station i has a certain amount of gas: gas[i]
# It costs cost[i] amount of gas to travel from station i to station (i + 1).

# You start the journey with an **empty gas tank** at one of the stations.
# Your goal is to determine the **minimum starting gas station's index** such that
# you can complete the entire circuit exactly once, returning to the starting station.

# You may only travel in one direction: i → i+1 → i+2 → ... → n-1 → 0 → 1 → ... → i

# If it's **not possible** to complete the circuit from any station, print -1.

# Input Format:
# --------------
# The first line contains an integer N — the number of gas stations.
# The second line contains N space-separated integers — gas[i] values.
# The third line contains N space-separated integers — cost[i] values.

# Constraints:
# -------------
# 1 <= N <= 10^5                  # Large input size
# All gas[i] and cost[i] are integers (typically in a reasonable range)

# Output Format:
# ---------------
# Print a single integer:
# - The minimum starting index (0-based) from which you can complete the circuit
# - Or -1 if completing the circuit is impossible

# Sample Input:
# --------------
# 2
# 1 2
# 2 1

# Sample Output:
# ---------------
# 1

# Explanation:
# ------------
# Trying from station 0:
#   gas = 1, cost = 2 → not enough gas → FAIL
# Trying from station 1:
#   gas = 2, cost = 1 → next station has gas = 1, cost = 2 → total gas = 2 → total cost = 3 → SUCCESS
# So index 1 is a valid starting point.

n=int(input())
gas=list(map(int,input().split()))
cost=list(map(int,input().split()))

total_gas=0
tank=0
start=0

for i in range(n):
    total_gas+=gas[i]-cost[i]
    tank+=gas[i]-cost[i]
    if tank <0:
        start=i+1
        tank=0
if total_gas >=0:
    print(start)
else:
    print(-1)
