"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Solution : Aller jusqu'à la racine carré du nombre considéré
"""
def solution(N):
  # Implement your solution here
  # initialization
  factors = 0
  i = 1    # start counting factors
  while i * i < N:
    if N % i ==0:
      factors += 2
    i += 1    # special case: perfect square

  if i*i == N:
    factors += 1    # return the count of factors
  return factors
