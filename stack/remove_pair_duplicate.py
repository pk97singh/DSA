#Remove All Adjacent Duplicates
def remove_pair_duplicate(s:str):
    n=len(s)
    i=0
    stack=[]
    for i in range(i,n):
        if stack and stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        
    return ''.join(stack)
     

print(remove_pair_duplicate('abbaca'))
