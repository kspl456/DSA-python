#Relative Ranks
'''
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
'''

def findRelativeRanks(score):
        rank={}
        sorted_score=sorted(score, reverse=True)
        for i in range(len(sorted_score)):
            if i==0:
                rank[sorted_score[i]]="Gold Medal"
            elif i==1:
                rank[sorted_score[i]]="Silver Medal"
            elif i==2:
                rank[sorted_score[i]]="Bronze Medal"
            else:
                rank[sorted_score[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(rank[i])
        return res

'''
Approach:
1. Create a dictionary `rank` to store the rank of each score.
2. Sort the `score` array in descending order to determine the ranks.
3. Iterate through the sorted scores and assign ranks:
    - The first score gets "Gold Medal".
    - The second score gets "Silver Medal".
    - The third score gets "Bronze Medal".
    - For all subsequent scores, assign their rank as a string of their position (i+1).
4. Create a result list `res` and populate it by looking up the rank for each original score in the `rank` dictionary.
5. Return the result list `res` containing the ranks of the athletes in the order of the original scores.
'''
#Time Complexity: O(n log n) due to sorting, where n is the length of the input array.
#Space Complexity: O(n) for storing the ranks in a dictionary and the result list.