#quoestion 1.
arr=[100,200,300,400]
k=2 

#fixed ,

l=0
h=k-1
n=len(arr)
sum=0
res=float('-inf')

for i in range(l,h+1):
    sum=sum+arr[i]
    

while (h<n):
    res=max(sum,res)
    h=h+1
    l=l+1
    
    if h==n :
        break;
    
    sum=sum+arr[h]-arr[l-1]
   
print(sum)

#quoestion 2.
nums = [2,3,1,2,4,3]
target = 7

#variable , 
h=0
l=0
n=len(nums)
sum=0
res=float('inf')

while(h<n):
    sum=sum+nums[h]
    h=h+1
    
    
    while(sum>=target):  
        len=h-l
        res=min(res,len)
        sum=sum-nums[l]
        l=l+1
        
if res==float('inf'):
        print(0)
         
print(res)

         

    
    
