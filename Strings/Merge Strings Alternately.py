#Merge Strings Alternately
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

def mergeAlternately(word1, word2):
        i=0
        ans=[]
        while i<len(word1) and i< len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i+=1
        ans.append(word1[i:])
        ans.append(word2[i:])
        return ''.join(ans)

'''
Approach:
1. Initialize an index `i` to 0 and an empty list `ans` to store the merged characters.
2. Use a while loop to iterate through both strings as long as `i` is less than the lengths of both strings.
3. In each iteration, append the character from `word1` at index `i` and the character from `word2` at index `i` to the `ans` list.
4. Increment the index `i` by 1.
5. After the loop, append any remaining characters from `word1` and `word2` (if one string is longer) to the `ans` list.
6. Finally, join the list `ans` into a single string and return it.
'''

#Time Complexity: O(n + m), where n and m are the lengths of word1 and word2 respectively.
#Space Complexity: O(n + m) for storing the merged string in the list ans.