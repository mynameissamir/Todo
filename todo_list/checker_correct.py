# your code goes here
def search(arr,target):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            h=mid-1
        else:
            l=mid+1
    return(-1)
    
test=int(input())
for i in range(test):
    arr=[int(i) for i in input().split()]
    #arr.sort()
    sE=int(input())
    elements=[int(i) for i in input().split()]
    for j in elements:
        print(search(arr,j))