def main():
    n=int(input())
    arr=[int(i) for i in input().split()]
    curr,res=0,float('-inf')
    for num in arr:
        if curr<0:
            curr=0
        curr+=num
        res=max(res,curr)
    print(res)
main()
