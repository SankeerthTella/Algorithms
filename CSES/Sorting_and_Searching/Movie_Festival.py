def helper(timings,n):
    i,res,cur=0,0,0
    for i in range(n):
        if timings[i][0]>=cur:
            cur=timings[i][1]
            res+=1
    print(res)


def main():
    n=int(input())
    timings=[]
    for _ in range(n):
        temp=[int(i) for i in input().split()]
        timings.append(temp)

    timings.sort(key=lambda x:x[1])
    return helper(timings,n)
main()

