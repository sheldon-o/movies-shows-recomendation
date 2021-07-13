from array import *
test=array("i",[2,4,1,5,8,7,19,11,3,12,15,13,16,14,18])


def MERGE(test,p,q,r):
    n1=q-p+1
    n2=r-q
    L=array("i",[])
    R=array("i",[])
    for i in range(n1):
        L[i]=test[p+i-1]
    for j in range(n2):
        R[j]=test[q+j]


    i=1
    j=1
    for k in range(p,r):
        if L[i]<R[j]:
            test[k]=L[i]
        else:
            test[k]=R[j]
            j=j+1
def MERGE_SORT(test,p,r):
    if p<r:
        q=(p+r)/2
        MERGE_SORT(test,p,q)
        MERGE_SORT(test,q+1,r)
        MERGE(test,p,q,r)
p=0
r=len(test)
MERGE_SORT(test,p,r)
print(test)



