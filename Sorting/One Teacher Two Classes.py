#One Teacher Two Classes
# Jessy, the P.E instructor for Middle Vale High School has to arrange his students in line for aerobics.
# Thankfully, his class of students already came to the court in a line of increasing order of heights.
# Not so thankfully, James, another P.E instructor is on leave again. So she has to take care of his class right now as well.
# The second class of students also came in a line of increasing order of heights.
# But Jessy feels that is useless since she has to make both classes stand together in a single line for her exercises.
# But you, the janitor (and also a computer science graduate with no other job), sees that this is the right place to use the merge technique.
# So write a program to help Jessy arrange the students in ascending order of their heights.
#
# Formally, given two sorted arrays, merge them into one sorted array and print the result.
#
# INPUT
# The first line of input is n (1
#
# OUTPUT
# Print the heights of the students in a row after both the lines have been merged.
#
# Sample Input 0
# 5
# 2 4 6 8 10
# 5
# 1 3 5 7 9
#
# Sample Output 0
# 1 2 3 4 5 6 7 8 9 10

n1=int(input())
s1=list(map(int,input().split()))
n2=int(input())
s2=list(map(int,input().split()))
i=0
n=n1+n2
j=0
s=[]
while i<n1 and j<n2:
    if s1[i]< s2[j]:
        s.append(s1[i])
        i+=1
    else:
        s.append(s2[j])
        j+=1
while i<n1:
    s.append(s1[i])
    i+=1
while j<n2:
    s.append(s2[j])
    j+=1
print(*s)
