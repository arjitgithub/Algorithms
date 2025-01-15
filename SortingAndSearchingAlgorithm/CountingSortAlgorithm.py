'''
Counting Sort Algorithm
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of
occurrences of each unique element in the array. The count is stored in an auxiliary array and the
sorting is done by mapping the count as an index of the auxiliary array.

Working of Counting Sort
1. Find out the maximum element (let it be max) from the given array.
2. Initialize an array of length max+1 with all elements 0.
   This array is used for storing the count of the elements in the array.
3. Store the count of each element at their respective index in count array.
   For example: if the count of element 3 is 2 then, 2 is stored in the 3rd position of count
   array.
   If element "5" is not present in the array, then 0 is stored in 5th position.
4. Store cumulative sum of the elements of the count array.
   It helps in placing the elements into the correct index of the sorted array.
5. Find the index of each element of the original array in the count array.
   This gives the cumulative count. Place the element at the index calculated as shown in figure
   below.
6. After placing each element at its correct position, decrease its count by one.

Counting Sort Algorithm
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1

'''

# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * (max(array) + 1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, (max(array) + 1)):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

'''
// Counting sort in Java programming

import java.util.Arrays;

class CountingSort {
  void countSort(int array[], int size) {
    int[] output = new int[size + 1];

    // Find the largest element of the array
    int max = array[0];
    for (int i = 1; i < size; i++) {
      if (array[i] > max)
        max = array[i];
    }
    int[] count = new int[max + 1];

    // Initialize count array with all zeros.
    for (int i = 0; i < max; ++i) {
      count[i] = 0;
    }

    // Store the count of each element
    for (int i = 0; i < size; i++) {
      count[array[i]]++;
    }

    // Store the cummulative count of each array
    for (int i = 1; i <= max; i++) {
      count[i] += count[i - 1];
    }

    // Find the index of each element of the original array in count array, and
    // place the elements in output array
    for (int i = size - 1; i >= 0; i--) {
      output[count[array[i]] - 1] = array[i];
      count[array[i]]--;
    }

    // Copy the sorted elements into original array
    for (int i = 0; i < size; i++) {
      array[i] = output[i];
    }
  }

  // Driver code
  public static void main(String args[]) {
    int[] data = { 4, 2, 2, 8, 3, 3, 1 };
    int size = data.length;
    CountingSort cs = new CountingSort();
    cs.countSort(data, size);
    System.out.println("Sorted Array in Ascending Order: ");
    System.out.println(Arrays.toString(data));
  }
}
'''