#Union of Arrays with Duplicates
#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

#The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

#Note: Elements of a[] and b[] are not necessarily distinct.
#Examples:

#Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
#Output: [1, 2, 3]
#Explanation: Union set of both the arrays will be 1, 2 and 3.
#Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
#Output: [1, 2, 3, 4, 5, 6]
#Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.
#Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
#Output: [1, 2]
#Explanation: Union set of both the arrays will be 1 and 2.
#Constraints:
#1 ≤ a.size(), b.size() ≤ 106
#0 ≤ a[i], b[i] ≤ 105

def findUnion(a, b):
        n1=len(a)
        n2=len(b)
        i,j=0,0
        res=[];added=set()
        while(i<n1 and j<n2):
            if a[i]<b[j]:
                if a[i] not in added:
                    res.append(a[i])
                    added.add(a[i])
                i+=1
            elif a[i]>b[j]: 
                if b[j] not in added:
                     res.append(b[j])
                     added.add(b[j])
                j+=1
            elif a[i]==b[j]:
                if a[i] not in added:
                    res.append(a[i])
                    added.add(a[i])
                i+=1
                j+=1

        while i<n1:
            if a[i] not in added:
                added.add(a[i])
                res.append(a[i])
            i+=1
        while j<n2:
            if b[j] not in added:
                added.add(b[j])
                res.append(b[j]) 
            j+=1
        return res