#include <stdio.h>


void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

int partition(int *arr, int low, int high) {
  int pivot = low;
  int i = pivot+1;
  int j = high;

  while(1) {
    while (i <= high && arr[i] <= arr[pivot]) {
      i += 1;
    }

    while (j >= low && arr[j] > arr[pivot]) {
      j -= 1;
    }

    if (i > j) {
      break;
    }

    swap(&arr[i], &arr[j]);
  }
  swap(&arr[j], &arr[pivot]);

  return j;
}

void quickSort(int *arr, int low, int high) {
  if (low < high) {
    int pivot_index = partition(arr, low, high);
    quickSort(arr, low, pivot_index-1);
    quickSort(arr, pivot_index+1, high);
  }
}

void printArr(int *arr, int n) {
  for (int i=0; i < n; i++) {
    printf("%d ", arr[i]);
  }
}

int main() {
  int arr[4] = {10, 12, 5, 7};
  int n = sizeof(arr)/sizeof(arr[0]);

  quickSort(arr, 0, n-1);
  printArr(arr, n);
}
