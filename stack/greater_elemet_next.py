my_arr=[1,2,4,3,5]



def greater_elemt_next(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    i=0
    
    
    for i in range(n-1,-1,-1):
        while stack and arr[i]>stack[-1]:
            stack.pop()

        if stack:
          res[i]=stack[-1]
        
        stack.append(arr[i])
    
    return res
 
 
print(greater_elemt_next(my_arr))    
    
    
    
    
    
    
