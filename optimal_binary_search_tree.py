""" pseudo code

OBST(p, q, n)

    Let s[1...n+1, 0...n], w[1...n+1, 0...n] be new arrays
    
    for i = 1 to n+1
        w[i, i-1] = q[i-1]
        s[i, i-1] = q[i-1]
    
    for l = 2 to n
        for i = 1 to n - l + 1
            j = i + l - 1
            w[i, j] = w[i, j-1] + p[j] + q[j]
            s[i, j] = inf
            for k = i+1 to j
                t = s[i, k-1] + s[k+1, j] + w[i, j]
                if t < s[i, j]
                    s[i, j] = t
    return s[1, n]
"""

# TODO use a matrix to record split point and reconstruct the optimal binary tree

def OBST(p, q, n):
    
    w = [[0 for i in range(n+1)] for j in range(n+2)]
    s = [[0 for i in range(n+1)] for j in range(n+2)]

    for i in range(1, n+2):
        w[i][i-1] = q[i-1]
        s[i][i-1] = q[i-1]

    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            w[i][j] = round(w[i][j-1] + p[j] + q[j], 3)
            s[i][j] = round(s[i][i-1] + s[i+1][j] + w[i][j], 3)
            for r in range(i+1, j+1):
                t = s[i][r-1] + s[r+1][j] + w[i][j]
                if t < s[i][j]:
                    s[i][j] = round(t, 3)
    return s[1][n]

def main():
    p = [0, 0.15, 0.1, 0.05, 0.1, 0.2]
    q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    
    # because first item in p is a dummy value
    n = len(p) - 1 
    answer = OBST(p, q, n) 
    print('answer:', answer)

if __name__ == '__main__':
    main()