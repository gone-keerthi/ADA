# Quick sort Algorithm using all necessary functions
# function to find the partition position
def partition(array, start_i, end_i):
  # choose the rightmost element as pivot
  pivot = array[end_i]
  # pointer for greater element
  i = start_i - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(start_i, end_i):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[end_i]) = (array[end_i], array[i + 1])
  # return the position from where partition is done
  return i + 1
# function to perform quicksort
def quickSort(array, start_i, end_i):
  if start_i < end_i:
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, start_i, end_i)
    # recursive call on the left of pivot
    quickSort(array, start_i, pi - 1)
    # recursive call on the right of pivot
    quickSort(array, pi + 1, end_i)
data = [8, 7, 6, 1, 0, 9, 2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

