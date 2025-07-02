# Problem: Find the Right Fit

# Scenario:
# There are N mice and N holes placed on a straight line (1D positions).

# Rules:
# - Each hole can accommodate exactly one mouse.
# - Mice can move:
#     - Stay in place
#     - Move one unit left (x → x - 1)
#     - Move one unit right (x → x + 1)
# - Each move (one step) takes exactly 1 minute.

# Objective:
# - Assign each mouse to a unique hole.
# - The goal is to minimize the **maximum time** taken by any mouse to reach its assigned hole.
# - This means: the last mouse to enter a hole should do so in the least time possible.

# Input Format:
# - Line 1: An integer N (number of mice and holes)
# - Line 2: N space-separated integers representing positions of the mice
# - Line 3: N space-separated integers representing positions of the holes

# Constraints:
# - 1 ≤ N ≤ 10^5

# Output Format:
# - A single integer: the minimum number of minutes required for the last mouse to get into a hole.

# Sample Input:
# 3
# 4 -4 2
# 4 0 5

# Explanation of Sample:
# - After sorting mice:   [-4, 2, 4]
# - After sorting holes:  [0, 4, 5]
# - Optimal pairing:
#     - Mouse at -4 → Hole at 0 → Time = 4
#     - Mouse at 2  → Hole at 4 → Time = 2
#     - Mouse at 4  → Hole at 5 → Time = 1
# - Maximum time taken by any mouse = 4 (this is the output)

n=int(input())
mouse=list(map(int,input().split()))
hole=list(map(int,input().split()))
mouse.sort()
hole.sort()
max_time=0
for i in range(n):
    max_time=max(max_time, abs(mouse[i]-hole[i]))
print(max_time)
