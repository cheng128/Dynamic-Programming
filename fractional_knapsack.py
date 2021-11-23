""" pseudo code

Let arr[1..n][1..2] be a array that contain value and weight of n items

FRACTIONAL_KNAPSACK(arr, W)

    Let cp[1...n][1..2] be a new array
    
    for i = 1 to n
        cp[i][1] = arr[i][1] / arr[i][2]
        cp[i][2] = arr[i][2]
        
    sort cp into ascending order by cp[1...n][1]
    
    total_value = 0
    total_weight = 0
    
    for i = 1 to n
        if total_weight + cp[i][2] <= W:
            total_value += cp[i][1] * cp[i][2]
            total_weight += cp[i][2]
        else
            total_value += cp[i][1] * (W - total_weight)
    
    return total_value
"""

def fractional_knapsack(arr, W):
    cp = [[i[0]/i[1], i[1]] for i in arr]
    cp = sorted(cp, reverse=True)

    total_value = 0
    total_weight = 0
    
    for value, weight in cp:
        if total_weight + weight <= W:
            total_value += value * weight
            total_weight += weight
        else:
            total_value += value * (W - total_weight)
    return total_value

def main():
    arr = [[6, 1], [10, 2], [12, 3]] 
    W = 5
    answer = fractional_knapsack(arr, W)
    print('answer:', answer)

if __name__ == '__main__':
    main()