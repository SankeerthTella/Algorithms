def helper(person,appt,k,n,m):
    res=0
    i,j=0,0
    person.sort()
    appt.sort()
    while i<n and j<m:
        if abs(person[i]-appt[j])<=k:
            res+=1
            i+=1
            j+=1
        elif person[i]<appt[j]:
            i+=1
        else:
            j+=1
    print(res)

def main():
    n,m,k=input().split()
    person=[int(i) for i in input().split()]
    appt=[int(i) for i in input().split()]
    return helper(person,appt,int(k),int(n),int(m))
    
main()
