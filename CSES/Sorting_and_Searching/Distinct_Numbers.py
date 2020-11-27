def helper(lst,n):
    visited=set()
    for i in lst:
        visited.add(i)
    print(len(visited))
def main():
    n=int(input())
    lst=[int(i) for i in input().split()]
    return helper(lst,n)
main()
