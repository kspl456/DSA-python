#Number of valid words in a sentence
'''
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
 

Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.
'''

def isValid(word):
            if any(char.isdigit() for char in word):
                return False
            if word.count("-")>1:
                return False
            if '-' in word:
                idx=word.index('-')
                if idx==len(word)-1 or idx==0: return False
                if not (word[idx-1].islower() and word[idx+1].islower()):
                    return False
            punct=['.',',','!']
            punctuation=sum(1 for char in word if char in punct)
            if punctuation>1: return False
            if punctuation==1:
                if word[-1] not in punct: return False
            if any(c in punct for c in word[:-1]):
                return False
            for i, c in enumerate(word):
                if not (c.islower() or c == '-' or c in punct):
                    return False
            return True

def countValidWords(sentence):
        words=sentence.split()
        count=0
        for i in words:
            if isValid(i):
                count+=1
        return count

'''
Approach
1. Split the sentence into tokens
Words in the sentence are separated by one or more spaces.
Use .split() to get a list of tokens (words).

2. Check each token for validity
For each token:

Rule A: No Digits
If it contains any digit, it's invalid.

Rule B: Hyphen
If there’s more than one hyphen → invalid.
If there's one hyphen:
It must not be the first or last character.
It must be surrounded by lowercase letters (e.g., "a-b" is okay, "-a", "a-" or "a-1" are not).

Rule C: Punctuation
If there’s more than one punctuation mark → invalid.
If there's one:
It must be at the end of the token.
No punctuation should appear before the last character.

Rule D: Character Check
All characters should be either:
Lowercase letters
A hyphen (at most one, placed correctly)
A punctuation mark (at most one, at the end)

3. Count the valid tokens
If a token passes all the checks, increase your count by 1.
'''