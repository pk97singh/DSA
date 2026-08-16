my_lst=[1,1,2,3,4]

low=0
high=0
freq={}
res=0
n=len(my_lst)

#find the longest subarray whith almost 2 disctinct number  .
#A farmer have a garden of fruit from left to right , we can pick atmost 2 distinct fruits.
# find total number of fruits which can be collected.


while (high < n):
    freq[my_lst[high]]=freq.get(my_lst[high],0)+1
    
    
    
    while len(freq)>2:
        freq[my_lst[low]]-=1
        if freq[my_lst[low]] == 0:
            del freq[my_lst[low]]
        low=low+1
        
    res=max(res,(high-low+1))
    
    high=high+1
    
    
print(res)
