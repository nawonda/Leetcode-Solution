'''
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.
'''
def bubble_sort(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        #
        for k in range(n):
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp