#include <stdio.h>


void merge(int *arr, int low, int mid, int high) {
  int tmp[high - low + 1];
  int left = low;
  int right = mid+1;
  int k = 0;

  while (left <= mid && right <= high) {
    if (arr[left] < arr[right]) {
      tmp[k] = arr[left];
      left += 1;
    } else {
      tmp[k] = arr[right];
      right += 1;
    }
    k += 1;
  }

  while (left <= mid) {
    tmp[k] = arr[left];
    left += 1;
    k += 1;
  }

  while (right <= high) {
    tmp[k] = arr[right];
    right += 1;
    k += 1;
  }

  for (int i = low; i <= high; i++) {
    arr[i] = tmp[i-low];
  }
}

void mergeSort(int *arr, int low, int high) {
  if (low >= high) {
    return;
  }

  int mid = (low + high) / 2;
  mergeSort(arr, low, mid);
  mergeSort(arr, mid+1, high);
  merge(arr, low, mid, high);
}

void printArr(int *arr, int n) {
  for (int i=0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

int main() {
  int arr[4] = {10, 12, 5, 7};
  int n = sizeof(arr)/sizeof(arr[0]);

  mergeSort(arr, 0, n);
  printArr(arr, n);
}
