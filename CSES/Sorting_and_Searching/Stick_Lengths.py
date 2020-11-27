def main():
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    mid=arr[(n-1)//2]
    res=0
    for num in arr:
        res+=abs(num-mid)
    print(res)
main()
