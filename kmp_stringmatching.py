

def BuiltArray(pattern):
  i,j,n=1,0,len(pattern)
  temp=[0]*n
  while i<n:
    if pattern[i]==pattern[j]:
      temp[i]=j+1
      i+=1
      j+=1
    else:
      if j==0:
        temp[i]=0
        i+=1
      else:
        j=temp[j-1]
  return temp

  
def KMP(text,pattern):
  temp=BuiltArray(pattern)
  print(temp)
  i,j=0,0
  while i<len(text) and j<len(pattern):
    if text[i]==pattern[j]:
      i+=1
      j+=1
    else:
      if j==0:
        i+=1
      else:
        j=temp[j-1]
  return j==len(pattern)

def main():
  text="abcxabcdabcdabcy"
  pattern="abcdabcy"
  print(KMP(text,pattern))
  
main()

