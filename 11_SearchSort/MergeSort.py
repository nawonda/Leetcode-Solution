'''
Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
'''

def mergeSort(alist):
    #base do nothing

    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


#merge two sorted array

A = [1,3,8,15,60]
B = [0,3,4,6,11]

m = len(A)
n = len(B)

A.extend(B)

while(m > 0 and n >0):
    
    if(A[m-1]>B[n-1]):        
        A[m+n-1] = A[m-1]
        m -= 1
    else:
        A[m+n-1] = B[n-1]
        n -= 1

while(n > 0):
    A[n-1] = B[n-1]
    n -=1
        
print A
        

