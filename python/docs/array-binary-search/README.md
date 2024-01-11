# Challenge Title
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![White board](binarySeacrh.png)

## Approach & Efficiency
First, set two pointers for higher and lower numbers. Then, look for the middle value. Check if it is the middle value; if so, return the middle value's index. If not, repeat the sequence, adjusting the middle value to the lower or higher pointer. Continue this process until the desired value is found. If the value is not found, return -1

## Solution
