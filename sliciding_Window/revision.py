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

#quoesstion 3:Longest Substring with K Uniques
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        h=0
        l=0
        freq={}
        n=len(s)
        res=float('-inf')
        for i in range(h,n):
            freq[s[h]]=freq.get(s[h],0)+1
            h=h+1
            
            while len(freq)>k:
               freq[s[l]]=freq[s[l]]-1
               if freq[s[l]]==0:
                   del freq[s[l]]
               
               l=l+1
            if len(freq)==k:
                length=h-l
                res=max(length,res)
            
                
                 
            
        if len(freq)<k:
            return -1
        return res

#quoestion 4: fruit basket

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        h=0
        freq={}
        res=float('-inf')

        n=len(fruits)
        for i in range(0,n):
            freq[fruits[i]]=freq.get(fruits[i],0)+1

            while (len(freq)>2):
                freq[fruits[l]]-=1
                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l=l+1
            h=h+1
            
            length=h-l
            res=max(res,length)
        return res
        
                
                
                
            
        
         

    
    
