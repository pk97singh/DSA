#find min size of subarray whose sum equals target
#solution : since keyword like subarray comes then follow by sum 
#variable window 
#low=0 high=0 in case of variable window   

#logic : keep adding until target exceed then start removing

my_lst=[1,2,4,4]
target=4
def min_subarray_sum_target(my_lst,tar):
    sum=0
    low=0 
    high=0 
    res=float('inf')
    
    n=len(my_lst) 
    
    while (high<n):
        sum=sum+my_lst[high] 
        
        
        while(sum>=tar):
            length=high-low+1 
            res=min(res,length) 
            
            sum=sum-my_lst[low] 
            low=low +1 
        high=high+1 
        
    return res   

print(min_subarray_sum_target(my_lst,target))
