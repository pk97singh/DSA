#substring with distinct k
s = "aabacbebebe"
k = 3

freq={}
res=0
low=0
rslt=""
high=0 
n=len(s) 

while high<n:
    freq[s[high]]=freq.get(s[high],0)+1
    
    
    while len(freq)>k:
        freq[s[low]]-=1
        if freq[s[low]]==0:
            del freq[s[low]]


        low=low+1
    
    if len(freq)==k:
        length=high-low+1
       # res=max(res,length)  #in case we want only length not substring, uncomment 
        
        if length>res:
            res=length
            rslt=s[low:high+1]
        
    high=high+1
    
print(res)  
print(rslt)     
