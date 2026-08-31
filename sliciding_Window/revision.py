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
 
    
    
