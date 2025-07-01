#Greedy Rayinshi
# ------------------------
# Rayinshi and Neechea are playing a game with a row of n cards.
# Each card has a distinct integer value. Players take turns picking cards.
# - On each turn, a player can take either the leftmost or rightmost card.
# - Rayinshi always goes first.
# - Both players are greedy: they always pick the higher-valued card available to them.

# The game continues until there are no cards left.
# The player with the higher total sum of collected card values wins.

# Inna, their friend, knows their strategy and wants to calculate the final scores.

# Input Format:
# -------------
# The first line contains a single integer n — the number of cards.
# The second line contains n space-separated integers representing card values from left to right.

# Constraints:
# ------------
# 1 <= n <= 1000               # Maximum 1000 cards
# All card values are distinct

# Output Format:
# --------------
# Print two space-separated integers:
# - The first is Rayinshi's total score.
# - The second is Neechea's total score.

# Sample Input:
# -------------
# 4
# 4 1 2 10

# Sample Output:
# --------------
# 12 5

# Explanation:
# Rayinshi picks 10, then Neechea picks 4, then Rayinshi picks 2, and Neechea picks 1.
# Final scores: Rayinshi = 10 + 2 = 12, Neechea = 4 + 1 = 5

n=int(input())
card=list(map(int,input().split()))
p1=0;p2=0
for _ in range(n//2):
    if card[0]> card[-1]:
        p1+=card.pop(0)
    else:
        p1+=card.pop()
    if card[0]> card[-1]:
        p2+=card.pop(0)
    else:
        p2+=card.pop()
print(p1,p2)
