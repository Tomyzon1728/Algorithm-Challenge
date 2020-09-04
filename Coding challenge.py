ls=[]
times=int(input ("Enter number of times to add to list:"))
a=0
while a<times:
    a+=1
    entry=input("Enter a num:")
    ls.append(entry)
    if entry=="stop":
        break
print(ls)
target=int(input ("Enter target number:"))
print (target)
"""
#ls_=[i for i in ls]
#print (ls_)
for i,j in enumerate (ls):
    print(i,j)
a=target - i
print(a)
if a not in ls:
    ls[j]=i
else:
    print([ls[a]],i)
"""