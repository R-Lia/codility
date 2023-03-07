import collections
def solution(A):
    if not A:
        return -1
    
    n = len(A)
    threshold = n//2

    
    dictOcc = collections.Counter(A)

    if max(dictOcc.values()) <= threshold:
        return -1
    
    for i,number in enumerate(A) :
        if dictOcc[number]> threshold:
            return i
