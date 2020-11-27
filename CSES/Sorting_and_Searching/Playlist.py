def main():
    n=int(input())
    arr=[int(i) for i in input().split()]
    visited=set()
    start,end,res=0,0,0
    while end<n:
        if arr[end] in visited:
            while arr[end] in visited and start<n:
                visited.remove(arr[start])
                start+=1
        visited.add(arr[end])
        res=max(res,end-start+1)
        end+=1
    print(res)
    return
  
main()
