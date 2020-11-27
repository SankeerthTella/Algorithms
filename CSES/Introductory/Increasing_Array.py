def helper(arr,n):
    res=0
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            res+=arr[i-1]-arr[i]
            arr[i]=arr[i-1]
    print(res)

def main():
    n=int(input())
    lst=[int(i) for i in input().split()]
    return helper(lst,n)
main()
