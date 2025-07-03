# Problem:Friendship ended
# Ramesh is learning to chat on Facebook and wants to say “Goodbye” (with no space) to his friend Suresh.
# He typed a word 'w'. We want to check whether it's possible to delete some characters from 'w'
# (without reordering the remaining characters) to form the word "Goodbye".
# If yes, print "Yes". Otherwise, print "No".
#
# For example:
# Input:  btaGpotodbqqyeekje   -> Output: Yes (because we can form "Goodbye" from it)
# Input:  pngodtbeyz           -> Output: No  (cannot form "Goodbye")

w=input()
goodbye="Goodbye"
i=0
for word in w:
        if i<len(goodbye) and word == goodbye[i]:
            i+=1
print("Yes" if i==len(goodbye) else "No")
