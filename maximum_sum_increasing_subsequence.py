""" pseudo code

MSIS(A)
    n = A.length
    Let dp[1....n] be a new array
    
    for i = 1 to n
        dp[i] = A[i]
    
    for i = 2 to n
        for j = 1 to i
            if A[i] > A[j] && dp[j] + A[i] > dp[i]
                dp[i] = dp[j] + A[i]
    
    max_num = -inf
    for i = 1 to n
        if dp[i] > max_num
            max_num = dp[i]
    
    return max_num
"""


def MSIS(A):
    n = len(A)
    dp = [i for i in A]
    for i in range(1, n):
        for j in range(0, i+1):
            if A[i] > A[j] and dp[j] + A[i] > dp[i]:
                dp[i] = A[i] + dp[j]
    return max(dp)
    
def main():
    A = [1, 101, 2, 3, 100, 4, 5]
    answer = MSIS(A)
    print("answer:", answer)
    
if __name__ == '__main__':
    main()