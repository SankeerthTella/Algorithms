def main():
    n=int(input())
    total=(n*(n+1))//2
    lst=[int(i) for i in input().split()]
    temp=sum(lst)
    print(total-temp)
main()
