arr = [1, 3, 5, 7, 9, 11, 13]
target = 11 

l=0 
r=len(arr)-1

while l<=r:
    mid= (l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1 
    else:
        r=mid-1
        
        
if not found:
    print(-1)
    
   
