"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
"""

import collections
def solution(A):
    # Implement your solution here
    
    ### Trouver tous les leaders et les stocker dans leaders
    n = len(A) 
    threshold = n//2

    dictOcc = collections.Counter(A) 

    leaders = []
    for k in dictOcc:
        if dictOcc[k]> threshold:
            leaders.append(k)
    
    # Compter le nombre de equileaders
    equileader = 0
    for l in leaders:
        #print("leader :", l)
        nbleaderLeft = 0
        for index in range(n):
            if A[index] == l:
                nbleaderLeft += 1
            if nbleaderLeft > (index+1)//2 and dictOcc[l]-nbleaderLeft > (n-index-1)//2:
                #print(index,nbleaderLeft)
                equileader += 1
    return equileader
