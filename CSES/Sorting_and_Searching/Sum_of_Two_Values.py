def main():
    n,x=[int(i) for i in input().split()]
    temp,arr=0,{}
    for i in input().split():
        if x-int(i) in arr:
            print(arr[x-int(i)],end=" ")
            print(temp+1)
            return
        arr[int(i)]=temp+1
        temp+=1
    print("IMPOSSIBLE")
    return
main()
