def greater_element_prev(s1):
    stack=[]
    rslt=[]
    for ch in s1:
        while stack and ch>stack[-1]:
            stack.pop() 
        if not stack:
            rslt.append(-1)
        else:
            rslt.append(stack[-1])
            
        stack.append(ch)    
        
            
           
                
    return rslt 

arr=[4,1,2,5,3]
print(greater_element_prev(arr))
