k=2 
my_lst= [100,200,300,400]

#find the subarray with max sum of size k in given array. 
#solution : subarray identifed then sum keyword identified : slicing window quoestion 
#since , its an fixed window , so low=0 high=1

#find sum of first window .
res=0
low = 0
high=1 #high =k-1
sum=0 
n=len(my_lst)
for i in range (low ,high+1):  #will give sum from first window as it's our start
    sum=sum+my_lst[i]
    
while (high<n):
    res=max(res,sum) #find max sum by comparing
    low=low+1 
    high=high+1 
    
    if high==n: #in case it should break
        break
    
    sum=sum-my_lst[low-1]+my_lst[high] #sub last and add new 
    

print(res)
    
    


    

