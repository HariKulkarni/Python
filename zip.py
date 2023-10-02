a=[1,2,3]

b=[3,4,5]
res=[]
i=0
for e1,e2 in zip(a,b):
    res+=[e1+e2]
print(res)
