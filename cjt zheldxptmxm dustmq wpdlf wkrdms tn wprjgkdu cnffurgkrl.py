def solution(arr):
    small=min(arr)
    arr.remove(small)
    length=len(arr)
    if length==0:
        arr.append(-1)
    return arr
