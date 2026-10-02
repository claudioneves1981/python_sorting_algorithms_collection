import math
import random
import time

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_alt(arr,left,mid,right):
    i = left
    j = mid + 1
    k = left    
    temp = [0] * len(arr)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
        
    

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            array_comparision_swap(arr, i)
            swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start - 1, -1):
            array_comparision_swap(arr, i)
            swapped = True

        start += 1

    return arr

def array_comparision_swap(arr, i):
     if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
       
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def counting_sort(arr):
    maximo = max(arr)
    count = [0] * (maximo + 1)
    for num in arr:
        count[num] += 1
    
    i = 0
    for val in range(0,maximo):
        while count[val] > 0:
            arr[i] = val
            i += 1
            count[val] -= 1
    return arr

def stalin_sort(arr):
    if len(arr) == 0:
        return arr
    
    kept = [arr[0]]
    max_so_far = arr[0] 

    for i in range(1, len(arr)):
        if arr[i] >= max_so_far:
            kept.append(arr[i])
            max_so_far= arr[i]
    return kept

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def bucket_sort(arr):
    
    max_value = max(arr)
    buckets = [[] for _ in range(max_value + 1)]

    for num in arr:
        bucketIndex = math.floor((num - 1)/3)
        buckets[bucketIndex].append(num)

    for bucket in buckets:
        bucket.sort()
    
    write_index = 0
    for bucket in buckets:
        for num in bucket:
            arr[write_index] = num
            write_index += 1
    return arr

def library_sort(arr):
    for i in range(1,len(arr)):
        left = 0
        right = i

        while left < right:
            mid = (left + right) >> 1
            if arr[mid] <= arr[i]:
                left = mid + 1
            else:
                right = mid
        for j in range(i,left, -1):
            [arr[j], arr[j -1]] =[arr[j-1],arr[j]]
    return arr


def slow_sort(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1
    if i >= j:
        return arr
    m = (i + j) >> 1
    slow_sort(arr, i, m)
    slow_sort(arr, m + 1, j)
    if arr[m] > arr[j]:
        arr[m], arr[j] = arr[j], arr[m]
    slow_sort(arr, i, j - 1)
    return arr
    
def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr

def insertion_sort(arr,left,right):
    if left == None and right == None:
        for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
    else:
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j - 1] >  arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j -= 1
    return arr


def tim_sort(arr, RUN = 4):
    n = len(arr)
    for i in range(0, n, RUN):
        insertion_sort(arr,i,min(i+RUN - 1, n -1))
    size = RUN
    size_temp(size, n, arr)
    return arr

def size_temp(size, n, arr):
    while size < n:
        for left in range(0,n, 2 * size):
            mid = min(left+ size-1, n -1)
            right = min(left+2*size-1,n -1)
            merge_alt(arr,left, mid, right)
        size *=2 
   


def bottom_up_merge_sort(arr):
    n = len(arr)
    width = 1
    size_temp(width, n, arr)
    return arr

def quick_sort_hoare(arr):
    def hoare_partition(low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def quick_sort_recursive(low, high):
        if low >= high:
            return
        p = hoare_partition(low, high)
        quick_sort_recursive(low, p)
        quick_sort_recursive(p + 1, high)
    quick_sort_recursive(0, len(arr) - 1)
    return arr

def adaptive_shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        swap_count = 0
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
                swap_count += 1
            if swap_count > n:
                gap = int(gap / 1.5)
            else:
                gap = int(gap / 2.5)
    return arr

def pancake_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        mi = find_max(arr, curr_size)
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size - 1)
    return arr

def find_max(arr, n):
    mi = 0
    for i in range(1, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def flip(arr, i):
    left, right = 0, i
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)

    start = time.perf_counter()
    sorted_array = merge_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Merge Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = cocktail_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Cocktail Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = heap_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Heap Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = counting_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Counting Sort):", sorted_array, f"Time Execution {execution_time:.10f}")
 
    start = time.perf_counter()
    sorted_array = stalin_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Stalin Sort):", sorted_array,f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = bogo_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (bogo_sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = bucket_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Bucket Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = library_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Library Sort):", sorted_array,f"Time Execution {execution_time:.10f}" )
    
    start = time.perf_counter()
    sorted_array = slow_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Slow Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = odd_even_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Odd-Even Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = tim_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Tim Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = insertion_sort(sample_array, None, None)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Insertion Sort):", sorted_array, f"Time Execution {execution_time:.10f}")
    
    start = time.perf_counter()
    sorted_array = bottom_up_merge_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Buttom Up Merge Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = quick_sort_hoare(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Quick Sort Hoare):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = adaptive_shell_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Adaptive Shell Sort):", sorted_array, f"Time Execution {execution_time:.10f}")

    start = time.perf_counter()
    sorted_array = pancake_sort(sample_array)
    end = time.perf_counter()
    execution_time = end - start
    print("Sorted array (Pancake Sort):", sorted_array, f"Time Execution {execution_time:.10f}")