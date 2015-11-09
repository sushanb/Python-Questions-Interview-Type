def QuickSelect(L, k):
    return MainQS(L, 0, len(L) -1 , k)
    
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

def MainQS(L, low, high, k):
    par_in = Partition(L, low, high)
    if low == high:
        return L[low]
    else:
        if k == par_in:
            return L[par_in]
        elif k < par_in:
            return MainQS(L, low, par_in -1, k)
        else:
            return MainQS(L, par_in + 1, high, k)
