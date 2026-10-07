import random
import time
import math

# --- Sorting Algorithms ---

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

def merge_alt(arr, left, mid, right):
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
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

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

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def counting_sort(arr):
    if not arr:
        return arr
    top = max(arr)
    count = [0] * (top + 1)
    for num in arr:
        count[num] += 1
    
    i = 0
    for j in range(0, top + 1):
        while count[j] > 0:
            arr[i] = j
            i += 1
            count[j] -= 1
    return arr

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def bucket_sort(arr):
    if not arr:
        return arr
    num_buckets = len(arr)
    max_val, min_val = max(arr), min(arr)
    val_range = (max_val - min_val) if max_val != min_val else 1
    
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_val) / val_range * (num_buckets - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()
    
    write_index = 0
    for bucket in buckets:
        for num in bucket:
            arr[write_index] = num
            write_index += 1
    return arr

def library_sort(arr):
    for i in range(1, len(arr)):
        left = 0
        right = i

        while left < right:
            mid = (left + right) >> 1
            if arr[mid] <= arr[i]:
                left = mid + 1
            else:
                right = mid
        for j in range(i, left, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
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
    sorted_status = False

    while not sorted_status:
        sorted_status = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_status = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_status = False

    return arr

def insertion_sort(arr, left=None, right=None):
    if left is None and right is None:
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
            while j > left and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
    return arr

def size_temp(size, n, arr):
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            merge_alt(arr, left, mid, right)
        size *= 2

def tim_sort(arr, RUN=4):
    n = len(arr)
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))
    size = RUN
    size_temp(size, n, arr)
    return arr

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
        
    if len(arr) > 1:
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

def pancake_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        mi = find_max(arr, curr_size)
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size - 1)
    return arr

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        else:
            is_sorted = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False

    return arr

def weak_heap_sort(arr):
    n = len(arr)
    def sift_down(root, end):
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            if left <= end and arr[left] > arr[largest]:
                largest = left
            if right <= end and arr[right] > arr[largest]:
                largest = right
            if largest == root:
                break
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n - 1)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(0, i - 1)
    return arr

def spaghetti_sort(arr):
    n = len(arr)
    for end in range(n - 1, 0, -1):
        max_index = 0
        for i in range(1, end + 1):
            if arr[i] > arr[max_index]:
                max_index = i
        if max_index != end:
            arr[max_index], arr[end] = arr[end], arr[max_index]
    return arr

def block_sort(arr):
    n = len(arr)

    def merge_in_place(start,mid,end):
        left, right = start,mid
        while left < right and right < end:
            if arr[left] <= arr[right]:
                left += 1
            else:
                value = arr[right]
                index = right
                while index > left:
                    arr[index] = arr[index - 1]
                    index -= 1
                arr[left] = value
                left += 1
                right += 1

    block_size = max(2, int(math.sqrt(n)))
    for i in range(0,n,block_size):
        hi = min(i + block_size, n)
        for a in range(i +1,hi):
            j = a
            while j > i and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
    width = block_size
    while width < n:
        for start in range(0,n,width*2):
            mid = min(start + width, n)
            end = min(start + 2 * width, n)
            if mid < end:
                merge_in_place(start,mid,end)
        width *= 2
    return arr

def shell_sort_sedgewick(arr):
    n = len(arr)
    gaps = [1]
    k = 1
    while True:
        gap = 4**k + 3 * 2**(k-1)+1
        if gap >= n:
            break
        gaps.append(gap)
        k+=1
    for gap in reversed(gaps):
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                j -= gap
    return arr




# --- Execution and Benchmarking ---

if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)
    print("-" * 60)

    algorithms = [
        ("Merge Sort", merge_sort),
        ("Cocktail Sort", cocktail_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort),
        ("Bogo Sort", bogo_sort),
        ("Bucket Sort", bucket_sort),
        ("Library Sort", library_sort),
        ("Slow Sort", slow_sort),
        ("Odd-Even Sort", odd_even_sort),
        ("Tim Sort", tim_sort),
        ("Insertion Sort", lambda a: insertion_sort(a, None, None)),
        ("Bottom Up Merge Sort", bottom_up_merge_sort),
        ("Quick Sort (Hoare)", quick_sort_hoare),
        ("Adaptive Shell Sort", adaptive_shell_sort),
        ("Pancake Sort", pancake_sort),
        ("Comb Sort", comb_sort),
        ("Weak Heap Sort", weak_heap_sort),
        ("Spaghetti Sort", spaghetti_sort),
        ("Block Sort", block_sort),
        ("Shell Sort (Sedgewick)", shell_sort_sedgewick)
    ]

    for name, func in algorithms:
        # Passa uma cópia nova da array para cada algoritmo
        arr_copy = sample_array.copy()
        
        start = time.perf_counter()
        sorted_array = func(arr_copy)
        end = time.perf_counter()
        
        execution_time = end - start
        print(f"{name:<22}: {sorted_array} | Time: {execution_time:.8f} s")