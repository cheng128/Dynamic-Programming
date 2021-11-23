
def Fib(n):
    if n == 0 or n == 1:
        return n
    else:
        F = [0 for i in range(n+1)]
        F[0] = 0
        F[1] = 1
        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]
        return F[n]
    
def main():
    answer = Fib(6)
    print('answer:', answer)

if __name__ == '__main__':
    main()