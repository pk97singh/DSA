arr = [40, 50, 60, 70, 10, 20, 30]
target = 20

def search_rotated_array_opt(arr,tar):
    l=0
    r=len(arr)-1
    n=len(arr)
    
    while (l<=r):
        m=(l+r)//2
        if arr[m]==tar:
            return m 
        if arr[m]>arr[n-1]: #bring me first part of array [40, 50, 60, 70]
            if arr[m]<tar:
                l=m+1
            else:
                if arr[0]>tar:
                    l=m+1
                else:
                    r=m-1
        
        else :  #[10, 20, 30]
            if arr[m]>tar:
                r=m-1
            else:
                if arr[n-1]<tar:
                    r=m-1
                else:
                    l=m+1
                    
    return -1

print(search_rotated_array_opt(arr,target))
                    
                    
                
                 
