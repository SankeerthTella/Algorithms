def helper(weights,limit,n):
    start,end,res=0,n-1,0
    weights.sort()
    while start<end:
        if weights[start]+weights[end]<=limit:
            res+=1
            start+=1
            end-=1
        else:
            res+=1
            end-=1
    if start==end:
        print(res+1)
        return
    print(res)
def main():
    n,limit=[int(i) for i in input().split()]
    weights=[int(i) for i in input().split()]
    return helper(weights,limit,n)

main()
