def helper(arrival,leave,n):
    i,j,res,cur=0,0,float('-inf'),0
    while i<n and j<n:
        if arrival[i]<leave[j]:
            cur+=1
            i+=1
        else:
            cur-=1
            j+=1
        res=max(res,cur)
    print(res)


def main():
    n=int(input())
    arrival=[]
    leave=[]
    for _ in range(n):
        a,l=[int(i) for i in input().split()]
        arrival.append(a)
        leave.append(l)
    arrival.sort()
    leave.sort()
    return helper(arrival,leave,n)
main()
