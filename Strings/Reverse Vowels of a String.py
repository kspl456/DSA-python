#Reverse Vowels of a String
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

def reverseVowels(s):
        st=list(s)
        vowel=set("aeiouAEIOU")
        left,right=0,len(st)-1
        while left<right:
            while left<right and st[left] not in vowel: left+=1
            while left< right and st[right] not in vowel: right-=1
            st[left],st[right]=st[right],st[left]
            left+=1
            right-=1
        return ''.join(st)

'''
Approach:
1. Convert the input string `s` into a list of characters `st` to allow for easy swapping.
2. Create a set `vowel` containing all the vowels (both lowercase and uppercase).
3. Initialize two pointers, `left` starting at the beginning of the list and `right` starting at the end of the list.
4. Use a while loop to iterate until the `left` pointer is less than the `right` pointer.
    - Move the `left` pointer to the right until it points to a vowel.
    - Move the `right` pointer to the left until it points to a vowel.
    - Swap the characters at the `left` and `right` pointers.
    - Move both pointers inward (increment `left` and decrement `right`).
5. Finally, join the list of characters back into a string and return it.
'''
#Time Complexity: O(n), where n is the length of the string.
#Space Complexity: O(n) for the list of characters.