"""

Solution :
Kadane's algorithm (left -> right)
Kadane's algorithm (right -> left)
Find the max sum 
"""

def solution(A):
    # Implement your solution here
    n = len(A)
    kadaneLR = [0 for i in range(n)]
    kadaneRL = [0 for i in range(n)]

     # Kadane de gauche à droite
    for i in range(1,n-1):
        kadaneLR[i] = max(kadaneLR[i-1]+A[i], 0)
    # Kadane de droite à gauche
    for i in range(n-2,0,-1):
        kadaneRL[i] = max(kadaneRL[i+1]+A[i], 0)

    # Trouver le max : cacher un nomber (A[i]) et prendre le max de la somme des subarray qui finissent juste avant et juste après
    maxDoubleSum = 0

    for i in range(1, n-1):
        maxDoubleSum = max(maxDoubleSum, kadaneLR[i-1]+kadaneRL[i+1])

    return maxDoubleSum
