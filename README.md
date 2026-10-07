# Sorting Algorithms Suite in Python

A benchmark suite featuring **20 sorting algorithms** implemented in Python. The project includes classical comparison sorts, non-comparison algorithms, hybrid methods, esoteric/educational sorting algorithms, and gap-sequence variants like Shell Sort with Sedgewick's sequence.

---

## 📋 Included Algorithms

### 1. Standard Comparison Sorts
* **Merge Sort**: Divide-and-conquer algorithm with recursive splitting and merging.
* **Heap Sort**: Selection sort variant using a binary heap data structure.
* **Insertion Sort**: Simple insertion-based sorting for small datasets.
* **Quick Sort (Hoare Partition)**: Fast in-place quicksort using Hoare's dual-pointer partitioning scheme.
* **Bottom-Up Merge Sort**: Iterative merge sort working bottom-up without recursion.

### 2. Gap & Shell Sort Variants
* **Adaptive Shell Sort**: Shell sort with dynamically adjusted gap increments based on swap counts.
* **Shell Sort (Sedgewick)**: Shell sort variant using Sedgewick's gap sequence $4^k + 3 \times 2^{k-1} + 1$, offering significantly improved empirical step bounds over traditional halved gaps.
* **Comb Sort**: Bubble sort improvement using dynamic gap sizes scaled by a shrink factor ($1.3$).

### 3. Non-Comparison & Distribution Sorts
* **Counting Sort**: Integer sorting algorithm based on frequency count arrays.
* **Bucket Sort**: Uniform distribution sorting method partitioning inputs into range buckets.

### 4. Hybrid & Advanced Sorts
* **Tim Sort**: Hybrid algorithm combining insertion sort on small runs with bottom-up merge sort.
* **Block Sort**: In-place merge sort algorithm dividing arrays into $\sqrt{N}$ blocks, sorting locally with insertion sort and merging in place.
* **Weak Heap Sort**: Heap sort variant running with relaxed structural properties to reduce total key comparisons.
* **Library Sort (Gapped Insertion Sort)**: Insertion sort optimization using binary search for position lookup and element shifts.

### 5. Concurrent / Exchange Variants
* **Cocktail Shaker Sort**: Bidirectional bubble sort iterating both forward and backward.
* **Odd-Even Sort (Parallel Bubble Sort)**: Exchange algorithm operating in odd and even index comparison passes.
* **Pancake Sort**: Sorting algorithm restricted to reversing sub-arrays (prefix flips).

### 6. Educational & Esoteric Sorts
* **Bogo Sort**: Randomized sorting algorithm shuffling until sorted ($O((N+1)!)$ complexity).
* **Slow Sort**: Multiply-and-surrender esoteric sort designed as a pessimistic recursive algorithm.
* **Spaghetti Sort**: Conceptual linear-time sorting simulation implemented via max-element extraction.

---

## 📊 Algorithmic Complexities

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Merge Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Yes |
| **Heap Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | No |
| **Weak Heap Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | No |
| **Quick Sort (Hoare)** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(\log N)$ | No |
| **Tim Sort** | $O(N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Yes |
| **Insertion Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes |
| **Shell Sort (Sedgewick)** | $O(N \log N)$ | $O(N^{4/3})$ | $O(N^{4/3})$ | $O(1)$ | No |
| **Adaptive Shell Sort** | $O(N \log N)$ | $O(N^{3/2})$ | $O(N^2)$ | $O(1)$ | No |
| **Comb Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(1)$ | No |
| **Block Sort** | $O(N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | Yes |
| **Counting Sort** | $O(N + K)$ | $O(N + K)$ | $O(N + K)$ | $O(K)$ | Yes |
| **Bucket Sort** | $O(N + K)$ | $O(N + K)$ | $O(N^2)$ | $O(N)$ | Yes |
| **Library Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(N)$ | No |
| **Cocktail Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes |
| **Odd-Even Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes |
| **Pancake Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | No |
| **Spaghetti Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | No |
| **Slow Sort** | $O(N^{\log N / 2})$ | $O(N^{\log N / 2})$ | $O(N^{\log N / 2})$ | $O(N)$ | No |
| **Bogo Sort** | $O(N)$ | $O((N+1)!)$ | $\infty$ | $O(1)$ | No |

---

## 🚀 How to Run

### Requirements
* Python 3.7 or higher (uses built-in `math`, `random`, and `time` modules).

### Execution

Run the main file directly in your terminal:

```bash
python sorting_algorithms.py
