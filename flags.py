"""

Correctness ok but performance : 28% A REVOIR
"""
def solution(A):
    # Implement your solution here
    n = len(A)
    if n < 3:
        return 0

    peaks = []
    for i in range(1,n-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    
    if len(peaks)==0:
        return 0
    if len(peaks)==1:
        return 1

    # KEY to reduce complexity :
    # On a 2 facteurs limitants : le nombre de peaks ET la racine carré de la longueur de A car on veut que
    # potentialK * (potentialK - 1) <= n car on veut fit k-1 fois la distance k dans N (les flags doivent être espacés de k distance)
    for potentialK in range(min(len(peaks), int(n **0.5)+1), 0, -1):
        currentNumberFlags = 1
        # index du dernier peak sur lequel on a posé un flag dans la liste peaks
        indexLastFlag=0
        for i in range(1,len(peaks)):
            if peaks[i]-peaks[indexLastFlag] >= potentialK and currentNumberFlags < potentialK:
                currentNumberFlags +=1 
                indexLastFlag = i
        #print(potentialK, currentNumberFlags)
        if currentNumberFlags == potentialK:
            return currentNumberFlags
        potentialK -=1

    return currentNumberFlags
