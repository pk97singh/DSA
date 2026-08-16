my_lst= [100,200,300,400]
def find_max_sum_subarray (k):
    low=0
    high=k-1 
    n=len(my_lst)
    res=float('-inf') 
    sum=0 
    
    for i in range(low ,high+1):
        sum=sum+my_lst[i] #create our first window   
        
    while (high<n):
        res=max(res,sum)
        low=low+1 
        high=high+1 
        
        if high==n:
            break 
        
        sum=sum-my_lst[low -1 ]+my_lst[high]
        
        
    return res 

print(find_max_sum_subarray(2))
