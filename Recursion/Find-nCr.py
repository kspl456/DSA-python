#Find nCr

def nCr(n,r):
    if n==r:
        return 1
    if r==1:
        return n
    return nCr(n-1,r-1) + nCr(n-1,r)
