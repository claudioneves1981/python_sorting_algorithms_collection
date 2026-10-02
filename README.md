# Python Sorting Algorithms Collection

This repository contains a comprehensive collection of sorting algorithms implemented in Python. The implementations range from standard production-grade algorithms and classic divide-and-conquer strategies to distribution sorts, esoteric/joke algorithms, and educational sorting methods.

---

## 📋 Quick Summary Table

| Algorithm | Category | Average Time Complexity | Worst-case Time Complexity | Space Complexity |
| :--- | :--- | :---: | :---: | :---: |
| **Merge Sort** | Divide & Conquer | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Bottom-Up Merge Sort** | Divide & Conquer | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Quick Sort (Hoare)** | Divide & Conquer | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |
| **Heap Sort** | Selection Sort | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ |
| **Tim Sort** | Hybrid | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Insertion Sort** | Insertion Sort | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Cocktail Shaker Sort** | Exchange Sort | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Odd-Even Sort** | Exchange Sort | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Adaptive Shell Sort** | Insertion/Diminishing | $O(n \log n)$ | $O(n^2)$ | $O(1)$ |
| **Library Sort** | Insertion / Gapped | $O(n \log n)$ | $O(n^2)$ | $O(n)$ |
| **Pancake Sort** | Selection / Reversal | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Counting Sort** | Non-Comparison | $O(n + k)$ | $O(n + k)$ | $O(k)$ |
| **Bucket Sort** | Distribution Sort | $O(n + k)$ | $O(n^2)$ | $O(n + k)$ |
| **Bogosort** | Esoteric / Random | $O((n + 1)!)$ | Unbounded ($O(\infty)$) | $O(1)$ |
| **Slowsort** | Esoteric / Reluctant | $O(n^{\frac{\log n}{2 \log 2}})$ | $O(n^{\frac{\log n}{2 \log 2}})$ | $O(\log n)$ |
| **Stalin Sort** | Esoteric / Lossy | $O(n)$ | $O(n)$ | $O(n)$ |

---

## 🧠 Detailed Algorithm Descriptions

### 1. Efficient Comparison Sorts

#### **Merge Sort (Top-Down)**
* **Method:** `merge_sort(arr)`
* **Description:** A classic recursive divide-and-conquer algorithm. It divides the array into two halves, recursively sorts them, and then merges the two sorted halves back together using a helper function `merge`.
* **Characteristics:** Stable, reliable $O(n \log n)$ performance, but requires $O(n)$ extra space.

#### **Bottom-Up Merge Sort**
* **Method:** `bottom_up_merge_sort(arr)`
* **Description:** An iterative variation of Merge Sort. Instead of dividing recursively, it starts by merging small sub-arrays of width $1$, then $2, 4, 8, \dots$ until the entire array is sorted.
* **Characteristics:** Eliminates recursion stack overhead while maintaining $O(n \log n)$ time efficiency.

#### **Quick Sort (Hoare Partition)**
* **Method:** `quick_sort_hoare(arr)`
* **Description:** Selects a pivot element and partitions the array such that elements smaller than the pivot go to the left and larger elements go to the right. This implementation uses **Hoare's Partitioning Scheme**, which uses two pointers moving towards each other and performs fewer swaps on average than Lomuto's scheme.
* **Characteristics:** Fast in practice, in-place sorting, but has a worst-case time complexity of $O(n^2)$ if poor pivots are chosen.

#### **Heap Sort**
* **Method:** `heap_sort(arr)`
* **Description:** Converts the array into a Max-Heap data structure. It repeatedly extracts the maximum element (root) and swaps it with the last unsorted position, then heapifies the remaining structure.
* **Characteristics:** Guaranteed $O(n \log n)$ time complexity and operates in-place ($O(1)$ auxiliary space).

---

### 2. Hybrid & Variant Sorts

#### **Tim Sort**
* **Method:** `tim_sort(arr, RUN=4)`
* **Description:** A hybrid algorithm derived from Merge Sort and Insertion Sort (used natively by Python and Java). It breaks the array into small chunks ("runs"), sorts them using Insertion Sort, and merges them using an iterative merge step.
* **Characteristics:** Highly optimized for real-world data containing pre-sorted sequences.

#### **Library Sort (Gapped Insertion Sort)**
* **Method:** `library_sort(arr)`
* **Description:** An optimization of Insertion Sort that uses binary search to find insertion points, followed by shifting elements. Conceptually related to leaving gaps on library shelves to make inserting new books faster.
* **Characteristics:** Improves search times for insertion, though shifting elements still takes $O(n)$ in standard array representations.

#### **Adaptive Shell Sort**
* **Method:** `adaptive_shell_sort(arr)`
* **Description:** A variation of Shell Sort that dynamically adapts the gap size based on the number of swaps performed during a pass. If swaps exceed the array size $n$, it reduces the gap faster ($\text{gap} / 1.5$ vs $\text{gap} / 2.5$).
* **Characteristics:** Improves performance on partially sorted or randomly ordered arrays by dynamically adjusting step sizes.

---

### 3. Simple & Exchange Sorts

#### **Insertion Sort**
* **Method:** `insertion_sort(arr, left, right)`
* **Description:** Iteratively builds the final sorted array one element at a time by shifting larger elements to the right and inserting the current item in its correct position.
* **Characteristics:** Efficient for very small arrays or nearly sorted data ($O(n)$ best case).

#### **Cocktail Shaker Sort**
* **Method:** `cocktail_sort(arr)`
* **Description:** A bidirectional variation of Bubble Sort. It passes through the list in both directions alternately: left-to-right (moving the largest element to the end) and right-to-left (moving the smallest element to the beginning).
* **Characteristics:** Solves the "turtles" problem in Bubble Sort, where small values near the end of the array move slowly.

#### **Odd-Even Sort (Brick Sort)**
* **Method:** `odd_even_sort(arr)`
* **Description:** A variation of Bubble Sort originally developed for parallel processing. It compares all (odd, even) indexed adjacent pairs in one pass, followed by all (even, odd) indexed pairs in the next.
* **Characteristics:** Simple to implement concurrently in multi-processor environments.

#### **Pancake Sort**
* **Method:** `pancake_sort(arr)`
* **Description:** Unlike standard sorts that use swaps, Pancake Sort reverses prefixes of the array (like flipping a stack of pancakes). It locates the maximum element, flips it to the front, and then flips it into its final position at the back.
* **Characteristics:** Unique constraint-based sorting problem ($O(n^2)$ time).

---

### 4. Non-Comparison & Distribution Sorts

#### **Counting Sort**
* **Method:** `counting_sort(arr)`
* **Description:** Counts the frequency of each distinct value in the array and reconstructs the sorted output based on the count array.
* **Characteristics:** Operates in linear time $O(n + k)$ (where $k$ is the maximum value in the array). Best suited for non-negative integer arrays with small ranges.

#### **Bucket Sort**
* **Method:** `bucket_sort(arr)`
* **Description:** Distributes elements into numerical "buckets" based on their values. Each bucket is then sorted individually (using built-in sorting), and the results are concatenated.
* **Characteristics:** Fast linear-time performance $O(n + k)$ when input elements are uniformly distributed.

---

### 5. Esoteric & Joke Sorts

#### **Bogosort (Stupid Sort)**
* **Method:** `bogo_sort(arr)`
* **Description:** Randomly shuffles the array until it happens to land in sorted order.
* **Characteristics:** Purely theoretical/joke algorithm. Average time complexity is $O((n + 1)!)$, and it can run indefinitely.

#### **Slowsort**
* **Method:** `slow_sort(arr, i, j)`
* **Description:** A humorous algorithm based on the principle of "Multiply and Surrender" (a parody of Divide and Conquer). It recursively breaks down the array, swaps extreme values, and reluctantly sorts remaining subsets.
* **Characteristics:** Deliberately highly inefficient recursive structure with exponential time complexity.

#### **Stalin Sort**
* **Method:** `stalin_sort(arr)`
* **Description:** A "lossy" sorting algorithm. It iterates through the array in a single pass ($O(n)$) and immediately removes any element that is not in non-decreasing order relative to the maximum seen so far.
* **Characteristics:** Guaranteed $O(n)$ speed, but alters the size of the array by eliminating out-of-order elements.

---

## 🚀 Execution & Benchmarking

### Running the Code

Ensure you have Python installed (Python 3.6+ recommended):

```bash
python sorts.py
```

### Script Workflow
1. Creates a sample array: `[38, 27, 43, 3, 9, 82, 10]`.
2. Measures execution times using `time.perf_counter()`.
3. Displays the output array and execution duration (in seconds) for each sorting algorithm.

> **💡 Developer Tip:** Many algorithms in the script sort the array **in-place**. If you run multiple in-place algorithms sequentially on the same array reference, subsequent algorithms will receive an already-sorted array. To benchmark accurately, pass a fresh copy of the array (e.g., `sample_array.copy()`) to each function.
