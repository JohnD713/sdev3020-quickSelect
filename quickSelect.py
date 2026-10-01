import random
import timeit
import psutil
#--------------------------------------------------------------------------------

def create_unique_random_numbers():
    numbers = random.sample(range(0, 10000000), 10)
    return numbers

def linearSearch(set, goal):
    for i in range(len(set)):
        if set[i] == goal:
            return f"Found at: {i}"

def binarySearch(set, goal):
    left, right = 0, len(set) - 1
    while left <= right:
        mid = (left + right) // 2
        if set[mid] == goal:
            return mid
        elif set[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1
    return

def quickSelect(set, left, right, goal):
    if (goal > 0 and goal <= right - left + 1):
        # partition the set
        index = partition(set, left, right)
        
        # if our index position is the goal, return the number at that index
        if index - left == goal - 1:
            return set[index]
        
        # if index(number of items in partition) is less than the goal, recur the left
        if index - left > goal - 1:
            return quickSelect(set, left, index - 1, goal)
            
        # otherwise recur the right partition
        return quickSelect(set, index + 1, right, goal - index + left - 1)

def partition(set, left, right):
    # set pivot to rightmost value
    pivot = set[right]
    # set the iterator to leftmost position
    iterator = left
    
    for j in range(left, right):
        # is current value less than the pivot?
        if set[j] <= pivot:
            # move behind pivot
            set[iterator], set[j] = set[j], set[iterator]
            # move up the iterator
            iterator += 1
    # move the pivot to current position
    set[iterator], set[right] = set[right], set[iterator]
    
    return iterator
#--------------------------------------------------------------------------------
if __name__ == "__main__":
    unsorted = create_unique_random_numbers()
    sorted = unsorted
    sorted.sort()  

    mBefore = psutil.Process().memory_info().rss / (1024 * 1024)
    cpuBefore = psutil.Process().cpu_times()

#-----------------------------------------------------------------------------------------------------

    linearSearch(unsorted, sorted[0])
    
    mAfterLinear = psutil.Process().memory_info().rss / (1024 * 1024)
    cpuAfterLinear = psutil.Process().cpu_times()

    binarySearch(unsorted, sorted[0])

    mAfterBinary = psutil.Process().memory_info().rss / (1024 * 1024)
    cpuAfterBinary = psutil.Process().cpu_times()

#-----------------------------------------------------------------------------------------------------

    quickSelect(unsorted, 3, 0, len(unsorted) - 1)

    mAfterQuick = psutil.Process().memory_info().rss / (1024 * 1024)
    cpuAfterQuick = psutil.Process().cpu_times()

#-----------------------------------------------------------------------------------------------------
    
    print("--Linear--")
    print(f"Time: {timeit.timeit('linearSearch(unsorted, sorted[0])', globals=globals(), number=1)}")
    print(f"Memory before: {mBefore} MB")
    print(f"Memory after: {mAfterLinear} MB")
    print(f"CPU Before: User: {cpuBefore[0]} | System: {cpuBefore[1]}")
    print(f"CPU After: User: {cpuAfterLinear[0]} | System: {cpuAfterLinear[1]}")


    print("--Binary--")
    print(f"Time: {timeit.timeit('binarySearch(unsorted, sorted[0])', globals=globals(), number=1)}")
    print(f"Memory before: {mBefore} MB")
    print(f"Memory after: {mAfterBinary} MB")
    print(f"CPU Before: User: {cpuBefore[0]} | System: {cpuBefore[1]}")
    print(f"CPU After: User: {cpuAfterBinary[0]} | System: {cpuAfterBinary[1]}")

    print("--Quick--")
    print(f"Time: {timeit.timeit('quickSelect(unsorted, 0, len(unsorted) - 1, 3)', globals=globals(), number=1)}")
    print(f"Memory before: {mBefore} MB")
    print(f"Memory after: {mAfterQuick} MB")
    print(f"CPU Before: User: {cpuBefore[0]} | System: {cpuBefore[1]}")
    print(f"CPU After: User: {cpuAfterQuick[0]} | System: {cpuAfterQuick[1]}")