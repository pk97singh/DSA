#find min of roated array
def roate_array_min(arr):
     l=0
     n=len(arr)
     r=len(arr)-1
     while (l<=r):
         m=(l+r)//2
         
         if (arr[m]>arr[n-1]):
             l=m+1
         else:
             res=m
             r=m-1
     return arr[res]
 
print(roate_array_min([5,6,7,1,2,3,4]))
