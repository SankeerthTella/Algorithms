def helper(st):
    n=len(st)
    res=1
    i=0
    while i<n-1:
        temp=1
        j=i+1
        while j<n:
            if st[i]==st[j]:
                temp+=1
            else:
                break
            j+=1
        i=j
        res=max(res,temp)

    print(res)

def main():
    st=input()
    return helper(st)
main()
