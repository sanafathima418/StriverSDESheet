from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    
    # Time Complexity : O(NLOGN) + O(N)
    # Space Complexity: O(1)
    
    # 1. Sort both arrays - Don't care about mixing up indexes of a train
    # This is cause we only need times of entry and exit
    at.sort()
    dt.sort()
    
    plats_needed = 1
    min_count = 1
    i = 1
    j = 0
    
    # Slow(Dep) and Fast Pointer(Arr)
    while(i < n and j < n):
        if at[i] <= dt[j]:
            # 2. If a train arrives before previous train departure(after sorting), increase demand and i
            plats_needed += 1
            i += 1
        else:
            # 3. If train departure(after sorting) is greater than next train arrival, decrease demand and j
            plats_needed -= 1
            j += 1
        # Update min plats needed after every iteration
        min_count = max(min_count,plats_needed)
    return min_count
        

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
