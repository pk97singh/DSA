my_lst=[3,4,5,10,10,10,10,25,27]
tar=10
#find the output as index of first index where we have 10 and last index where we have 10

def duplicate_index(arr,tar):
    
    l=0
    r=len(arr)-1
    rslt=[]
    first=-1
    last=-1
    while (l<=r):
        m=(l+r)//2
        
        if arr[m]<tar:
            l=m+1
            
        elif arr[m]>tar:
             r=m-1
        else:
            first=m
            r=m-1
    l=0
    r=len(arr)-1        
    while (l<=r):
        m=(l+r)//2
        
        if arr[m]<tar:
            l=m+1
            
        elif arr[m]>tar:
             r=m-1
        else:
            last=m
            l=m+1
    
    return [first,last]
        

print(duplicate_index(my_lst,tar))
