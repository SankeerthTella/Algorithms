from bisect import bisect_right
def main():
    n=int(input())
    arr=[]
    for i in input().split():
        pos= bisect_right(arr,int(i))
        if pos>=len(arr):
            arr+=[int(i)]
        else:
            arr[pos]=int(i)
    print(len(arr))
        
main()
