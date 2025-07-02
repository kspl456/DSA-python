# Problem: Newbie to Chat Room

# Background:
# Rohan has just learned to use the keyboard and access the Internet.
# As his first interaction online, he enters a chat room and tries to say "hello" to everyone.

# Input:
# - Rohan types a string `s`.
# - This string contains only lowercase Latin letters ('a' to 'z').
# - Length of `s` is between 1 and 100 characters (inclusive).

# Objective:
# - We need to check if Rohan's typed string contains the word "hello" as a subsequence.
# - A subsequence means we can remove some (or none) of the characters from the original string,
#   and the remaining characters, in order, should spell "hello".

# Examples:
# - If Rohan types "ahhellllloou":
#   -> We can extract characters 'h', 'e', 'l', 'l', 'o' in order, so the output is "YES".
# - If Rohan types "hlelo":
#   -> Though all characters of "hello" are present, they are not in the correct order.
#   -> So, the output is "NO".

# Output:
# - Print "YES" if the word "hello" is a subsequence of the typed string `s`.
# - Otherwise, print "NO".

s=input()
if len(s)< 5:
    print("NO")
else:
    hello="hello"
    typed=""
    i=0
    for letter in s:
        if typed!="hello":
            if hello[i]==letter:
                typed=typed+letter
                i+=1
        else:
            break
    if typed == hello:
        print("YES")
    else:
        print("NO")

#more optimised
s=input()
if len(s)< 5:
    print("NO")
else:
    hello="hello"
    i=0
    for letter in s:
        if hello[i]==letter:
                i+=1
        if i==5:
            break
    if i==5:
        print("YES")
    else:
        print("NO")
