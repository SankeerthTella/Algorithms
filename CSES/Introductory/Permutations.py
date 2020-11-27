def helper(n):
    if n==1:
        print(1," ")
        return
    res=[]
    if n<=3:
        print("NO SOLUTION")
        return 
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
    for i in range(1,n+1):
        if i%2==1:
            print(i,end=" ")

    
def main():
    n=int(input())
    return helper(n)
main()
