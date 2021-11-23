""" pseudo code

LCS(s, t)
    Let M[0...s.length, 0...t.length] be a new array with value 0
    Let C[0...s.length, 0...t.length] be a new array
    
    for i = 1 to s.length
        for j = 1 to t.length
            if s_i == t_i
                M[i, j] = M[i-1, j-1] + 1
                C[i, j] = '↖'
            elif M[i-1, j] > M[i, j-1]
                M[i, j] = M[i-1, j]
                C[i, j] = '↑'
            else
                M[i, j] = M[i, j-1]
                C[i, j] = '←'
                
    return M[-1][-1]
    
"""

def LCS(s, t):
    M = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    C = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                C[i][j] = 'same'
            elif M[i][j-1] > M[i-1][j]:
                M[i][j] = M[i][j-1]
                C[i][j] = 'left'
            else:
                M[i][j] = M[i-1][j]
                C[i][j] = 'up'
                
    return M, C

def find_subsequence(s, C):
    i, j = -1, -1
    result = C[i][j]
    subsequence = ''
    while result:
        if result == 'same':
            subsequence = s[j] + subsequence
            i -= 1
            j -= 1
            result = C[i][j]
        elif result == 'left':
            j -= 1
            result = C[i][j]
        else:
            i -= 1
            result = C[i][j]
    return subsequence

def main():
    s = "GTCA"
    t = "GTACG"

    length, record = LCS(s, t)
    print("length:", length[-1][-1])
    subsequence = find_subsequence(s, record)
    print("subsequence:", subsequence)
    
if __name__ == '__main__':
    main()