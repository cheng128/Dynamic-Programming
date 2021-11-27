""" pseudo code
Time Complexity: O(nW)

Let arr[1...n][1..2] be a array that contain value and weight of n items
W be the maximum total weight we can carry

ZERO_ONE_KNAPSACK(arr, W)

    Let S[0...arr.length][0...W] be a new array with value 0
    
    for i = 1 to arr.length
        for k = 1 to W
            if arr[i][2] > k
                S[i][k] = S[i-1][k]
            else
                S[i][k] = max{S[i-1][k], arr[i][1] + S[i-1][k - arr[i][2]]}
                
    return S[-1][-1]
    
"""

def zero_one_knapsack(arr, W):
    # S will be used to save the largest value we can get
    # when we limit the weight with k we can carry and 
    # we can only choose from the first item to ith item
    S = [[0 for i in range(W+1)] for j in range(len(arr)+1)]
    
    for i in range(1, len(arr)+1):
        for k in range(1, W+1):
            # this item is too heavy, we can't take it since we can only carry k
            if arr[i-1][1] > k:
                S[i][k] = S[i-1][k]
            else:
                # we can choose to take this item or not
                # we left (k - weight of this item) to take first to (i-1)th item
                take = arr[i-1][0] + S[i-1][k - arr[i-1][1]]
                not_take = S[i - 1][k]
                S[i][k] = max(take, not_take)
    return S[-1][-1]

def main():
    arr = [[6, 1], [10, 2], [12, 3]] 
    W = 5
    answer = zero_one_knapsack(arr, W)
    print("answer:", answer)

if __name__ == '__main__':
    main()