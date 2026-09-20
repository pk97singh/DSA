my_arr=[30,40,60,50]
#o/p: [1,1,0,0]
def find_warmer_day(arr1):
    n=len(arr1)
    stack=[]
    res=[0]*4
    count=0
    for i in range(0,n):
        
        while stack and arr1[i]>arr1[stack[-1]]:
            prev=stack.pop()
            print(prev)
            res[prev]=i-prev
            
            
        stack.append(i)
        print(stack)
        
    return res
    

print(find_warmer_day(my_arr))
