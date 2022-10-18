#Implement Merge Sort Algorithm with all the necessary functions.

def merge(low,high): # function take Two parameter
    # to store result
    result = [] 
    i ,j=0,0
    # merging algorithm
    while i<len(low) and j < len(high):  
        if(low[i]<high[j]):
           result.append(low[i])
           i +=1
        else:
           result.append(high[j]) 
           j +=1
    result +=low[i:]
    result +=high[j:]
    return result


def mergesort(lst):
    # return is lst has only one value, cause it is already sorted
    if(len(lst)<=1): 
       return lst
    mid = int(len(lst)/2)
    low = mergesort(lst[:mid]) #calling function recursively
    high = mergesort(lst[mid:])#calling function recursively
    return merge(low,high)

arr = [2,5,-2,0,7,9,5,-8,-6,4]
print(mergesort(arr))