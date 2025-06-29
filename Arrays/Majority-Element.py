#Majority Element

#Used Boyer-Moore Majority Vote Algorithm.

def majorityElement(nums):
    res, count =0,0
    for i in nums:
        if count==0:
            res=i
        count+= (1 if i==res else -1)
    return res