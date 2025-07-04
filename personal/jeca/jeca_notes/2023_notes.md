# 2023 Answer sheet

## Semaphore
- A semaphore is a program used to implement process synchroniation like mutual exclusion to prevent situations like race condition.
- It is initialized with a intial value which denotes no of process can access critical section at a time.
- It provides two operations:
  - wait: When a process enters a critical section it decrements semaphore value.
  - signal: When a provcess leaves critical section it increments semaphore value.
- When semaphore value is zero, any process that performs wait operation will be blocked until the another process increments semaphore value with signal operation.
- Types of semaphores:
  - Binary semaphores: It is also known as mutex lock, used to implement mutual exclusion. It is initialized with 1 and can have only two values 0 and 1.
  - Counting Semaphore: It can be used to control access to a given resource consisting of a finite number of instances. The semaphore is initialized to the number of resources available.

## Binary Tree
- A binary tree has at most two children per node.
- Inserting data without order can cause problems during searching.
- Data structures should organize data for easy search, insertion, and deletion.

## Binary Search Tree (BST)
- BSTs are binary trees with restriction of having smaller elements on the left and larger elements on the right of the root.
- BSTs facilitate easier searching, insertion, and deletion compared to Binary Tree.
- **Worst-case scenario:** If data is skewed (right or left), the tree behaves like a linked list, leading to O(n) complexity.

### Binary Search Tree Traversals

- Inorder Traversal: Traverse left subtree then visit the root and then traverse the right subtree.
```c++
void printInorder(Node* node) {
    if (node == NULL) return;

    // Traverse left subtree
    printInorder(node->left);

    // Visit node
    cout << node->data << " ";

    // Traverse right subtree
    printInorder(node->right);
}
```

- Preorder Traversal: Visit the root then traverse left subtree and then traverse the right subtree.
```c++
void printPreOrder(Node* node)
{
    if (node == NULL) return;

    // Visit Node
    cout << node->data << " ";

    // Traverse left subtree
    printPreOrder(node->left);

    // Traverse right subtree
    printPreOrder(node->right);
}
```

- Postorder Traversal: Traverse left subtree then traverse the right subtree and then visit the root.
```c++
void printPostOrder(Node* node)
{
    if (node == NULL) return;

    // Traverse left subtree
    printPostOrder(node->left);

    // Traverse right subtree
    printPostOrder(node->right);

    // Visit node
    cout << node->data << " ";
}
```

## AVL Tree
- AVL trees are balanced BSTs with restriction of tree's height to log n, where n = number of nodes.
- These trees is used for efficient search operations with guarantee of O(log n) time complexity.
- The goal is to prevent the height from exceeding log n to avoid increased time complexity.
- AVL trees must have Balance Factor values between -1, 0 and +1 for each node.
- **Balance Factor** is calculated as the height of the left subtree minus the height of the right subtree.

## Create AVL Tree

### Unbalanced BST Cases
- Case 1: RR (Right Right) Unbalance
  - Example: Inserting 8, 9, 10 sequentially.
  - The balance factor of node 8 becomes -2 after inserting 10, indicating an RR unbalance.
  - Solution: Perform a single anticlockwise rotation at node 9.
  - After rotation, the tree is rebalanced with 9 as the root, and 8 and 10 as its left and right children, respectively.

- Case 2: LL (Left Left) Unbalance
  - Example: Inserting 10, 9, 8 sequentially.
  - The balance factor of node 10 becomes 2 after inserting 8, indicating an LL unbalance.
  - Solution: Perform a single clockwise rotation at node 9.
  - After rotation, the tree is rebalanced with 9 as the root, and 8 and 10 as its left and right children.

- Case 3: RL (Right Left) Unbalance
  - Example: Inserting 10, 12, 11 sequentially.
  - The balance factor of node 10 becomes -2 after inserting 11, indicating an RL unbalance.
  - Solution: Requires two rotations.
    - First, convert RL into RR by rotating nodes 12 and 11, making 11 the parent of 12.
    - Second, perform a single anticlockwise rotation at node 11.
  - After rotations, the tree is balanced with 11 as the root, and 10 and 12 as its left and right children.

- Case 4: LR (Left Right) Unbalance
  - Example: Inserting 10, 8, 9 sequentially.
  - The balance factor of node 10 becomes 2 after inserting 9, indicating an LR unbalance.
  - Solution: Requires two rotations.
    - First, convert LR into LL by rotating nodes 8 and 9, making 9 the parent of 8.
    - Second, perform a single clockwise rotation at node 9.
  - After rotations, the tree is balanced with 9 as the root, and 8 and 10 as its left and right children.

## Sorting

### Bubble Sort

- **Compare Adjacent Elements:** Repeatedly step through the list, comparing each pair of adjacent elements.
- **Swap if Needed:** If a pair is in the wrong order (i.e., the first is greater than the second), swap them.
- **Repeat Passes:** Continue making passes through the list until no swaps are needed, which means the list is sorted.
- **Time Complexity:** Worst-case and average time complexity is O(n²), it's inefficient for large datasets.
- [Link](https://www.geeksforgeeks.org/bubble-sort-algorithm/)

### Insertion Sort

- **Build Sorted Sublist:** Start from the second element and insert each element into its correct position in the sorted part of the list.
- **Shift Elements:** Compare the current element with those before it and shift larger elements one position to the right.
- **Insert Element:** Place the current element in the correct position.
- **Time Complexity:** Worst-case time complexity is O(n²), but it's efficient for small or nearly sorted datasets.
- [Link](https://www.geeksforgeeks.org/insertion-sort-algorithm/)

### Selection Sort

- **Find Minimum:** In each pass, find the smallest (or largest) element from the unsorted portion.
- **Swap:** Swap it with the first unsorted element.
- **Shrink Unsorted Part:** Move the boundary between sorted and unsorted parts one step forward.
- **Time Complexity:** Always O(n²) regardless of input, and it makes the minimum number of swaps.
- [Link](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)

### Quick Sort

```
function QUICK_SORT(array, low, high)
    if low < high then
        pivot_index = PARTITION(array, low, high)
        QUICK_SORT(array, low, pivot_index - 1)   // Sort left part
        QUICK_SORT(array, pivot_index + 1, high)  // Sort right part
    end if
end function

function PARTITION(array, low, high)
    pivot = array[low]                 // Choose pivot (can be low, high, or random)
    i = low + 1
    j = high

    while true do
        // Move i to the right until finding element >= pivot
        while i <= high and array[i] <= pivot do
            i = i + 1
        end while

        // Move j to the left until finding element <= pivot
        while j >= low and array[j] > pivot do
            j = j - 1
        end while

        // If pointers cross, break the loop
        if i > j then
            break
        end if

        // Swap elements at i and j
        SWAP(array[i], array[j])
    end while

    // Swap pivot with element at j to place pivot in correct position
    SWAP(array[low], array[j])

    return j  // New pivot index
end function
```

- Divide and conquer approach.
- [Link](https://www.youtube.com/watch?v=tWCaFVJMUi8&t=9s)
- Space Complexity: O(1)
- Time Complexity: Average: O(n log n), worst Case: O(n^2) (happens when the pivot is always the smallest or largest element), best Case: O(n log n), with balanced partitions.

### Merge Sort

```
MERGE_SORT(A, p, r)
    if p < r then
        q = floor((p + r) / 2)          // Find middle index
        MERGE_SORT(A, p, q)             // Sort left half
        MERGE_SORT(A, q + 1, r)         // Sort right half
        MERGE(A, p, q, r)               // Merge the two sorted halves
    end if
end function

MERGE(A, p, q, r)
    n1 = q - p + 1                      // Length of left subarray
    n2 = r - q                          // Length of right subarray

    create array L[1 .. n1 + 1]
    create array R[1 .. n2 + 1]

    for i = 1 to n1
        L[i] = A[p + i - 1]             // Copy left half into L
    end for

    for j = 1 to n2
        R[j] = A[q + j]                 // Copy right half into R
    end for

    L[n1 + 1] = ∞                       // Sentinel value
    R[n2 + 1] = ∞                       // Sentinel value

    i = 1
    j = 1

    for k = p to r
        if L[i] ≤ R[j] then
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
        end if
    end for
end function
```

- Divide and conquer approach.
- Space Complexity: O(n) extra space is used for merging.
- Time Complexity: Average: O(n log n), worst Case: O(n log n), best Case: O(n log n), merging takes linear time and there are log n levels of division.

## Graph

- Breath First search (BFS)
    - Time Complexity: O(V+E), V = vertex, E = edges
    - Space Complexity: O(V), V = adjacency list

- Depth First search (DFS)
    - Time Complexity: O(V+E), V = vertex, E = edges
    - Space Complexity: O(V), V = adjacency list

- Kahn's Topological Sort
    - Time Complexity: O(V+E), V = vertex, E = edges
    - Space Complexity: O(V), V = adjacency list

- DFS Topological Sort
    - Time Complexity: O(V+E), V = vertex, E = edges
    - Space Complexity: O(V), V = adjacency list

- Dijkstra's Algo
    - Time Complexity: O((V+E) log V), V = vertex, E = edges
    - Space Complexity: O(V + E), V = adjacency list, E = queue

- Kruskal's Algo
    - Time Complexity: O(E log E), E = edges
    - Space Complexity: O(V + E), V = adjacency list, E = queue
