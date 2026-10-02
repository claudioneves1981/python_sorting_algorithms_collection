# Python Sorting Algorithms Collection

A comprehensive collection of sorting algorithms implemented in Python. This repository includes standard, efficient algorithms used in production as well as esoteric/humorous sorting algorithms for educational and comparison purposes.

## 📋 Included Algorithms

| Algorithm | Average Time Complexity | Worst-Case Time Complexity | Space Complexity | Type |
| :--- | :--- | :--- | :--- | :--- |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Comparison / Divide & Conquer |
| **Quick Sort (Hoare)** | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Comparison / Divide & Conquer |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | Comparison / Heap |
| **Tim Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Hybrid (Insertion + Merge) |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(k)$ | Non-Comparison / Integer |
| **Bucket Sort** | $O(n + k)$ | $O(n^2)$ | $O(n)$ | Distribution |
| **Comb Sort** | $O(n \log n)$ | $O(n^2)$ | $O(1)$ | Comparison / Exchange |
| **Adaptive Shell Sort** | $O(n \log n)$ | $O(n^2)$ | $O(1)$ | Comparison / Insertion |
| **Insertion Sort** | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Comparison / Insertion |
| **Cocktail Shaker Sort** | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Comparison / Exchange |
| **Odd-Even Sort** | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Comparison / Exchange |
| **Library Sort** | $O(n \log n)$ | $O(n^2)$ | $O(n)$ | Comparison / Insertion |
| **Pancake Sort** | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Comparison / Reversal |
| **Bottom-Up Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Iterative Merge |
| **Slowsort** | $O(n^{\frac{\log n}{2.7188}})$ | $O(n^{\frac{\log n}{2.7188}})$ | $O(\log n)$ | Multiply and Surrender |
| **Bogo Sort** | $O((n+1)!)$ | Unbounded | $O(1)$ | Stochastic / Esoteric |

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.7+** (No external dependencies required; uses built-in modules `math`, `random`, and `time`).

### Running the Code

1. Clone or download the repository.
2. Run the script using Python:

```bash
python sorting_algorithms.py
```

---

## 💻 Example Output

```text
Original array: [38, 27, 43, 3, 9, 82, 10]
=================================================================
Merge Sort            : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001820 s
Cocktail Sort         : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000850 s
Heap Sort             : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001540 s
Counting Sort         : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001010 s
Bogo Sort             : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00341200 s
Bucket Sort           : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001400 s
Library Sort          : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000720 s
Slow Sort             : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00004510 s
Odd-Even Sort         : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000930 s
Tim Sort              : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001250 s
Insertion Sort        : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000540 s
Bottom Up Merge Sort  : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001680 s
Quick Sort (Hoare)    : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001120 s
Adaptive Shell Sort   : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000890 s
Pancake Sort          : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00001180 s
Comb Sort             : [3, 9, 10, 27, 38, 43, 82] | Time: 0.00000780 s
```

---

## 📝 Important Notes

1. **Array Mutability:** The execution harness uses `sample_array.copy()` for each iteration to guarantee that every algorithm sorts an unsorted array, providing fair comparison time metrics.
2. **Performance Warning:** Algorithms like `Bogo Sort` and `Slowsort` have extreme time complexities. Running them on arrays larger than 10 elements may result in extremely long execution times or freezing.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
