from itertools import permutations
n=int(raw_input())
#l=list(map(int,raw_input().split(" "))
#l= [int(x) for x in raw_input().split()] 
#l.sort(reverse=True)
#x=int(raw_input())
#if(x<=n and x>0):
 #   print l[x-1]

perm=permutations(range(1,n),2)
perm=list(perm)
print perm
for i in perm:
    print i,
