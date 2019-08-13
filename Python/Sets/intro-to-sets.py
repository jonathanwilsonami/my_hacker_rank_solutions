def average(array):
    # your code goes here
    mySet = set(array)
    return(sum(mySet)/len(mySet))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
