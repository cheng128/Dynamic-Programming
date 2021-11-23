""" pseudo code

Let p[0...n] contains the row and column of matrices
p[0] = #row of matrix 1
p[1] = #column of matrix 1 and #row of matrix 2
...
p[n-1] = #column of matrix n-2 and #row of matrix n
p[n] = #column of matrix n

MATRIX_CHAIN(p)
    Let s[1...n, 1...n] c[1...n-1, 2...n] be new arrays

    for l = 2 to n
        for i = 1 to n - l + 1
            j = i + l - 1
            s[i, j] = inf
            c[i, j] = i
            for k = i to j-1 
                r = s[i, k] + s[k+1, j] + p[i-1]p[k]p[j]
                if r < s[i, j]
                    s[i, j] = r
                    c[i, j] = k
    return s[1, n]
"""

def matrix_chain(p):
    n = len(p)
    s = [[0 for i in range(n)] for j in range(n)]
    c = [[0 for i in range(n-2)] for j in range(n-1)]
    
    for i in range(n):
        s[i][i] = 0
    
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            s[i][j] = float('inf')
            c[i][j-2] = i
            for k in range(i, j):
                r = s[i][k] + s[k+1][j] + p[i-1] * p[k] * p[j]
                if r < s[i][j]:
                    s[i][j] = r
                    c[i][j-2] = k        
    return s, c

def print_matrix(s, c):
    print([i for i in range(1, len(s))])
    for idx, line in enumerate(s):
        if idx != 0 and set(line) != 0:
            print(line[1:], idx)
    print('-'*10)
    print([i for i in range(2, len(s))])
    for idx, line in enumerate(c):
        if idx != 0 and set(line) != 0:
            print(line, idx)

# TODO
# def build_chain():

def main():
    p = [2, 3, 5, 4, 2]
    s, c = matrix_chain(p)
#     print_matrix(s, c)
    print('answer:', s[1][-1])

if __name__ == '__main__':
    main()