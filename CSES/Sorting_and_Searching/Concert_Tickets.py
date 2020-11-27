from bisect import bisect_right
 
def helper(tickets,customers,n,m):
    tickets.sort()
    visited=[False]*len(tickets)
    for cust in customers:
        i=bisect_right(tickets,cust)
 
        if i:
 
            if i==n and visited[i-1]==False:
                print(tickets[i-1])
                tickets.remove(tickets[i-1])
            else:
                i-=1
                if i>=0:
                    print(tickets[i])
                    tickets.remove(tickets[i])
                else:
                    print("-1")
        else:
            print("-1")
 
def main():
    n,m=[int(i) for i in input().split()]
    tickets=[int(i) for i in input().split()]
    customers=[int(i) for i in input().split()]
    return helper(tickets,customers,n,m)
main()
