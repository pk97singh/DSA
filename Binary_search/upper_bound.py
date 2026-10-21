arr = [1, 3, 5, 7, 9, 11, 13]
tar=11 
# requirement : greater or equal to tar

def greater_or_equal(tar,arr):
    l=0
    r=len(arr)-1 
    rslt=-1
    
    while (l<=r):
        m=(l+r)//2
        
        if arr[m]<=tar:
            l=m+1
            
        else:
            rslt=m 
            r=m-1
    return rslt

print(greater_or_equal(tar,arr))
        
