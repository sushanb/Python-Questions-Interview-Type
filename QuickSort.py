def QuickSort(L):
    return MainQS(L, 0, len(L) -1)
    
def GetPivot(L, high, low):
    pivot = high
    mid = (high + low) // 2
    if L[low] < L[mid]:
        if L[mid] < L[high]:
            pivot = mid
    else:
        if L[low] < L[high]:
            pivot = low
    return pivot

def Partition(L, low, high):
    pivot_index = GetPivot(L, high, low)
    pivot_value = L[pivot_index]
    L[low], L[pivot_index] = L[pivot_index], L[low]
    forward = low
    for i in range(low, high + 1):
        if L[i] < pivot_value:
            forward += 1
            L[i], L[forward] = L[forward] , L[i]
    L[low], L[forward] = L[forward] , L[low]
    return forward

def PartitionWithPivotFunction(L, low, high):
    pivot = L[high] #Assumes that the element in high index is pivot
    start_index = low #Select the starting index as index 
    for i in range(low, high): # A for procedure that gives us a correct index of the pivot number
        if L[i] <= pivot: #If the element is less than pivot, shift it near to start
            L[i], L[start_index] = L[start_index], L[i] #Swapping in Python
            start_index += 1 #Increment the counter
    L[high], L[start_index] = L[start_index], L[high] #Swapping in Python and the value in end get the right place
    return start_index

def MainQS(L, low, high):
    if low < high:
        par_in = PartitionWithPivotFunction(L, low, high)
        MainQS(L, low, par_in -1)
        MainQS(L, par_in + 1, high)
    return L
print QuickSort([1,-10,-20,6,18])
